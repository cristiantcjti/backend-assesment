
# BACKEND ASSESMENT

<p align="center">
  <img alt="Python 12.6.6" src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" />
  <img alt="Django 5.1.1" src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green" />
  <img alt="Django Ninja 1.3.0" src="https://img.shields.io/badge/ninja-092E20?style=for-the-badge&logo=django&logoColor=green" />
  <img alt="Postgres" src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white">
  <img alt="Docker" src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white">
</p>


# Summary

1. **[Introduction](#introduction-architecture-haiku)**
2. **[Prerequisites](#prerequisites)**
3. **[Project Architecture](#project-architecture)**
   1. **[Code Design](#code-design)**
   2. **[Project Structure](#project-structure)**
4. **[Standards Used](#standards-used)**
5. **[Database](#database)**
   1. **[Django ORM](#Django-orm)**
6. **[Coverage](#coverage)**
7. **[Starting the Application](#starting-the-application)**
   1. **[Cloning the Repository](#cloning-the-repository)**
   2. **[Running the Application Locally with Docker](#running-the-application-locally-with-docker)**
   3. **[Running the Application Locally](#running-the-application-locally)**
   4. **[Creating and Running Migrations](#creating-and-running-migrations)**
   5. **[Adding New Packages to the Project](#adding-new-packages-to-the-project)**
8. **[Pull Request](#pull-request)**
9. **[Notion](#notion)**

---

## Introduction

**To Be Determined (TBD)**

#### Business Objectives
To offer a secure and sustainable service that enables management to the project.

#### Constraints
**TBD**

#### Prioritized Quality Attributes:
- **Integration** > **Availability** > **Security** > **Usability**

#### Key Application Components:
- Service: `backend-assesment`.
- Database: `backend-assesment-database`.

#### Component Relationships:
The `backend-assesment` service (API) provides BACKs management endpoints and interacts with the `backend-assesment-database` database to perform REST actions:
- Create
- Read
- Update
- Delete

---

## Prerequisites
- Make
- [pyenv](https://github.com/pyenv/pyenv)
- [docker](https://docs.docker.com/desktop/install/linux-install/)
- [docker-compose](https://docs.docker.com/compose/install/)

---

## Project Architecture

*TBD*

### Code Design
**TBD**

### Project Structure

```plaintext
backend-assesment/
├── etc/
├── src/
├── .dockerignore
├── .env
├── .gitignore
├── .pre-commit-config.yaml
├── docker-compose.env
├── docker-compose.yml
├── Dockerfile
├── Makefile
├── manage.py
├── poetry.lock
├── pyproject.toml
├── README.md
└── setup.cfg
```

---

## Standards Used

**TBD**

Branch naming conventions adhere to the project's declarative standard based on the purpose of changes, beginning with:

- `feat/BACK-0001`
- `refactor/BACK-0002`
- `bugfix/BACK-0003`
- `hotfix/BACK-0004`

Commit naming conventions follow these guidelines:
[Reference 1](https://www.conventionalcommits.org/en/v1.0.0/)
[Reference 2](https://graphite.dev/guides/git-commit-message-best-practices)

Examples:
- `feat[BACKS-0001]`: Introduces a new feature.
- `fix[BACKS-0002]`: Fixes an issue.
- `docs[BACKS-0003]`: Documentation-only changes.
- `style[BACKS-0004]`: Code changes that do not affect functionality (e.g., formatting, removing white spaces).
- `refactor[BACKS-0005]`: A change that neither fixes a bug nor adds a feature.
- `perf[BACKS-0006]`: Performance improvements.
- `test[BACKS-0007]`: Adds or fixes tests.
- `chore[BACKS-0008]`: Build process changes or auxiliary tool additions.

---

## Database

The primary database for the `backend-assesment` service is relational, using MSSQL Server as the DBMS.

### Django ORM

Django ORM
Together with PostgreSQL, we use Django's ORM to create migrations in our database.

To create a migration, we follow the naming convention provided by Django:

Version: Four-digit numerical sequence.
Action: The action being performed on the table.
Model: The name of the model/table on which the action is executed.
Field: The field undergoing the action.
Suffix: .py
Example of a migration file: 0005_add_user_name.py

For more information, we can refer to the official Django Migrations documentation.

---
## Coverage

Excellence is a priority in the `backend-assesment` development process. For this reason, a high standard for test coverage is maintained. The project's acceptance threshold is **80%**, but the goal is always as close to **100%** as possible. The more meaningful the tests, the lower the risk of future issues.

---

## Starting the Application

Starting the application is a straightforward process. Follow the steps below to get the project running at 100%.

### Cloning the Repository

Before cloning the project, ensure the following dependencies are installed:

**TBD**

Once everything is configured in your development environment, clone the repository with the command:

```bash
git clone "project path"
```

---

## How to launch the project?

Create an environment variables file.
```
cp etc/env-sample .env
```

Create containers.
```
make up
```

## How to set up the local development environment?
Install the Python version and create a virtual environment.
```
make create-venv
```

Install packages.
```
make setup-dev
```

Enable pre-commit.
```
pre-commit install
```

To update the worker code, it is necessary to restart them.
```
make restart
```

## How to create and run migrations?
After making changes to the model, run the following command to create the migration file:
```
make migrations
```

With the file created, run the following command to execute the pending migrations:
```
make migrate
```

## How to add new packages to the project?
This project uses **pipenv** as the package manager. To add new packages, use the following commands:
```
pipenv install PACKAGE_NAME==VERSION
```
After adding, it will be necessary to rebuild the containers: ``make build``

Development-only packages should be added as follows:
```
pipenv install --dev PACKAGE_NAME==VERSION
```


---

## Pull Request

**TBD**

---

## Documentation

**TBD**







