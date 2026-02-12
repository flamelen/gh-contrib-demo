from gh_contrib_demo.core.entities.repository import Repo


def test_repo_from_json_example() -> None:
    payload = {"id": 1, "name": "demo", "full_name": "org/demo"}
    repo = Repo.from_json(payload)

    assert repo.id == 1
    assert repo.name == "demo"
    assert repo.full_name == "org/demo"
