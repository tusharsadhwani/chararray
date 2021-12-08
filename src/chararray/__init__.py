"""
chararray(chars='')

Standard mutable character array implementation.

If no argument is given, it creates an empty chararray.
The argument must be an iterable of characters, if specified.
"""
from collections import UserList
from typing import Iterable


class chararray(UserList[str]):
    def __init__(self, chars: Iterable[str] = "") -> None:
        if not isinstance(chars, Iterable):
            raise ValueError(f"Expected a list of characters, got {type(chars)}")

        char_list = list(chars)
        for char in chars:
            if not isinstance(char, str):
                raise ValueError(
                    f"Expected a list of characters, got {type(char)}",
                )
            if len(char) != 1:
                raise ValueError("Expected a list of characters, not a list of strings")

        super().__init__(char_list)

    def __repr__(self) -> str:
        if len(self) == 0:
            return "chararray()"

        return f"chararray('{''.join(self)}')"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, str):
            return self == chararray(other)

        return super().__eq__(other)

    def __setitem__(self, index, item):
        if not isinstance(item, str):
            raise TypeError(f"Expected character, got {type(item)}")

        if isinstance(index, int) and len(item) != 1:
            raise ValueError("Expected single character, got string of length != 1")

        super().__setitem__(index, item)
