from typing import Any, List, Optional

from pydantic import BaseModel

from VarlaLib.Shell import VarlaCLI as Varla


class Command(BaseModel):
    command: str
    short_hand: Optional[str] = None
    options: Optional[list[str]]
    action: Any
    help: str = ""


class Registry(BaseModel):
    command: Command
    subcommands: Optional[List[Command]] = []

    def trigger(self, *sub_command) -> None:

        try:
            if len(*sub_command):
                self.command.action(*sub_command)
            else:
                self.command.action()

        except Exception as e:
            Varla.say(str(self.command.__dict__))
            Varla.error(str(e))
            pass
