# GitHub Mutual Follow & Networking Bot

A Python-based GitHub automation project designed to manage mutual followers and help developers build meaningful connections.

Built using Python, GitHub REST API, and GitHub Actions.

## 🚀 Phase 1 — Mutual Follow Synchronization

**Goal:** Maintain only mutual GitHub connections.

### Features
- Automatically follow users who follow your account.
- Detect users who unfollow you.
- Unfollow users who are no longer following you.
- Preserve mutual connections.
- Fetch complete follower and following lists.
- Prevent duplicate follow operations.
- Run automatically using GitHub Actions.
- Support manual workflow execution.
- Secure authentication using GitHub Secrets.

### Workflow

1. Fetch current followers.
2. Fetch current following list.
3. Compare both lists.
4. Follow users who follow you but whom you don't follow.
5. Unfollow users you follow who no longer follow you.
6. Complete synchronization.

## 🌐 Phase 2 — Developer Networking Assistant

**Goal:** Discover developers and manage new networking opportunities.

### Features
- Discover developers based on programming interests.
- Search developers working with Python, AI/ML, cybersecurity, Django and open source.
- Generate a daily list of potential connections.
- Track manually initiated follows.
- Store follow dates and usernames.
- Check follow-back status after 48 hours.
- Categorize connections:
  - Mutual connections
  - Pending follow-backs
  - Non-mutual connections
- Generate connection statistics.
- Provide a review list for connection cleanup.

### 48-Hour Tracking Workflow

1. Discover potential developers.
2. Review and manually follow selected developers.
3. Record the follow date.
4. After 48 hours, check their follow-back status.
5. Update their connection status.
6. Review non-mutual connections and decide whether to unfollow.

## 🛠️ Technology Stack

- Python
- GitHub REST API
- GitHub Actions
- Requests
- SQLite (Phase 2 tracking)
- YAML

## 📂 Project Structure

```text
github-mutual-follow-bot/
│
├── .github/
│   └── workflows/
│       └── follow_sync.yml
│
├── main.py
├── requirements.txt
├── README.md
│
└── future/
    ├── discovery.py
    ├── tracker.py
    ├── database.py
    └── dashboard.py
```

## 📈 Development Roadmap

| Feature | Phase | Status |
|---|---|---|
| Automatic follow-back | 1 | Planned |
| Automatic unfollow detection | 1 | Planned |
| Daily synchronization | 1 | Planned |
| Developer discovery | 2 | Planned |
| Follow history | 2 | Planned |
| 48-hour follow-back tracking | 2 | Planned |
| Networking dashboard | 2 | Planned |

## 🔐 Security

- Store GitHub tokens in repository secrets.
- Never expose personal access tokens in source code.
- Use minimum required permissions.
- Handle API rate limits and errors.

---

**Project:** GitHub Mutual Follow & Networking Bot  
**Language:** Python  
**Automation:** GitHub Actions  
**Purpose:** Developer networking and connection management.