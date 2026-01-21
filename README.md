# Product Allocation Test Automation Framework

## Overview
This project is a Python-based automation framework designed to validate
product allocation logic used in retail systems.

The focus is on validating business rules, backend data consistency,
and API behavior rather than UI testing.

## Business Problem
Retailers allocate thousands of products to stores based on demand,
store capacity, and business constraints.

Incorrect allocation can lead to:
- Overstocking
- Lost sales
- Poor customer experience

This framework ensures allocation logic behaves correctly under
normal and edge-case conditions.

## Tech Stack
- Python
- Pytest
- Requests
- JSONSchema
- SQLite (backend validation)
- GitHub Actions (CI/CD)

## Test Coverage
- Allocation algorithm validation
- API happy-path testing
- Edge case testing
- Data-driven testing
- Backend persistence validation

## Project Structure
