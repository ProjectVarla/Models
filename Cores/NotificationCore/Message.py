from pydantic import BaseModel

class NotificationMessage(BaseModel):
    channel_name:str
    message: str
