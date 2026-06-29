# PA3 - Pruebas Unitarias, TDD y ORM

Proyecto académico pequeño para el Producto Académico n.° 3. El alcance se mantuvo intencionalmente reducido para evidenciar buenas prácticas de pruebas unitarias, ciclo TDD y persistencia con ORM sin convertir el trabajo en un sistema grande.

## Alcance del proyecto

- Gestor personal de tareas con categorías.
- Kata **String Calculator** como evidencia explícita de TDD.
- Persistencia con **SQLAlchemy ORM** sobre **SQLite**.
- Pruebas unitarias y de integración local con `pytest`.
- Documentación académica en español.

## Funcionalidades implementadas

- Crear categoría.
- Crear tarea asociada a una categoría.
- Marcar tarea como completada.
- Listar tareas por categoría.

## Requisitos

- Python 3.12 o superior.
- `git` opcional para preparación local del repositorio.

## Instalación local

```bash
python3 -m venv .venv
.venv/bin/pip install -e .[dev]
```

## Comandos principales

```bash
.venv/bin/pytest
.venv/bin/pytest tests/test_kata_string_calculator.py
.venv/bin/pytest tests/test_domain_service.py
.venv/bin/pytest tests/test_repository_orm.py
.venv/bin/ruff check .
.venv/bin/basedpyright
```

## Estructura del proyecto

```text
PA3_Pruebas_Unitarias_TDD_ORM/
├── docs/
├── src/
│   └── gestor_tareas/
│       ├── domain/
│       ├── infrastructure/
│       └── kata/
├── tests/
├── .gitignore
├── pyproject.toml
└── README.md
```

## Evidencias académicas

- Evidencia del ciclo **Red → Green → Refactor**: `docs/tdd_evidence.md`
- Informe técnico en borrador: `docs/technical_report.md`
- Informe técnico para entrega en Word: `docs/technical_report.doc`

## Nota para la entrega en GitHub

Este proyecto quedó listo para una futura subida a GitHub, pero en esta implementación no se creó ningún repositorio remoto ni se hizo `push`. Cuando el repositorio exista, basta con enlazar el remoto y subir esta carpeta con su historial local.
