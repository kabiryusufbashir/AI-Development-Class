from app.clients.api_client import (
    APIClient
)


class UserService:

    def __init__(self, client: APIClient) -> None:

        self.client = client

    def get_user(self, user_id: int) -> dict:

        return self.client.get(
            f"/users/{user_id}"
        )