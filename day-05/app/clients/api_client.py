import httpx


class APIClient:

    def __init__(self, base_url: str, token: str | None = None) -> None:

        self.base_url = (
            base_url.rstrip("/")
        )

        self.headers = {
            "Accept": "application/json"
        }

        if token:
            self.headers[
                "Authorization"
            ] = f"Bearer {token}"

    def get(self, endpoint: str) -> dict | list:

        url = (
            f"{self.base_url}/{endpoint.lstrip('/')}"
        )

        response = httpx.get(
            url,
            headers=self.headers,
            timeout=10
        )

        response.raise_for_status()

        return response.json()

if __name__ == "__main__":
    client = APIClient(
        base_url=(
            "https://jsonplaceholder."
            "typicode.com"
        )
    )

    user = client.get("/users/2")

    print(user)