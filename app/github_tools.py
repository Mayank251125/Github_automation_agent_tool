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


def commit_and_push(repo_path, commit_msg):
    try:
        repo = Repo(repo_path)
        repo.git.add(A=True)
        repo.index.commit(commit_msg)
        repo.remote(name="origin").push()
        return "Changes committed & pushed successfully."
    except (InvalidGitRepositoryError, NoSuchPathError):
        return "Invalid git repository path."
    except Exception as e:
        return f"Git Error: {str(e)}"


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

