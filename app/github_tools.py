from github import Github
from git import Repo
from app.config import GITHUB_TOKEN

github = Github(GITHUB_TOKEN)

def create_repository(name, description=""):
    user = github.get_user()
    repo = user.create_repo(
        name=name,
        description=description,
        private=False,
        auto_init=True
    )
    return repo.clone_url


def commit_and_push(repo_path, commit_msg):
    repo = Repo(repo_path)
    repo.git.add(A=True)
    repo.index.commit(commit_msg)
    repo.remote(name="origin").push()
    return "Changes committed & pushed successfully."


def create_issue(repo_name, title, body):
    repo = github.get_repo(repo_name)
    return repo.create_issue(title=title, body=body).html_url


def create_pull_request(repo_name, title, body, head, base="main"):
    repo = github.get_repo(repo_name)
    return repo.create_pull(title=title, body=body, head=head, base=base).html_url


def audit_repository(repo_name):
    repo = github.get_repo(repo_name)
    findings = []

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
