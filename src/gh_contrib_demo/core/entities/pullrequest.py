from dataclasses import dataclass


@dataclass(frozen=True)
class PullRequest:
    id: int
    number: int
