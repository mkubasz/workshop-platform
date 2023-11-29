from typing import Generic, Protocol, TypeVar, Iterator
from command import Command
from event import Event


State = TypeVar('State')


class Decider(Protocol[State]):
    def decide(self, command: Command, state: State) -> Event | Iterator[Event] | None: ...
    def evolve(self, current_state: State, event: Event) -> State | None: ...
    def initial_state(self) -> State | None: ...
