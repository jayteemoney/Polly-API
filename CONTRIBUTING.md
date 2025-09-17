# Contributing Guidelines

When contributing to this project, please follow these guidelines:

## Code Style
- Follow PEP 8 for Python code.
- Use meaningful names for variables and functions.

## Utility Functions
- For any reusable logic, especially for database queries that are used in multiple places, create a utility function in `api/utils.py` to avoid code duplication.
- Keep utility functions small and focused on a single task.

## Commits
- Write clear and concise commit messages.
- Each commit should represent a single logical change.