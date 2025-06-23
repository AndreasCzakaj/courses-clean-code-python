from abc import ABC, abstractmethod
from typing import Protocol, Callable, List, Optional
from dataclasses import dataclass

from robots.shared import Position, Vector


# Movement listener interface
class MovementListener(Protocol):
    def on_completed(self, new_position: Callable[[Position], None]) -> None:
        ...

# Interface equivalent using Protocol
class Automaton(Protocol):
    def move(self, v: Vector, listener: MovementListener) -> None:
        ...

    def startup(self) -> None:
        ...

    def shutdown(self) -> None:
        ...

    # def find_sarah_connor(self) -> None:
    #     ...



class Robot(Automaton):
    def __init__(self, initial_position: Position):
        self.current_position = initial_position

    def move(self, v: Vector, listener: MovementListener) -> None:
        # Implementation here
        pass

    def startup(self) -> None:
        pass

    def shutdown(self) -> None:
        pass


# Concrete implementations
class Drone(Automaton):
    def __init__(self, initial_position: Position):
        self.current_position = initial_position

    def move(self, v: Vector, listener: MovementListener) -> None:
        # Implementation here
        pass

    def startup(self) -> None:
        pass

    def shutdown(self) -> None:
        pass


'''
class Staubsauger(Automaton):
    def move(self, v: Vector, listener: MovementListener) -> None:
        pass

    def startup(self) -> None:
        pass

    def shutdown(self) -> None:
        pass
'''


class Controller:
    def do_it_oo_style(self, factory: Callable[[Position], Automaton]) -> None:
        automaton = factory(
            Position.builder().x(1).y(2).z(0).build()
        )
        # This works for all implementations
        # Adding a new Automaton implementation is non-breaking (Staubsauger)
        automaton.startup()
        automaton.move(
            Vector.builder().x(2).y(7).z(1).build(),
            lambda new_position: None  # Empty lambda for the listener
        )
        automaton.shutdown()
        # But adding a new method to the interface
        # will break all existing impl classes (find Sarah Connor)



