from dataclasses import dataclass
from typing import Protocol, runtime_checkable, Sequence


@dataclass
class Task:
    """
    Структура данных для представления задачи.
    Attributes:
        id: Уникальный идентификатор задачи.
        payload: Произвольные данные задачи.
    """
    id: int
    payload: dict

@runtime_checkable
class TaskProtocol(Protocol):
    """
        Контракт для всех источников задач.
    """
    def get_tasks(self) -> Sequence[Task]:
        ...
