# Learn through Open Source, Job API (FastAPI)

A community-driven open-source REST API built with **FastAPI** to help developers learn backend development, Git/GitHub collaboration, and real-world software engineering practices.

This project is part of the **Fata Open Source Project**, where participants contribute to a shared codebase while learning how professional teams build and maintain software.
Main aim is promote learning through **Fata** while actually practicing learnt concepts, into a real project.

---

## Project Goals

The purpose of this project is to help developers:

- Learn FastAPI and modern backend development.
- Learn Python programming concepts
- Understand REST API design.
- Practice Git and GitHub workflows.
- Learn how to collaborate on an open-source project.
- Gain experience working on an existing codebase.
- Build a portfolio through meaningful contributions.

---

## Tech Stack

- FastAPI
- SQLAlchemy
- SQLite (Development)
- PostgreSQL (Future)
- Alembic
- Pydantic
- Pytest

---

## Project Features

The API will include:

- User Authentication
- Job Listings
- Companies
- Job Applications
- Search & Filtering
- API Documentation
- Unit Tests

---

## Getting Started

### 1. Fork the repository

Click **Fork** at the top-right of this repository.

---

### 2. Clone your fork

```bash
git clone https://github.com/FATAschool/JobAPI.git
```
to avoid push authentication everytime i recommend this method
    1. Generate a fine grained ssh token key
    2. include it in you clone url like so httsp://graintoken@github.com...., 
        this automatically authenticates you to work on the repo.
```bash
git clone https://graintoken@github.com/FATAschool/JobAPI.git
```

---

### 3. Navigate into the project

```bash
cd JobAPI
```

---

### 4. Create a virtual environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 5. Install dependencies

```bash
pip install -r requirements.dev.txt
```

---

### 6. Run the application

```bash
uvicorn app.main:app --reload
```
or
```bash
python3 run.py
```

---

## Contribution Workflow

We welcome contributions from everyone.

Please follow the workflow below.

1. Fork the repository.
2. Pull from remote, git pull.
3. Branch names are present on the feature branch, a branch name presents the app/module you are working on
    e.g(feature/FATA01-emails), that branch is for emails workflow for the jobApi.
4. Complete one assigned issue. Issues will be assigned to individuals
5. Commit your changes with a meaningful commit message.
6. Push your branch.
7. Open a Pull Request.
8. Wait for review before merging.

---

## Branch Naming

Use descriptive branch names, use the prefix FATA01-"branch name".

Examples

```
dev/FATA01-user-authentication
dev/FATA01-jobs
feature/FATA01-companies
fix/login-validation
docs/update-readme
test/job-endpoints
```

---

## Commit Message Examples

Good examples

```
feat: add job creation endpoint

fix: validate email during registration

docs: update installation guide

test: add authentication tests
```

Avoid

```
update

changes

fixed

work
```

---

## Pull Requests

Every Pull Request should:

- Solve one issue.
- Be focused on a single feature or fix.
- Include a clear description of what changed.
- Pass all tests (where applicable).

---

# Rules

## Do not push directly to `main or master` branch

No contributor is allowed to push directly to the `main` (or `master`) branch.

All changes **must** go through a Pull Request and be reviewed by a project maintainer before being merged.

---

## Work on Assigned Issues/Tasks

Please work only on issues assigned to you. Tasks will be available on trello board

If you want to work on a new feature, open an issue first or ask a maintainer to assign it to you.

---

## Keep Pull Requests Small

Small Pull Requests are easier to review and merge.

Avoid combining multiple unrelated features into one Pull Request.

---

## Follow the Project Structure

Before creating new folders or changing the architecture, discuss the change with the maintainers.

Consistency helps everyone contribute more effectively.

---

## Write Clean Code

Please follow these principles:

- Write readable code.
- Use meaningful variable names.
- Keep functions small.
- Remove unused code.
- Follow Python style guidelines (PEP 8).

---

## Respect Code Reviews

Code reviews are part of the learning process.

Feedback is meant to improve the project and help everyone grow.

---

## Need Help?

If you're stuck:

- Ask questions in the community, whatsapp or discord server
- Open a discussion.
- Reach out to a project maintainer.

There are no bad questions—we're all here to learn.

---

## Code of Conduct

We are committed to providing a welcoming and respectful environment for everyone.

Please:

- Be respectful.
- Be patient.
- Help others learn.
- Give constructive feedback.
- Respect different experience levels.

Harassment, discrimination, or disrespectful behavior will not be tolerated.

---

## License

This project is released under the MIT License.

---

## Acknowledgements

Thank you to every contributor who takes the time to learn, collaborate, and improve this project.

Every issue solved, bug fixed, documentation update, and line of code helps make this project better.

Happy coding! 🚀