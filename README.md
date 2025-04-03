# pythondsap

## Setup

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies using `pyproject.toml`:
   ```bash
   pip install .
   ```

## Running Tests

To run the tests for the project, you can use the following command:

```bash
pytest tests/patterns/_1_pattern_sliding_window/_1_test_average_of_subarray_of_size_k.py
```

This command will execute the tests defined in the specified test file. You can also run all tests in the `tests` directory by using:

```bash
pytest tests/
```

## Note

All implementations are my own work, created for learning and practice purposes. The project uses `pyproject.toml` for dependency management instead of `requirements.txt`.
