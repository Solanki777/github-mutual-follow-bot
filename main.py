
import os
import json
import requests
from pathlib import Path

API = "https://api.github.com"
TOKEN = os.environ["GH_TOKEN"]
STATE_FILE = Path("state.json")

HEADERS = {
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
            headers=HEADERS,
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
        headers=HEADERS,
        timeout=30
    )
    response.raise_for_status()
    print(f"FOLLOWED: {username}")


def unfollow(username):
    response = requests.delete(
        f"{API}/user/following/{username}",
        headers=HEADERS,
        timeout=30
    )
    response.raise_for_status()
    print(f"UNFOLLOWED: {username}")


def load_state():
    if not STATE_FILE.exists():
        return {
            "initialized": False,
            "followers": [],
            "following": []
        }

    with STATE_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def save_state(followers, following):
    state = {
        "initialized": True,
        "followers": sorted(followers),
        "following": sorted(following)
    }

    with STATE_FILE.open("w", encoding="utf-8") as file:
        json.dump(state, file, indent=2)

    print("State successfully saved.")


def main():
    print("GitHub Mutual Follow Bot Started")

    old_state = load_state()

    followers = get_users("/user/followers")
    following = get_users("/user/following")

    to_follow = followers - following

    # Only remove accounts that were previously mutual.
    previous_mutual = (
        set(old_state["followers"]) &
        set(old_state["following"])
    )

    if old_state["initialized"]:
        to_unfollow = (
            previous_mutual - followers
        ) & following
    else:
        to_unfollow = set()

    print("\n========== REPORT ==========")
    print("Followers:", len(followers))
    print("Following:", len(following))
    print("To follow:", len(to_follow))
    print("Confirmed unfollowers:", len(to_unfollow))

    if not old_state["initialized"]:
        print("\nFirst run: establishing tracking baseline.")
        print("Existing non-mutual accounts will be preserved.")

    for username in sorted(to_follow):
        follow(username)

    for username in sorted(to_unfollow):
        unfollow(username)

    # Save the expected post-sync following list.
    updated_following = (following | to_follow) - to_unfollow

    save_state(followers, updated_following)

    print("\nSynchronization completed!")


if __name__ == "__main__":
    main()
