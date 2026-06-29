from dataclasses import dataclass
from typing import Final, override

DEFAULT_DELIMITERS: Final[tuple[str, ...]] = (",", "\n")


@dataclass(frozen=True, slots=True)
class NegativeNumberError(Exception):
    numbers: tuple[int, ...]

    @override
    def __str__(self) -> str:
        negative_values = ", ".join(str(number) for number in self.numbers)
        return f"No se permiten números negativos: {negative_values}"


class StringCalculator:
    def add(self, text: str) -> int:
        delimiter = DEFAULT_DELIMITERS[0]
        payload = text

        if text.startswith("//"):
            header, payload = text.split("\n", maxsplit=1)
            delimiter = header[2:]

        normalized_payload = payload
        for current_delimiter in DEFAULT_DELIMITERS:
            normalized_payload = normalized_payload.replace(
                current_delimiter,
                delimiter,
            )

        if normalized_payload == "":
            return 0

        numbers = [
            int(raw_number) for raw_number in normalized_payload.split(delimiter)
        ]
        negative_numbers = tuple(number for number in numbers if number < 0)
        if negative_numbers:
            raise NegativeNumberError(numbers=negative_numbers)

        return sum(numbers)
