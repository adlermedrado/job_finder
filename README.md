# **Job Finder 🕵️‍♂️**
🚀 *Automate job search & analysis using AI.*

Job Finder is an open-source project that **scrapes** job postings from various sources and **analyzes** them using AI based on user-defined criteria. It helps developers and job seekers find the best opportunities efficiently.

---

## **✨ Features**
✅ Scrapes job postings from multiple sources (e.g., GitHub, LinkedIn, etc.)  
✅ Uses **AI-powered analysis** to evaluate job descriptions  
✅ Filters jobs based on remote work, technologies, and contract types  
✅ Fully customizable and extensible  
✅ Supports **Django & Celery** for background job execution

---

## **📦 Installation**
### **Prerequisites**
- Python **3.12+**
- PostgreSQL **or** SQLite (for local testing)
- Docker & Docker Compose (optional, recommended)
- Redis (for Celery workers)

### **Clone the Repository**
```bash
git clone https://github.com/adlermedrado/job-finder.git
cd job-finder
```

### **Install Dependencies**

```
poetry install
```

### **Set Up the Database**
Apply migrations:
```
poetry run python manage.py runserver
```
