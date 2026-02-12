from dataclasses import dataclass


@dataclass(frozen=True)
class Repo:
    id: int
    name: str
    full_name: str

    @classmethod
    def from_json(cls, data: dict) -> "Repo":
        return cls(
            id=int(data["id"]),
            name=str(data["name"]),
            full_name=str(data["full_name"]),
        )
