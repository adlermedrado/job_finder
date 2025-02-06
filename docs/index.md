# **Job Finder 🕵️‍♂️**

## 🚀 Automate Job Search & Analysis Using AI

**Job Finder** is an open-source project that **scrapes job postings**  
from multiple sources and **analyzes them using AI** based on user-defined criteria.

It helps developers and job seekers **find the best job opportunities efficiently**.

⚠️ **Note:** This is a **personal project** in an **early-stage of development**.

---

## **✨ Features**
✅ Scrapes job postings from multiple sources (e.g., GitHub Issues, LinkedIn, etc.)  
✅ Uses **AI-powered analysis** to evaluate job descriptions  
✅ Filters jobs based on **remote work, technologies, and contract types**  
✅ **Fully customizable and extensible**  
✅ Uses **Django & Celery** for background job execution

---

## **📦 Installation**

### **Prerequisites**
- Python **3.12+**
- PostgreSQL **or** SQLite (for local testing)
- Docker & Docker Compose (optional, recommended)
- Redis (for Celery workers)

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/adlermedrado/job-finder.git
cd job-finder
```

2️⃣ Install Dependencies

Using [poetry](https://python-poetry.org/):
```bash
poetry install
```

Or using pip (requires a virtual environment):
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3️⃣ Set Up the Database

Apply migrations:
```bash
poetry run python manage.py migrate
```

Or using venv:
```bash
python manage.py migrate
```

5️⃣ Setup environment variables
To run locally, rename [.env.sample](.env.sample) to **.env** and fill the required values,
or load the environment variables directly into your shell.
Setting up the .env file you can load them as below:

After setting up .env, load the variables as follows:
```bash
# Using Poetry
poetry shell
source load_env.sh  # For Bash/Zsh
source load_env.fish  # If using Fish shell

# Using venv
source load_env.sh  # For Bash/Zsh
source load_env.fish  # If using Fish shell
```

4️⃣ Run the Project

Start the Django server:
```bash
poetry run python manage.py runserver
```

Or using venv:
```bash
source load_env.sh (or if using fish: load_env.fish)
&& python manage.py runserver
```

Start celery workers:

```bash 
celery -A job_finder worker --loglevel=info
```

Start celery beat:
```beat
celery -A job_finder beat --loglevel=info
```

(Optional) Run Redis & PostgreSQL via Docker:
```bash
docker-compose up -d
```

### 👨‍💻 Contributing

Contributions are welcome! To contribute:
1.	**Fork** the repo and create a **new branch** (git checkout -b feature-name)
2. Make your changes and test them
3. **Run tests** with `pytest`
4. **Submit a pull request (PR)**

### 📢 Support

If you find this project useful, ⭐ star the repository and share it with your network!

### 📅 Roadmap
✔ **Supported job sources:** Currently, the project scrapes job postings from **open-source repositories using GitHub Issues**
🚀 **Planned features:**
*	Add support for **more job sources** (LinkedIn, Indeed, etc.)
*	Improve **AI job matching accuracy** enabling **job analysis criteria configuration** via Django Admin
*	Add support for **more AI providers** (currently it matches only remote positions, for example)
*	Implement a **web dashboard** for job management
*	Increase **test coverage**

### 📜 License
This project is licensed under the MIT License. 

See [LICENSE](LICENSE) for details.


### 🔄 Basic Flow
```mermaid
graph TD;
A[Start] -->|Scrape job postings| B[Workers Job Scraper]
B -->|Save to database| C[(PostgreSQL)]
C -->|Sanitize Data using NLP| D[(spaCy)]
D -->|Analyze jobs using AI| E[OpenAI API]
E -->|Store analysis results| F[(Database)]
F -->|Display results| G[User Interface]
G -->|Done| H[End]

```