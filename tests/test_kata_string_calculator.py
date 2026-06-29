import pytest

from gestor_tareas.kata.string_calculator import NegativeNumberError, StringCalculator


def test_add_returns_zero_when_input_is_empty() -> None:
    # Given
    calculator = StringCalculator()

    # When
    result = calculator.add("")

    # Then
    assert result == 0


def test_add_returns_same_number_when_input_has_one_number() -> None:
    # Given
    calculator = StringCalculator()

    # When
    result = calculator.add("7")

    # Then
    assert result == 7


def test_add_sums_numbers_separated_by_commas_or_new_lines() -> None:
    # Given
    calculator = StringCalculator()

    # When
    result = calculator.add("1,2\n3")

    # Then
    assert result == 6


def test_add_supports_custom_delimiter() -> None:
    # Given
    calculator = StringCalculator()

    # When
    result = calculator.add("//;\n1;2;3")

    # Then
    assert result == 6


def test_add_raises_typed_error_when_input_contains_negative_numbers() -> None:
    # Given
    calculator = StringCalculator()

    # When / Then
    with pytest.raises(NegativeNumberError) as error:
        _ = calculator.add("1,-2,-5")

    assert error.value.numbers == (-2, -5)
