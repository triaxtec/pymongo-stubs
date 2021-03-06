from typing import Any, Optional, Union, Literal

from pymongo import common as common

class CollationStrength:
    PRIMARY: int = ...
    SECONDARY: int = ...
    TERTIARY: int = ...
    QUATERNARY: int = ...
    IDENTICAL: int = ...

class CollationAlternate:
    NON_IGNORABLE: str = ...
    SHIFTED: str = ...

class CollationMaxVariable:
    PUNCT: str = ...
    SPACE: str = ...

class CollationCaseFirst:
    UPPER: str = ...
    LOWER: str = ...
    OFF: str = ...

class Collation:
    def __init__(
        self,
        locale: str,
        caseLevel: bool = ...,
        caseFirst: Union[Literal["upper"], Literal["lower"], Literal["off"]] = ...,
        strength: Union[Literal[1], Literal[2], Literal[3], Literal[4], Literal[5]] = ...,
        numericOrdering: bool = ...,
        alternate: Union[Literal["non-ignorable"], Literal["shifted"]] = ...,
        maxVariable: Union[Literal["punct"], Literal["space"]] = ...,
        normalization: bool = ...,
        backwards: bool = ...,
        **kwargs: Any,
    ) -> None: ...
    @property
    def document(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...

def validate_collation_or_none(value: Any): ...
