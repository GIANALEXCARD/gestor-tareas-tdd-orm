# Borrador de informe técnico

## Datos del estudiante

- **Estudiante:** Giancarlos Alexis Cardenas Galarza
- **Curso:** Simulación
- **Producto académico:** Producto Académico n.° 3 - Pruebas Unitarias y TDD
- **Proyecto desarrollado:** Gestor personal de tareas con categorías y kata String Calculator

## 1. Resumen del proyecto

Se desarrolló un proyecto pequeño en Python con la finalidad de demostrar competencias en pruebas unitarias, desarrollo guiado por pruebas (TDD) y uso de ORM. El sistema implementado es un gestor personal de tareas con categorías, persistencia local en SQLite mediante SQLAlchemy ORM y una kata adicional de String Calculator para mostrar el ciclo Red-Green-Refactor de manera puntual.

La solución fue diseñada con un alcance reducido porque el objetivo de la evaluación no es construir un producto complejo, sino evidenciar una práctica técnica correcta, comprensible y fácil de sustentar.

## 2. Objetivo académico

Aplicar pruebas unitarias y TDD en un proyecto pequeño, integrando además una capa de persistencia con ORM y una documentación que explique cómo las pruebas se incorporan dentro de un flujo de trabajo ágil.

## 3. Descripción de la solución implementada

El proyecto se organizó con estructura `src/` y se dividió en tres partes principales:

1. **Dominio**: entidades `Category` y `Task`, errores tipados y servicio de aplicación.
2. **Infraestructura ORM**: repositorio con SQLAlchemy para SQLite.
3. **Kata TDD**: implementación de String Calculator.

Las funcionalidades del gestor son:

- crear categorías;
- crear tareas asociadas a una categoría;
- marcar tareas como completadas;
- listar tareas por categoría.
- validar que los nombres de categorías y títulos de tareas no estén vacíos.

## 4. Mapeo con la rúbrica

| Criterio de evaluación | Evidencia en el proyecto |
|---|---|
| Pruebas unitarias | Archivos `tests/test_kata_string_calculator.py`, `tests/test_domain_service.py` y `tests/test_repository_orm.py` |
| Ciclo TDD Red-Green-Refactor | Documento `docs/tdd_evidence.md` con fallas iniciales y validaciones posteriores |
| Katas TDD | Implementación de `StringCalculator` en `src/gestor_tareas/kata/string_calculator.py` |
| Uso de ORM | Repositorio `SqlAlchemyTaskRepository` y modelos SQLAlchemy en `src/gestor_tareas/infrastructure/` |
| Integración ágil de pruebas | Ejecución frecuente de `pytest`, diseño incremental y separación de responsabilidades |
| Documentación técnica | `README.md` y este informe técnico |

## 5. Evidencia del ciclo Red-Green-Refactor

El trabajo siguió una secuencia incremental:

### 5.1 Red

Primero se escribieron los tests requeridos. Al ejecutarlos, el proyecto falló porque todavía no existían los módulos `kata`, `domain` e `infrastructure`. Estas fallas fueron correctas porque demostraron que las pruebas estaban guiando la construcción del código.

### 5.2 Green

Luego se implementó el mínimo código necesario para que cada bloque de pruebas pase:

- primero la kata String Calculator;
- después el servicio de dominio;
- finalmente el repositorio ORM.

### 5.3 Refactor

Con las pruebas en verde, la estructura quedó organizada en carpetas separadas por responsabilidad (`kata`, `domain`, `infrastructure`). Esto evita mezclar reglas de negocio con persistencia y facilita explicar el diseño durante la sustentación.

## 6. Kata String Calculator

La kata se usó como evidencia específica de TDD. Se implementaron los siguientes casos:

- cadena vacía devuelve `0`;
- un solo número devuelve ese mismo valor;
- números separados por coma o salto de línea se suman correctamente;
- se acepta delimitador personalizado;
- los números negativos generan un error tipado.

Esta parte demuestra que el desarrollo guiado por pruebas no solo se aplica a sistemas con base de datos, sino también a lógica de negocio pequeña y autocontenida.

## 7. Uso de ORM con SQLAlchemy y SQLite

Se utilizó SQLAlchemy ORM con SQLite para mantener la solución local y simple. Se modelaron dos entidades persistentes:

- **Category**: `id`, `name`
- **Task**: `id`, `title`, `is_done`, `category_id`

La persistencia se probó con SQLite en memoria, lo que permite correr tests rápidos y repetibles. Esto resulta adecuado para un trabajo académico donde se necesita demostrar funcionamiento sin depender de servicios externos.

## 8. Integración de pruebas en un flujo ágil

La integración ágil de pruebas se evidencia en los siguientes puntos:

- los tests se escribieron antes de la implementación correspondiente;
- cada bloque funcional se validó por separado;
- la retroalimentación fue inmediata con `pytest`;
- la estructura pequeña permite iterar y corregir rápido;
- la documentación quedó alineada con el código y las pruebas.

La verificación final ejecutada localmente fue `15 passed`, cubriendo la kata, el servicio de dominio y la integración ORM con SQLite.

Este enfoque se relaciona con prácticas ágiles porque reduce retrabajo, hace visible el progreso y favorece cambios pequeños con verificación constante.

## 9. Conclusiones

El proyecto cumple con el objetivo de mostrar una aplicación pequeña, entendible y verificable mediante pruebas. La kata evidencia el proceso TDD a nivel de lógica simple, mientras que el gestor de tareas demuestra cómo aplicar el mismo enfoque junto con un ORM y persistencia local.

## 10. Pendiente para la entrega final

Como siguiente paso administrativo, el contenido de esta carpeta debe subirse a un repositorio GitHub cuando el estudiante cree el remoto correspondiente. En esta etapa solo se dejó la base local lista para esa publicación.
