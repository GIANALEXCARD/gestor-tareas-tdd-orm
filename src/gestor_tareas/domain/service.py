from __future__ import annotations

from dataclasses import replace

from gestor_tareas.domain.entities import Category, CategoryId, Task, TaskId
from gestor_tareas.domain.errors import (
    CategoryNotFoundError,
    InvalidCategoryNameError,
    InvalidTaskTitleError,
    TaskNotFoundError,
)
from gestor_tareas.domain.repositories import TaskManagerRepository


class TaskManagerService:
    def __init__(self, repository: TaskManagerRepository) -> None:
        self._repository: TaskManagerRepository
        self._repository = repository

    def create_category(self, name: str) -> Category:
        if name.strip() == "":
            raise InvalidCategoryNameError(name=name)

        return self._repository.create_category(name)

    def create_task(self, title: str, category_id: CategoryId) -> Task:
        if title.strip() == "":
            raise InvalidTaskTitleError(title=title)

        category = self._repository.get_category(category_id)
        if category is None:
            raise CategoryNotFoundError(category_id=category_id)

        return self._repository.create_task(title, category.id)

    def mark_task_done(self, task_id: TaskId) -> Task:
        task = self._repository.get_task(task_id)
        if task is None:
            raise TaskNotFoundError(task_id=task_id)

        completed_task = replace(task, is_done=True)
        return self._repository.update_task(completed_task)

    def list_tasks_by_category(self, category_id: CategoryId) -> list[Task]:
        category = self._repository.get_category(category_id)
        if category is None:
            raise CategoryNotFoundError(category_id=category_id)

        return self._repository.list_tasks_by_category(category.id)
