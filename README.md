# GitHub Automation Agent

---

## Overview

The **GitHub Automation Agent** is a Chat-based intelligent system that automates common GitHub workflows using natural language instructions. It integrates LLM-powered reasoning with GitHub API tools to perform repository management, issue handling,audit or recommend best github practices, and automated README generation.

The project focuses exclusively on the GitHub Automation Agent component of a larger multi-agent AI architecture. It is built using LangChain with an API-based LLM backend and emphasizes modular design, automation reliability, and extensibility rather than UI complexity.

---

## Demo Video

 👉 **https://drive.google.com/file/d/1mS60S_hcMCWruB_v0rU2JU6mtRsTMoII/view?usp=drive_link**

---

## 📁 Project Structure

```
GITHUB-AUTOMATION-AGENT
│
├── app/
│ ├── init.py
│ ├── agent.py             # Core agent logic and orchestration
│ ├── config.py            # Environment configuration
│ ├── github_tools.py      # GitHub API interaction functions
│ ├── llm.py               # LLM setup and configuration
│ ├── readme_generator.py  # README generation logic
│ ├── tools.py             # Tool definitions
│
├── chat.py                # Chat interaction entry point
├── requirements.txt       # Project dependencies
├── .env                   # Environment variables (excluded from Git)
├── .gitignore             # Git ignore rules
├── README.md              # Project documentation

```

---

## Key Capabilities

- Natural language → GitHub action execution  
- Repository creation and management  
- Issue creation and listing  
- Automated README generation  
- Files commit and push
- Audit Github repository 
- Modular tool-based architecture  
- Chat-based interaction  
- Secure environment-based authentication  

---

## Safety Design

The agent is designed with controlled GitHub API execution:

- All GitHub operations are executed via authenticated API calls
- Sensitive credentials are stored securely using `.env`
- No hardcoded tokens in source code
- Tool-based architecture prevents arbitrary chat-command execution
- Designed to avoid unintended destructive operations

---

## Technology Stack

- **Language:** Python  
- **AI Framework:** LangChain  
- **LLM Backend:** Groq API (LLama 3.1 – 8B Instant)  
- **GitHub Integration:** GitHub REST API  
- **Environment Management:** python-dotenv  
- **Interface:** Terminal / Chat  

---

##  Setup Instructions

### 1️⃣ Clone the Repository: 

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

### 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
GITHUB_TOKEN=your_github_classic_token_key_here
```

## ▶️ Running the Agent

```bash
python chat.py
```

---

##  Supported Chat Capabilities/Commands (Examples)

### 🔹 Repository Management:

```text
create a new repository named demo-project 
```

### 🔹 COMMIT and PUSH in repository:

```text
commit and push chat.py in repo Mayank251125/demo-project 
```

```text
commit and push app/tools.py in repo Mayank251125/demo-project 
```

### 🔹 Issue Management:

```text
create an issue named repo-issue in repo Mayank251125/demo-project with description high risk error
```

### README Generation:

```text
Generate a README.md file for my repo Mayank251125/demo-project
```

### 🔹 Audit/Analysing the repository: 

```text
Call audit_repo_tool with repo="Mayank251125/Stock_Market_Analysis_Tool"
```

---

##  Design Philosophy

* LLM used strictly for reasoning and decision making
* GitHub actions executed programmatically via tools
* Modular architecture for easy extensibility
* Secure token management using environment variables
* Model-agnostic design for future LLM flexibility
* Chat-based interaction for simplicity and clarity

---

##  Future Enhancements

* GitHub Webhook automation
* Pull request enhancement + Auto merge system
* Multi-repository orchestration
* LangGraph-based multi-agent coordination
* Web-based interface using FastAPI
* Advanced repository analytics

---

##  Author

**Mayank Joshi**
VIT Bhopal University

**Project Component:**
Project Component: Multi-Agent AI System — *GitHub Automation Agent*

---













