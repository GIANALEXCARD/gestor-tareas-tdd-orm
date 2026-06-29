from dataclasses import replace

import pytest

from gestor_tareas.domain.entities import Category, CategoryId, Task, TaskId
from gestor_tareas.domain.errors import (
    CategoryNotFoundError,
    InvalidCategoryNameError,
    InvalidTaskTitleError,
    TaskNotFoundError,
)
from gestor_tareas.domain.service import TaskManagerService


class FakeTaskRepository:
    def __init__(self) -> None:
        self._next_category_id: int
        self._next_task_id: int
        self._next_category_id = 1
        self._next_task_id = 1
        self.categories: dict[CategoryId, Category] = {}
        self.tasks: dict[TaskId, Task] = {}

    def create_category(self, name: str) -> Category:
        category_id = CategoryId(self._next_category_id)
        self._next_category_id += 1
        category = Category(id=category_id, name=name)
        self.categories[category_id] = category
        return category

    def get_category(self, category_id: CategoryId) -> Category | None:
        return self.categories.get(category_id)

    def create_task(self, title: str, category_id: CategoryId) -> Task:
        task_id = TaskId(self._next_task_id)
        self._next_task_id += 1
        task = Task(id=task_id, title=title, is_done=False, category_id=category_id)
        self.tasks[task_id] = task
        return task

    def get_task(self, task_id: TaskId) -> Task | None:
        return self.tasks.get(task_id)

    def update_task(self, task: Task) -> Task:
        self.tasks[task.id] = task
        return task

    def list_tasks_by_category(self, category_id: CategoryId) -> list[Task]:
        return [task for task in self.tasks.values() if task.category_id == category_id]


def test_create_category_returns_created_category() -> None:
    # Given
    repository = FakeTaskRepository()
    service = TaskManagerService(repository)

    # When
    created_category = service.create_category("Estudio")

    # Then
    assert created_category.id == CategoryId(1)
    assert created_category.name == "Estudio"


def test_create_category_raises_typed_error_when_name_is_empty() -> None:
    # Given
    repository = FakeTaskRepository()
    service = TaskManagerService(repository)

    # When / Then
    with pytest.raises(InvalidCategoryNameError) as error:
        _ = service.create_category("  ")

    assert error.value.name == "  "


def test_create_task_raises_typed_error_when_title_is_empty() -> None:
    # Given
    repository = FakeTaskRepository()
    service = TaskManagerService(repository)
    category = service.create_category("Estudio")

    # When / Then
    with pytest.raises(InvalidTaskTitleError) as error:
        _ = service.create_task("", category.id)

    assert error.value.title == ""


def test_create_task_raises_typed_error_when_category_does_not_exist() -> None:
    # Given
    repository = FakeTaskRepository()
    service = TaskManagerService(repository)

    # When / Then
    with pytest.raises(CategoryNotFoundError) as error:
        _ = service.create_task("Repasar ORM", CategoryId(999))

    assert error.value.category_id == CategoryId(999)


def test_mark_task_done_updates_task_status() -> None:
    # Given
    repository = FakeTaskRepository()
    service = TaskManagerService(repository)
    category = service.create_category("Curso")
    task = service.create_task("Preparar pruebas", category.id)

    # When
    completed_task = service.mark_task_done(task.id)

    # Then
    assert completed_task.is_done is True
    assert repository.tasks[task.id] == replace(task, is_done=True)


def test_mark_task_done_raises_typed_error_when_task_does_not_exist() -> None:
    # Given
    repository = FakeTaskRepository()
    service = TaskManagerService(repository)

    # When / Then
    with pytest.raises(TaskNotFoundError) as error:
        _ = service.mark_task_done(TaskId(404))

    assert error.value.task_id == TaskId(404)


def test_list_tasks_by_category_returns_only_matching_tasks() -> None:
    # Given
    repository = FakeTaskRepository()
    service = TaskManagerService(repository)
    study = service.create_category("Estudio")
    home = service.create_category("Casa")
    first_task = service.create_task("Leer capítulo de TDD", study.id)
    _ = service.create_task("Ordenar escritorio", home.id)
    second_task = service.create_task("Practicar SQLAlchemy", study.id)

    # When
    tasks = service.list_tasks_by_category(study.id)

    # Then
    assert tasks == [first_task, second_task]
