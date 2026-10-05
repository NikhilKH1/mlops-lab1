# MLOps Lab 1

This project demonstrates basic MLOps practices using Python, Pytest, Unittest, and GitHub Actions.

## Project Structure

```text
.
├── src/
│   └── calculator.py
├── test/
│   ├── test_pytest.py
│   └── test_unittest.py
├── .github/
│   └── workflows/
│       ├── pytest_action.yml
│       └── unittest_action.yml
├──data/
    └── __init__.py
├── requirements.txt
└── README.md
```

## Calculator Functions

The original calculator was extended with additional operations:

- `fun1` – Addition
- `fun2` – Subtraction
- `fun3` – Multiplication
- `fun4` – Add three numbers
- `fun5` – Division
- `fun6` – Power
- `fun7` – Modulus
- `fun8` – Average
- `fun9` – Maximum
- `fun10` – Minimum

Input validation and error handling were also added for invalid inputs and divide-by-zero cases.

## Testing

The project uses both Pytest and Unittest.

Run Pytest:

```bash
pytest test/test_pytest.py -v
```

Run Unittest:

```bash
python -m unittest test.test_unittest -v
```

The tests cover normal calculations, negative values, zero values, invalid inputs, and divide-by-zero cases.

## GitHub Actions

Two CI workflows are included:

- `pytest_action.yml`
- `unittest_action.yml`

The workflows automatically:

1. Check out the repository
2. Set up Python
3. Install dependencies
4. Run automated tests
5. Generate test reports
6. Generate code coverage reports
7. Upload test and coverage reports as GitHub Actions artifacts
8. Report success or failure

## Changes Made

To extend the original lab, I added:

- Six new calculator operations
- Additional Pytest test cases
- Additional Unittest test cases
- Input validation and error handling
- Pytest code coverage using `pytest-cov`
- Unittest code coverage using `coverage`
- HTML coverage report generation
- GitHub Actions artifact uploads for coverage reports

## Installation

```bash
python -m venv lab_01
source lab_01/bin/activate
pip install -r requirements.txt
```

## Git Workflow

```bash
git add .
git commit -m "Extend calculator and CI pipeline"
git push origin main
```

Pushing to `main` triggers the configured GitHub Actions workflows.
