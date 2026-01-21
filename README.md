# Product Allocation Test Automation Framework

## Overview
This project is a Python-based automation framework designed to validate
product allocation logic used in large-scale retail systems.

Retailers like grocery chains allocate thousands of products to stores
based on demand, store capacity, and business constraints.
Even small errors in allocation logic can result in overstocking,
lost sales, or poor customer experience.

This framework focuses on validating allocation **correctness, edge cases,
data integrity, and backend persistence** rather than UI behavior.

---

## Business Problem
In retail assortment and set planning systems:

- Products must be allocated accurately across many stores
- Allocation logic often involves complex formulas and constraints
- Errors may not be visible in UI but surface later as data issues

This project simulates a simplified allocation system and validates it
across multiple layers to ensure correctness and reliability.

---

## Test Strategy (Manual → Automation)
The framework follows a realistic QA approach:

1. **Manual Test Thinking**
   - Identify happy paths and high-risk edge cases
   - Understand business rules before automating

2. **Algorithm Validation**
   - Validate allocation rules independently of API responses

3. **API-Level Automation**
   - Validate request/response behavior
   - Ensure business rules are enforced

4. **Backend Validation**
   - Confirm allocation results are persisted correctly in the database

5. **Data-Driven Testing**
   - Scale validation across multiple products and stores using JSON data

---

## Architecture Overview

AllocationAPI
│
├── Business Rule Validator
│
├── SQLite Backend (Persistence)
│
└── Centralized Logging


---

## Tech Stack
- Python 3
- Pytest
- SQLite (backend validation)
- JSON (data-driven tests)
- Centralized logging
- GitHub (version control)

---

## Project Structure

src/
├── api/ # Allocation logic and API simulation
├── validators/ # Business rule validation
├── db/ # Database client and persistence
tests/
├── api/ # Pytest automation tests
├── data/ # JSON-based test data
config/ # Environment and path configuration
utils/ # Logging utilities


---

## Test Coverage
- Happy-path allocation validation
- Edge cases (zero demand, demand > capacity)
- Data-driven testing across multiple SKUs
- Backend persistence validation
- Logging and observability

---

## How to Run the Tests

```bash
# Activate virtual environment
venv\Scripts\activate

# Run all tests
pytest

An HTML test report is generated after execution.

Why This Framework Is Different

Focuses on algorithm and data correctness, not UI automation

Validates multiple layers (logic, API, backend)

Designed to scale to thousands of products via data-driven testing

Uses clean separation of concerns for maintainability

Future Enhancements

Negative and fault-injection testing

Performance validation for large data sets

CI/CD integration

Environment-based configuration

Enhanced reporting and metrics

Author

Sunil Sodhi
Senior QA / SDET / Automation Engineer

