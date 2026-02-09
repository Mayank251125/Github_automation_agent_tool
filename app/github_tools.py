import requests
import base64
from app.config import GITHUB_TOKEN

BASE_URL = "https://api.github.com"


def _headers():
    return {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json",
    }


def create_repository(name: str, description: str = "", private: bool = False):
    url = f"{BASE_URL}/user/repos"

    response = requests.post(
        url,
        headers=_headers(),
        json={
            "name": name,
            "description": description,
            "private": private,   # 🔥 THIS IS THE IMPORTANT FIX
            "auto_init": True     # optional but recommended (creates initial commit)
        },
    )

    return response.json()


import os

def commit_and_push_file(
    repo: str,
    branch: str,
    file_path: str,
    commit_message: str,
):
    """
    Reads a local file and pushes it to GitHub.
    """

    if not os.path.exists(file_path):
        return {"error": f"File '{file_path}' not found locally."}

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    url = f"{BASE_URL}/repos/{repo}/contents/{file_path}"

    # Check if file exists
    response = requests.get(url, headers=_headers())
    sha = None

    if response.status_code == 200:
        sha = response.json().get("sha")

    data = {
        "message": commit_message,
        "content": base64.b64encode(content.encode()).decode(),
        "branch": branch,
    }

    if sha:
        data["sha"] = sha

    res = requests.put(url, headers=_headers(), json=data)

    return res.json()


def create_issue(repo: str, title: str, body: str):
    # Check existing issues first
    check_url = f"{BASE_URL}/repos/{repo}/issues"
    existing = requests.get(check_url, headers=_headers()).json()

    for issue in existing:
        if issue["title"] == title:
            return {"message": "Issue with this title already exists."}

    url = f"{BASE_URL}/repos/{repo}/issues"

    response = requests.post(
        url,
        headers=_headers(),
        json={"title": title, "body": body},
    )

    return response.json()



def audit_repository(repo: str):
    """
    Audit GitHub repository and return structured JSON.
    Format: username/repository
    """

    if "/" not in repo:
        return {
            "status": "error",
            "message": "Invalid repository format. Use username/repository."
        }

    repo_url = f"{BASE_URL}/repos/{repo}"
    repo_response = requests.get(repo_url, headers=_headers())

    if repo_response.status_code == 404:
        return {
            "status": "error",
            "message": "Repository not found."
        }

    if repo_response.status_code != 200:
        return {
            "status": "error",
            "message": "GitHub API error",
            "code": repo_response.status_code
        }

    missing = []

    # README
    if requests.get(f"{BASE_URL}/repos/{repo}/readme", headers=_headers()).status_code == 404:
        missing.append("Add a README.md file.")

    # LICENSE
    if requests.get(f"{BASE_URL}/repos/{repo}/license", headers=_headers()).status_code == 404:
        missing.append("Add a LICENSE file.")

    # CONTRIBUTING
    if requests.get(f"{BASE_URL}/repos/{repo}/contents/CONTRIBUTING.md", headers=_headers()).status_code == 404:
        missing.append("Add a CONTRIBUTING.md file.")

    # .gitignore
    if requests.get(f"{BASE_URL}/repos/{repo}/contents/.gitignore", headers=_headers()).status_code == 404:
        missing.append("Add a .gitignore file.")

    # GitHub Actions
    if requests.get(f"{BASE_URL}/repos/{repo}/contents/.github/workflows", headers=_headers()).status_code == 404:
        missing.append("Set up GitHub Actions (CI/CD).")

    return {
        "status": "success",
        "repository": repo,
        "missing_items": missing,
        "compliant": len(missing) == 0
    }








