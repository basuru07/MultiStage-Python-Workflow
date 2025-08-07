# 🐍 Python Flask App with Multistage Reusable DevOps Workflow

This project is a simple Python Flask application with a fully automated **CI pipeline using GitHub Actions**. The pipeline is **multistage and reusable**, performing linting, testing, and Docker builds in a modular way.

---

## 🚀 Features

- ✅ Simple REST API using Flask
- ✅ Unit tests using Pytest
- ✅ Linting with Flake8
- ✅ Dockerized application
- ✅ Multistage reusable GitHub Actions workflow
- ✅ Automatic CI on push and PR

---

## 📁 Project Structure

```
my-python-app/
├── app/
│   └── main.py  
├── tests/
│   └── test_main.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .flake8
├── .github/
│   └── workflows/
│       ├── _reusable-python.yml    # Reusable workflow
│       └── ci.yml                  # Main CI pipeline
```

---

## 🧪 Local Development

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the app
```bash
python app/main.py
```
Access: http://localhost:5000

### 3. Run tests
```bash
pytest
```

### 4. Lint the code
```bash
flake8 app/
```

---

## 🐳 Docker Usage

### Build the Docker image
```bash
docker build -t my-python-app .
```

### Run the container
```bash
docker run -p 5000:5000 my-python-app
```

---

## ⚙️ CI/CD with GitHub Actions

This project uses GitHub Actions with a reusable workflow file:

**Reusable Workflow: `_reusable-python.yml`**
- setup: Python & dependencies
- lint: Runs flake8
- test: Runs pytest
- docker-build: Builds Docker image

**Main Pipeline: `ci.yml`**
- Calls the reusable workflow with these inputs:
```yaml
with:
  run-tests: true
  run-lint: true
  build-docker: true
```
- Triggered on every push and pull request to main.

---

## ✅ Example API Response

```bash
curl http://localhost:5000/
```

```json
{"message": "Hello from Flask!"}
```

---

## 🧱 Requirements

- Python 3.11+
- Docker (optional)
- GitHub Actions enabled in your repo
