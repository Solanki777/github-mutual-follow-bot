
import os
import requests
import sys

API = "https://api.github.com"
TOKEN = os.environ["GH_TOKEN"]

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28"
}


def get_users(endpoint):
    users = set()
    page = 1

    while True:
        response = requests.get(
            f"{API}{endpoint}",
            headers=headers,
            params={"per_page": 100, "page": page},
            timeout=30
        )
        response.raise_for_status()

        data = response.json()
        users.update(user["login"] for user in data)

        if len(data) < 100:
            break

        page += 1

    return users


def follow(username):
    response = requests.put(
        f"{API}/user/following/{username}",
        headers=headers,
        timeout=30
    )
    response.raise_for_status()
    print(f"FOLLOWED: {username}")


def unfollow(username):
    response = requests.delete(
        f"{API}/user/following/{username}",
        headers=headers,
        timeout=30
    )
    response.raise_for_status()
    print(f"UNFOLLOWED: {username}")


def main():
    print("GitHub Mutual Follow Sync Started")

    followers = get_users("/user/followers")
    following = get_users("/user/following")

    to_follow = followers - following
    to_unfollow = following - followers

    print("Followers:", len(followers))
    print("Following:", len(following))
    print("New mutual follows:", len(to_follow))
    print("Non-mutual follows:", len(to_unfollow))

    for user in sorted(to_follow):
        follow(user)

    for user in sorted(to_unfollow):
        unfollow(user)

    print("Synchronization completed!")


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print("ERROR:", error)
        sys.exit(1)
