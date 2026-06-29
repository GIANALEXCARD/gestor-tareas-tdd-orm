from __future__ import annotations

from dataclasses import dataclass
from typing import override

from gestor_tareas.domain.entities import CategoryId, TaskId


@dataclass(frozen=True, slots=True)
class InvalidCategoryNameError(Exception):
    name: str

    @override
    def __str__(self) -> str:
        return "El nombre de la categoría no puede estar vacío"


@dataclass(frozen=True, slots=True)
class InvalidTaskTitleError(Exception):
    title: str

    @override
    def __str__(self) -> str:
        return "El título de la tarea no puede estar vacío"


@dataclass(frozen=True, slots=True)
class CategoryNotFoundError(Exception):
    category_id: CategoryId

    @override
    def __str__(self) -> str:
        return f"No existe la categoría con id {self.category_id}"


@dataclass(frozen=True, slots=True)
class TaskNotFoundError(Exception):
    task_id: TaskId

    @override
    def __str__(self) -> str:
        return f"No existe la tarea con id {self.task_id}"
