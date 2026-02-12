from dataclasses import dataclass


@dataclass(frozen=True)
class Issue:
    id: int
    number: int
