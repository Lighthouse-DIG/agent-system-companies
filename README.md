# Agent-system-companies

A system to query company information from various data sources using Python.  
This project uses [`uv`](https://github.com/astral-sh/uv) for fast environment and dependency management.

---

## 📁 Project Structure

- `companies.py`: Main script containing the business logic.
- `.env`: Environment variables file with your API key.
- `pyproject.toml`: Defines the project and its dependencies.
- `.venv/`: Local virtual environment (should not be committed to version control).

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your_username/agent-system-companies.git
cd agent-system-companies
```

### 2. Initialize the Project & Create Virtual Environment
```bash
uv init agent-system-companies
cd agent-system-companies
uv venv
```

### 3. Activate the Virtual Environment
💻 macOS & Linux


```bash 
source .venv/bin/activate
 ```
🪟 Windows

```bash 
.venv\Scripts\activate
```

### 4. Install Project Dependencies
Run the following command to add the necessary packages:

```bash 
uv add httpx>=0.28.1 mcp[cli]>=1.6.0 pandas>=2.2.3 python-dotenv>=1.1.0 requests>=2.32.3
``` 
### 5. Obtain Your API Key
 - Visit the official Alpha Vantage website to get your free API key: https://www.alphavantage.co/
 - Click on "GET FREE API KEY."

### 6. Set Up Environment Variables
Create a .env file in the root of the project with your Alpha Vantage API key:

```bash 
env ALPHAVANTAGE_API_KEY=your_api_key 
```