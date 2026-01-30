from github import Github
from git import Repo, InvalidGitRepositoryError, NoSuchPathError
from app.config import GITHUB_TOKEN

github = Github(GITHUB_TOKEN)


def create_repository(name, description=""):
    try:
        user = github.get_user()
        repo = user.create_repo(
            name=name,
            description=description,
            private=False,
            auto_init=True
        )
        return repo.clone_url
    except Exception as e:
        return f"GitHub Error: {str(e)}"


import tempfile
import shutil
from git import Repo
import os
from dotenv import load_dotenv
import os

load_dotenv()

def commit_and_push(repo_url: str, message: str):
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        raise ValueError("GITHUB_TOKEN not found in environment")

    # Inject token into HTTPS URL
    auth_repo_url = repo_url.replace(
        "https://",
        f"https://{token}@"
    )

    temp_dir = tempfile.mkdtemp()

    try:
        repo = Repo.clone_from(auth_repo_url, temp_dir)

        readme_path = os.path.join(temp_dir, "README.md")
        if not os.path.exists(readme_path):
            with open(readme_path, "w", encoding="utf-8") as f:
                f.write("# Automated Commit\n\nInitial commit.")

        repo.git.add(A=True)
        repo.index.commit(message)
        repo.remote(name="origin").push()

        return "Commit & push successful!"

    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)




def create_issue(repo_name, title, body):
    try:
        repo = github.get_repo(repo_name)
        issue = repo.create_issue(title=title, body=body)
        return issue.html_url
    except Exception as e:
        return f"GitHub Error: {str(e)}"


def create_pull_request(repo_name, title, body, head, base="main"):
    try:
        repo = github.get_repo(repo_name)
        pr = repo.create_pull(title=title, body=body, head=head, base=base)
        return pr.html_url
    except Exception as e:
        return f"GitHub Error: {str(e)}"


def audit_repository(repo_name):
    findings = []
    try:
        repo = github.get_repo(repo_name)

        try:
            repo.get_readme()
        except:
            findings.append("Missing README.md")

        try:
            repo.get_contents(".github/workflows")
        except:
            findings.append("Missing CI/CD workflows")

        try:
            repo.get_contents(".gitignore")
        except:
            findings.append("Missing .gitignore")

        return findings or ["Repository follows best practices."]

    except Exception as e:
        return [f"Audit Error: {str(e)}"]

