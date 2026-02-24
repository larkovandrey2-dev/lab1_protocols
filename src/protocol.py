from dataclasses import dataclass
from typing import Protocol, runtime_checkable, Iterable


@dataclass
class Task:
    id: int
    payload: dict

@runtime_checkable
class TaskProtocol(Protocol):
    def get_tasks(self) -> Iterable[Task]:
        ...
