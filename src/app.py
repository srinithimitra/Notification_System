import uuid
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from src.config import settings
from src.db import Notifications, get_db
from src.models import NotificationPayload
from src.lib.kafka import create_kafka_producer
from src.lib.retry_mechanism import retry_with_exponential_backoff


app = FastAPI(
    title="Notification Service",
    description="""
    A scalable notification API supporting Email, SMS, and In-app messages.
    
    Features:
    - Asynchronous delivery via queue
    - Retry on failure
    - REST endpoints for sending and retrieving notifications
    """,
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/users/{id}/notifications")
def get_user_notifications(id: int, db = Depends(get_db)):
    """
    Get notifications for a user.
    """
    notifications = db.query(Notifications).filter(Notifications.user == id).all()
    if notifications is None or len(notifications) == 0:
        raise HTTPException(status_code=404, detail="Notifications not found for this user.")
    return {"user_id": id, "notifications": notifications}

@app.post("/notifications")
def send_notification(notification: NotificationPayload, producer = Depends(create_kafka_producer)):
    """
    Send a notification.
    """
    # Send the message to a kafka topic
    # For now, just return the notification
    if producer is None:
        return {"error": "Failed to create Kafka producer."}
    try:
        key = str(uuid.uuid4())
        retry_with_exponential_backoff(
            task=producer.produce,
            max_retries=5,
            initial_delay=1,
            backoff_factor=2,
            topic=settings.kafka.topic,
            key=key,
            value=notification.model_dump_json(),
            callback=lambda err, msg: print(f"Message delivery failed: {err}") if err else print(f"Message delivered to {msg.topic()} partition [{msg.partition()}] at offset {msg.offset()}")
        )
        producer.flush()
        return {"status": "Notification sent successfully.", "key": key}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to send notification: {e}")