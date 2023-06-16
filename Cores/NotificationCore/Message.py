from pydantic import BaseModel

from .Socket import Verbosity


class NotificationMessage(BaseModel):
    channel_names: list[str]
    message: str
    verbosity: Verbosity = Verbosity.NORMAL
