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
            raise ValueError("Expected a list of characters, got", type(self))

        char_list = list(chars)
        for char in chars:
            if not isinstance(char, str):
                raise ValueError("Expected a list of characters, got", type(char))
            if len(char) != 1:
                raise ValueError("Expected a list of characters, not a list of strings")

        super().__init__(char_list)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, str):
            return self == chararray(other)

        return super().__eq__(other)

    def __repr__(self) -> str:
        if len(self) == 0:
            return "chararray()"

        return f"chararray('{''.join(self)}')"
