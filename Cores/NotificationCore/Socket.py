from dataclasses import dataclass

from starlette.websockets import WebSocket


@dataclass
class Socket:
    websocket: WebSocket
    acknowledged: bool
