# GoRest API Testing Project

This project is a suite of tests for the GoRest API, written in Python using `pytest`. The tests cover basic CRUD operations (Create, Read, Update, Delete) on users.

 Visit Website : [GoRest API](#https://gorest.co.in/)

## Table of Contents

- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Running the Tests](#running-the-tests)
- [Test Details](#test-details)
- [Generating Test Reports](#generating-test-reports)
- [Contributing](#contributing)
- [License](#license)

## Project Structure

```
GoRestAPITesting/
├── venv/
├── api_tests/
│   ├── __init__.py
│   ├── test_gorest_api.py
│   └── conftest.py
├── utils/
│   ├── __init__.py
│   ├── helper_functions.py
│   └── config.py
├── reports/
│   ├── html/
│   └── logs/
├── .env
├── requirements.txt
├── pytest.ini
└── README.md
```

- `venv/`: Virtual environment directory.
- `api_tests/`: Directory containing test files.
- `utils/`: Directory containing utility modules.
- `reports/`: Directory for storing test reports.
- `.env`: Environment variables file.
- `requirements.txt`: List of Python dependencies.
- `pytest.ini`: Pytest configuration file.
- `README.md`: This file.

## Prerequisites

- Python 3.7 or higher
- `pip` (Python package installer)
- `virtualenv` (optional but recommended)

## Setup

1. **Clone the repository**:

    ```bash
    git clone https://github.com/iam-aniruddha/GoRestAPITesting.git
    cd GoRestAPITesting
    ```

2. **Create and activate a virtual environment**:

    - **On Windows**:

        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

    - **On macOS/Linux**:

        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:

    Create a `.env` file in the root directory with the following content:

    ```plaintext
    AUTH_TOKEN=Bearer your_auth_token_here
    ```

## Running the Tests

To run the tests, use the following command:

```bash
pytest
```

This will run all the tests in the `api_tests/` directory.

## Test Details

### test_gorest_api.py

- `test_get_users()`: Tests the GET /public/v2/users/ endpoint.
- `test_create_user()`: Tests the POST /public/v2/users/ endpoint.
- `test_update_user()`: Tests the PUT /public/v2/users/{id} endpoint.
- `test_delete_user()`: Tests the DELETE /public/v2/users/{id} endpoint.

### conftest.py

- Contains fixtures for setting up and tearing down test data.

### helper_functions.py

- Utility functions for making API requests and generating random data.

### config.py

- Configuration file for storing base URL and reading environment variables.

## Generating Test Reports

To generate an HTML report, ensure the `pytest-html` plugin is installed and run:

```bash
pytest --html=reports/html/report.html --self-contained-html
```

The report will be generated in the `reports/html/` directory.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature/your-feature-name`).
6. Open a pull request.

Please ensure your code follows the existing style and includes relevant tests.


---

This README should provide a comprehensive guide to understanding, setting up, and contributing to your GoRest API testing project. It includes all necessary details and ensures that anyone can start working on the project with minimal setup.