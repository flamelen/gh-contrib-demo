class GithubClient:
    """Very lightweight client placeholder."""

    def __init__(self, token: str, base_url: str = "https://api.github.com") -> None:
        self.token = token
        self.base_url = base_url
