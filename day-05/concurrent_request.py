import asyncio
import httpx

async def fetch_user(client:httpx.AsyncClient, user_id:int) -> dict:
    response = await client.get(
        (
            "https://jsonplaceholder."
            f"typicode.com/users/{user_id}"
        )
    )

    response.raise_for_status()
    return response.json()

async def main():
    async with httpx.AsyncClient() as client:
        tasks = [
            fetch_user(client, user_id)
            for user_id in range(1, 9)
        ]

        users = await asyncio.gather(*tasks)

        for user in users:
            print(user["name"])

asyncio.run(main())