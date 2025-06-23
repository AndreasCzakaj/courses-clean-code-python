from abc import ABC, abstractmethod
from typing import Protocol, Callable, List, Optional

from robots.shared import Position


# Abstract class equivalent
class AutomatonDto(ABC):
    def __init__(self):
        self.started: bool = False
        self.current_position: Optional['Position'] = None
        self.battery: int = 0


class RobotDto(AutomatonDto):
    def __init__(self):
        super().__init__()


class DroneDto(AutomatonDto):
    def __init__(self):
        super().__init__()
        self.camera_stream: Optional[List[int]] = None


'''
class StaubsaugerDto(AutomatonDto):
    def __init__(self):
        super().__init__()
'''


class Controller:
    def start_procedurally(self, factory: Callable[[Position], AutomatonDto]) -> None:
        automaton = factory(
            Position.builder().x(1).y(2).z(0).build()
        )
        if not automaton.started:
            if isinstance(automaton, DroneDto):
                if automaton.battery > 4500:
                    automaton.camera_stream = []
                    automaton.started = True
            elif isinstance(automaton, RobotDto):
                if automaton.battery > 3500:
                    # do stuff
                    automaton.started = True

    # It's easy to add this new function... or find Sarah Connor
    def move_procedurally(self, factory: Callable[[Position], AutomatonDto]) -> None:
        automaton = factory(
            Position.builder().x(1).y(2).z(0).build()
        )
        if automaton.started:
            if isinstance(automaton, DroneDto):
                # ...
                pass
            elif isinstance(automaton, RobotDto):
                # ...
                pass
            # Adding a new Dto class will require to add another case
            # to do_it_procedurally and all the other functions (Stabsauger)
            # => just like the car type disaster