import os
from dotenv import load_dotenv
from pathlib import Path

# Always load .env from project root
ROOT_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = ROOT_DIR / ".env"

load_dotenv(dotenv_path=ENV_PATH)

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

print("DEBUG ENV PATH:", ENV_PATH)
print("DEBUG GITHUB_TOKEN LOADED:", bool(GITHUB_TOKEN))
print("DEBUG GROQ_API_KEY LOADED:", bool(GROQ_API_KEY))

if not GITHUB_TOKEN:
    raise ValueError("Missing GITHUB_TOKEN")

if not GROQ_API_KEY:
    raise ValueError("Missing GROQ_API_KEY")


