from gestor_tareas.domain.entities import CategoryId
from gestor_tareas.infrastructure.database import (
    create_schema,
    create_session_factory,
    create_sqlite_engine,
)
from gestor_tareas.infrastructure.repository_orm import SqlAlchemyTaskRepository


def test_repository_creates_category_and_task_in_sqlite() -> None:
    # Given
    engine = create_sqlite_engine("sqlite+pysqlite:///:memory:")
    create_schema(engine)
    repository = SqlAlchemyTaskRepository(create_session_factory(engine))
    category = repository.create_category("Académico")

    # When
    task = repository.create_task("Terminar PA3", category.id)

    # Then
    assert category.id == CategoryId(1)
    assert task.id == 1
    assert task.category_id == category.id
    assert task.is_done is False


def test_repository_marks_task_done_persisting_changes() -> None:
    # Given
    engine = create_sqlite_engine("sqlite+pysqlite:///:memory:")
    create_schema(engine)
    repository = SqlAlchemyTaskRepository(create_session_factory(engine))
    category = repository.create_category("Curso")
    task = repository.create_task("Corregir informe", category.id)

    # When
    updated_task = repository.mark_task_done(task.id)

    # Then
    assert updated_task.is_done is True
    assert repository.get_task(task.id) == updated_task


def test_repository_lists_only_tasks_of_requested_category() -> None:
    # Given
    engine = create_sqlite_engine("sqlite+pysqlite:///:memory:")
    create_schema(engine)
    repository = SqlAlchemyTaskRepository(create_session_factory(engine))
    first_category = repository.create_category("Universidad")
    second_category = repository.create_category("Casa")
    task_one = repository.create_task("Estudiar ORM", first_category.id)
    _ = repository.create_task("Lavar platos", second_category.id)
    task_two = repository.create_task("Escribir README", first_category.id)

    # When
    tasks = repository.list_tasks_by_category(first_category.id)

    # Then
    assert tasks == [task_one, task_two]
