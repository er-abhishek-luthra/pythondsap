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

## Setup with Conda

### 1. Install Conda

If you haven't already installed Conda, you can choose between two distributions:

- **Miniconda**: A minimal installer for Conda, which includes only Conda and its dependencies. You can download it from [Miniconda](https://docs.conda.io/en/latest/miniconda.html).
- **Anaconda**: A larger distribution that includes Conda and many pre-installed scientific packages. You can download it from [Anaconda](https://www.anaconda.com/products/distribution).

### 2. Create a Conda Environment

1. **Navigate to Your Project Directory**:
   Open your terminal and change to your project directory:
   ```bash
   cd /path/to/your/project
   ```

2. **Create the Environment from `environment.yml`**:
   Use the following command to create a Conda environment from the `environment.yml` file:
   ```bash
   conda env create -f environment.yml
   ```

3. **Activate the Environment**:
   After the environment is created, activate it using:
   ```bash
   conda activate myenv  # Replace 'myenv' with the name specified in your environment.yml
   ```

### 3. Basic Conda Commands

Here are some basic Conda commands that you might find useful:

- **List All Conda Environments**:
  ```bash
  conda env list
  ```

- **Activate an Environment**:
  ```bash
  conda activate myenv
  ```

- **Deactivate the Current Environment**:
  ```bash
  conda deactivate
  ```

- **Remove an Environment**:
  ```bash
  conda env remove --name myenv
  ```

- **Install a Package**:
  ```bash
  conda install package_name
  ```

- **Update a Package**:
  ```bash
  conda update package_name
  ```

- **Export the Current Environment to a YAML File**:
  ```bash
  conda env export > environment.yml
  ```

### 4. Running Tests

To run the tests for the project, you can use the following command:

```bash
pytest tests/patterns/_1_pattern_sliding_window/_1_average_of_subarray_of_size_k_test.py
```

This command will execute the tests defined in the specified test file. You can also run all tests in the `tests` directory by using:

```bash
pytest tests/
```

## Note

All implementations are my own work, created for learning and practice purposes. The project uses `pyproject.toml` for dependency management instead of `requirements.txt`.
