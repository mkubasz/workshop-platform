from typing import Protocol, TypeVar

EventType = str
EventData = TypeVar("EventData")


class Event(Protocol[EventData]):
    type: EventType
    data: EventData
