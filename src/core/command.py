from typing import Protocol, TypeVar

CommandType = str
CommandData = TypeVar("CommandData")


class Command(Protocol[CommandData]):
    type: CommandType
    data: CommandData
