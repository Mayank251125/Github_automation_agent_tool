from langchain.agents import initialize_agent, AgentType
from langchain.llms.base import LLM
from langchain.tools.github import GitHubToolkit
from github import Github
from groq import Groq
from typing import Optional, List
from app.config import GITHUB_TOKEN, GROQ_API_KEY


class GroqLLM(LLM):
    client: Groq
    model: str = "llama-3.1-70b-versatile"


    def __init__(self):
        super().__init__()
        self.client = Groq(api_key=GROQ_API_KEY)

    @property
    def _llm_type(self) -> str:
        return "groq-llama3-70b"

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1,
        )
        return response.choices[0].message.content


def create_agent():
    llm = GroqLLM()

    github_client = Github(GITHUB_TOKEN)
    toolkit = GitHubToolkit.from_github_client(github_client)

    agent = initialize_agent(
        tools=toolkit.get_tools(),
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    return agent

