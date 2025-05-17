from pydantic import BaseModel
from datetime import datetime, timezone

class NotificationPayload(BaseModel):
    """
    Notification payload model.
    """
    user: str
    message: str