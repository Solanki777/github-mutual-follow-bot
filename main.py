
import os
import requests

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


def main():
    print("GitHub Mutual Follow Bot - DRY RUN")

    followers = get_users("/user/followers")
    following = get_users("/user/following")

    to_follow = followers - following
    to_unfollow = following - followers

    print("\n========== REPORT ==========")
    print("Total followers:", len(followers))
    print("Total following:", len(following))

    print("\nPeople to follow:")
    for user in sorted(to_follow):
        print("+", user)

    print("\nNon-mutual follows to review:")
    for user in sorted(to_unfollow):
        print("-", user)

    print("\nNo accounts were changed.")


if __name__ == "__main__":
    main()
