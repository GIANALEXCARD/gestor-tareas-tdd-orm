from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session, sessionmaker

from gestor_tareas.domain.entities import Category, CategoryId, Task, TaskId
from gestor_tareas.domain.errors import TaskNotFoundError
from gestor_tareas.infrastructure.database import CategoryModel, TaskModel


class SqlAlchemyTaskRepository:
    def __init__(self, session_factory: sessionmaker[Session]) -> None:
        self._session_factory: sessionmaker[Session]
        self._session_factory = session_factory

    def create_category(self, name: str) -> Category:
        with self._session_factory() as session:
            category_model = CategoryModel(name=name)
            session.add(category_model)
            session.commit()
            session.refresh(category_model)
            return self._to_category(category_model)

    def get_category(self, category_id: CategoryId) -> Category | None:
        with self._session_factory() as session:
            category_model = session.get(CategoryModel, int(category_id))
            if category_model is None:
                return None

            return self._to_category(category_model)

    def create_task(self, title: str, category_id: CategoryId) -> Task:
        with self._session_factory() as session:
            task_model = TaskModel(
                title=title,
                is_done=False,
                category_id=int(category_id),
            )
            session.add(task_model)
            session.commit()
            session.refresh(task_model)
            return self._to_task(task_model)

    def get_task(self, task_id: TaskId) -> Task | None:
        with self._session_factory() as session:
            task_model = session.get(TaskModel, int(task_id))
            if task_model is None:
                return None

            return self._to_task(task_model)

    def update_task(self, task: Task) -> Task:
        with self._session_factory() as session:
            task_model = session.get(TaskModel, int(task.id))
            if task_model is None:
                raise TaskNotFoundError(task_id=task.id)

            task_model.title = task.title
            task_model.is_done = task.is_done
            task_model.category_id = int(task.category_id)
            session.commit()
            session.refresh(task_model)
            return self._to_task(task_model)

    def mark_task_done(self, task_id: TaskId) -> Task:
        with self._session_factory() as session:
            task_model = session.get(TaskModel, int(task_id))
            if task_model is None:
                raise TaskNotFoundError(task_id=task_id)

            task_model.is_done = True
            session.commit()
            session.refresh(task_model)
            return self._to_task(task_model)

    def list_tasks_by_category(self, category_id: CategoryId) -> list[Task]:
        with self._session_factory() as session:
            task_models = session.scalars(
                select(TaskModel)
                .where(TaskModel.category_id == int(category_id))
                .order_by(TaskModel.id)
            ).all()
            return [self._to_task(task_model) for task_model in task_models]

    @staticmethod
    def _to_category(category_model: CategoryModel) -> Category:
        return Category(id=CategoryId(category_model.id), name=category_model.name)

    @staticmethod
    def _to_task(task_model: TaskModel) -> Task:
        return Task(
            id=TaskId(task_model.id),
            title=task_model.title,
            is_done=task_model.is_done,
            category_id=CategoryId(task_model.category_id),
        )
