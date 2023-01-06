from typing import Any, List, Optional

from pydantic import BaseModel


class Command(BaseModel):
    command: str
    short_hand: Optional[str] = None
    options: Optional[list[str]]
    action: Any
    help: str = ""


class Registry(BaseModel):
    command: Command
    subcommands: Optional[List[Command]] = []

    def trigger(self) -> None:
        self.command.action()
