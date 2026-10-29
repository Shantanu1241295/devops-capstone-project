# devops-capstone-project



[![CI Build](https://github.com/Shantanu1241295/devops-capstone-project/actions/workflows/ci-build.yaml/badge.svg)](https://github.com/Shantanu1241295/devops-capstone-project/actions/workflows/ci-build.yaml)
License: [MIT](LICENSE)

## Project Overview
This repository contains the microservice application and DevOps pipeline developed for the DevOps Capstone Project. The application is a Flask-based Accounts REST API service equipped with database persistence, security hardening (HTTP headers and CORS policies), containerization via Docker, and continuous integration/continuous deployment (CI/CD) workflows using GitHub Actions and Tekton.

---

## Features & Implementation
- **RESTful API**: Full CRUD operations (Create, Read, Update, Delete, List) for managing customer accounts.
- **Security & Compliance**: Integrated security headers via Flask-Talisman and configured Cross-Origin Resource Sharing (CORS).
- **Continuous Integration**: Automated linting (`flake8`) and unit test execution (`nosetests`) running within isolated containers via GitHub Actions.
- **Containerization**: Optimized multi-stage `Dockerfile` running under a non-root security context.
- **Orchestration & Deployment**: Kubernetes manifests and Tekton pipeline configurations for automated build, push, and deployment workflows.

---

## Project Structure
```text
├── .github/
│   └── workflows/
│       └── ci-build.yaml       # GitHub Actions CI workflow configuration
├── service/
│   ├── __init__.py             # Flask application & security headers initialization
│   ├── config.py               # Application configuration settings
│   ├── models.py               # Database models and business logic
│   ├── routes.py               # REST API endpoints
│   └── common/                 # Logging, error handlers, and status codes
├── tests/
│   └── test_*.py               # Unit and integration test suites
├── Dockerfile                  # Secure container definition
├── requirements.txt            # Python dependencies
├── setup.cfg                   # Tool configurations (flake8, nose, pylint)
└── README.md
