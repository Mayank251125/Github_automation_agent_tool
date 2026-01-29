from groq import Groq
from pymarkdown.api import PyMarkdownApi
from app.config import GROQ_API_KEY


def generate_readme(project_name, features):
    client = Groq(api_key=GROQ_API_KEY)

    prompt = f"""
    Create a professional GitHub README.md for:

    Project: {project_name}

    Features:
    {features}

    Include:
    - Project description
    - Features list
    - Installation steps
    - Usage examples
    - Environment setup
    - Contribution guide
    - License
    """

    response = client.chat.completions.create(
       model="llama-3.1-70b-versatile",

        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    readme = response.choices[0].message.content

    PyMarkdownApi().scan_string(readme)

    return readme

