# Part B

This story test suite uses Pytest for testing, and specifically incorporates the `pytest-random-order` plugin to randomize the order of test execution and `pytest-bdd` to execute gherkin scripts. Below are the instructions for installing Pytest and running tests with different configurations.

## Installing Pytest, Pytest-BDD Pytest-Random-Order

To install Pytest, `pytest-bdd` and `pytest-random-order`, run the following command:

```bash
pip install pytest pytest-bdd pytest-random-order
```

## To run tests

Run

```bash
pytest --random-order
```

## Project Structure

- part_b
  - **categories**: Directory containing test files for `categories`
  - **projects**: Directory containing test files for `projects`
  - **todos**: Directory containing test files for `todos`
  - **resources**: Directory containing the feature files for `categories`, `projects`, and `todos`
  - **utils_b**: Directory containing test data, error codes, and helper functions
  - `conftest.py`: File containing step definitions and fixtures used throughout the test suite
  - `README.md`: Main README file with instructions.
