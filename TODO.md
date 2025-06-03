# TODO: Improvements & Best Practices for Weather App

This checklist is based on code review and best practices for Python FastAPI projects deployed on Azure.

---

## 1. Code Quality & Structure
- [ ] Refactor API logic, data models, and utility functions into separate modules.
- [ ] Add/complete type annotations for all functions and methods.
- [ ] Add robust error handling for all external API calls.
- [ ] Use `logging` throughout the application to capture errors and key events.

## 2. Containerization & Deployment
- [ ] Add a `.dockerignore` file to exclude unnecessary files (e.g., `.venv`).
- [ ] Use multi-stage Docker builds to minimize image size.
- [ ] Move external API URLs and keys to environment variables.

## 3. Azure Integration
- [ ] Implement Azure Function for weather threshold alerts.
- [ ] Integrate Azure Function with main app (e.g., webhook, queue, or timer).
- [ ] Add Application Insights SDK for FastAPI and Azure Function.
- [ ] Track custom metrics and errors in Azure Monitor.
- [ ] Store secrets (API keys, etc.) in Azure Key Vault.

## 4. CI/CD Pipeline
- [ ] Add automated tests (e.g., with `pytest`) for endpoints and error cases.
- [ ] Integrate tests into CI pipeline (build should fail if tests fail).
- [ ] Add linting (`flake8`) and formatting (`black`) checks to CI.
- [ ] Ensure pipeline builds, tests, and pushes Docker image to Azure Container Registry.
- [ ] Use deployment slots for zero-downtime deploys.

## 5. API & Functionality
- [ ] Implement rate limiting middleware.
- [ ] Link to FastAPI docs (`/docs`) in README.
- [ ] Add input validation for city names and edge cases.

## 6. Documentation
- [ ] Add an app architecture diagram to README.
- [ ] Add CI/CD status badges to README.
- [ ] Document Azure setup steps in README.
- [ ] Add troubleshooting and FAQ sections to README.
- [ ] Expand usage examples with sample responses.

## 7. General Improvements
- [ ] Ensure no sensitive info is exposed in logs or errors.
- [ ] Add authentication (OAuth, API keys) if app will be public.
- [ ] Use Azure’s scaling features and keep app stateless.

---

Check off each item as you complete it!