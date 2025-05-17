import uvicorn
import multiprocessing
from src.app import app
from src.lib.kafka import create_kafka_consumer

if __name__ == "__main__":
    try:
        # Create the kafka consumer process
        kafka_process = multiprocessing.Process(target=create_kafka_consumer)
        # Start the kafka consumer process
        kafka_process.start()
        print("Kafka consumer started with PID:", kafka_process.pid)
        # Start the FastAPI server
        uvicorn.run(app)
        # Wait for the kafka consumer process to finish
        kafka_process.join()
    except KeyboardInterrupt:
        print("Server stopped.")
        print("Kafka consumer stopped.")