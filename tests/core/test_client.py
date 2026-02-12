from gh_contrib_demo.core.client import GithubClient


def test_github_client_fields() -> None:
    client = GithubClient(token="tkn", base_url="https://api.github.com")
    assert client.token == "tkn"
    assert client.base_url == "https://api.github.com"
