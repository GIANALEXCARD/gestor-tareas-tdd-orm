from dataclasses import dataclass
from typing import NewType

CategoryId = NewType("CategoryId", int)
TaskId = NewType("TaskId", int)


@dataclass(frozen=True, slots=True)
class Category:
    id: CategoryId
    name: str


@dataclass(frozen=True, slots=True)
class Task:
    id: TaskId
    title: str
    is_done: bool
    category_id: CategoryId
