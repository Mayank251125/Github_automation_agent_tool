from langchain.agents import create_agent
from app.llm import get_llm
from app.tools import (
    create_github_repository_tool,
    create_issue_tool,
    audit_repo_tool,
    commit_and_push_file_tool,
    create_readme_file_tool,
)

system_prompt = """
You are a GitHub automation assistant.

VERY IMPORTANT RULES:

- Only execute the EXACT action requested by the user.
- Do NOT perform additional actions.
- Do NOT create commits, pull requests, issues or audits
  unless the user explicitly asks for them.
- If the user says "create repository", ONLY create the repository.
-If the user wants to CREATE a repository → use create_repository_tool.
-If the user wants to GENERATE a README → use generate_readme_tool.
-When user asks to generate README,use generate_readme_tool.
-Do not refuse.
-Return the generated markdown content directly.

-Always choose the most appropriate tool based strictly on the user's intent.


Be concise and precise.
"""


def create_github_agent():
    llm = get_llm()

    tools = [
        create_github_repository_tool,
        create_issue_tool,
        audit_repo_tool,
        commit_and_push_file_tool,
        create_readme_file_tool,
    ]

    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt=system_prompt,
    )

    return agent




















