# Evidencia TDD: Red -> Green -> Refactor

Este archivo resume los ciclos TDD ejecutados localmente durante la construcción del proyecto.

## 1. Kata String Calculator

### Red

```bash
.venv/bin/pytest tests/test_kata_string_calculator.py
```

Resultado observado:

- `ModuleNotFoundError: No module named 'gestor_tareas.kata'`

### Green

Después de crear `src/gestor_tareas/kata/string_calculator.py`:

```bash
.venv/bin/pytest tests/test_kata_string_calculator.py
```

Resultado observado:

- `5 passed in 0.00s`

### Refactor

Se mantuvo la kata en un módulo separado para que la evidencia TDD quede aislada del resto del proyecto.

## 2. Servicio de dominio

### Red

```bash
.venv/bin/pytest tests/test_domain_service.py
```

Resultado observado:

- `ModuleNotFoundError: No module named 'gestor_tareas.domain'`

### Green

Después de crear las entidades, errores tipados, protocolo de repositorio y servicio de dominio:

```bash
.venv/bin/pytest tests/test_domain_service.py
```

Resultado observado:

- `7 passed`

### Refactor

La lógica del negocio quedó separada de la infraestructura ORM para mantener responsabilidades claras.

## 3. Repositorio ORM

### Red

```bash
.venv/bin/pytest tests/test_repository_orm.py
```

Resultado observado:

- `ModuleNotFoundError: No module named 'gestor_tareas.infrastructure'`

### Green

Después de crear la infraestructura con SQLAlchemy ORM y SQLite:

```bash
.venv/bin/pytest tests/test_repository_orm.py
```

Resultado observado:

- `3 passed in 0.11s`

### Refactor

La persistencia se dividió en dos archivos:

- `database.py` para motor, modelos y esquema.
- `repository_orm.py` para el repositorio concreto.

## 4. Cierre del ciclo

Al finalizar la implementación se ejecutan nuevamente las pruebas, el chequeo estático y el linter para confirmar que el refactor no rompió el comportamiento esperado.

Resultado final observado:

- `.venv/bin/pytest`: `15 passed`
- `.venv/bin/ruff check .`: `All checks passed!`
- `.venv/bin/basedpyright`: `0 errors, 0 warnings, 0 notes`
