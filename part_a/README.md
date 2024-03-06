# Part A

This unit test suite uses Pytest for testing, and specifically incorporates the `pytest-random-order` plugin to randomize the order of test execution. Below are the instructions for installing Pytest and running tests with different configurations.

## Installing Pytest and Pytest-Random-Order

To install Pytest and the `pytest-random-order` plugin, run the following command:

```bash
pip install pytest pytest-random-order
```

## To run tests

### 1. Test API reactivity

```bash
pytest -vv -k "run_first"
```

### 2. Randomized Tests

```bash
pytest --random-order -vv -k "not run_first" -k "not run_last"
```

### 3. Test shutdown endpoint

```bash
pytest -vv -k "run_last"
```

## Project Structure

- part_1
  - **categories**: Directory containing test files for `categories`
  - **projects**: Directory containing test files for `projects`
  - **todos**: Directory containing test files for `todos`
  - **utils**: Directory containing test data, error codes, and helper functions
  - `test_app.py`: File containing tests for API reactivity and shutdown endpoint
  - `pytest.ini`: Configuration file with markers to control test execution
  - `README.md`: Main README file with instructions.
