# Contributing to VetDataHub

Thank you for your interest in contributing to **VetDataHub**! We appreciate your help in making our project better. To maintain a smooth collaboration process, please follow the guidelines outlined below.

## How to Contribute

### 1. Fork the Repository

Start by forking the repository to your own GitHub account. This allows you to make changes freely without affecting the original project.

### 2. Clone Your Fork

Clone your forked repository to your local machine:

```bash
git clone https://github.com/yourusername/vetdatahub.git
cd vetdatahub
```

### 3. Create a New Branch

Create a new branch for your feature or bug fix. It's essential to keep your changes organized and separate from the main codebase.

```bash
git checkout -b your-feature-branch
```

### 4. Set Up the Development Environment

To maintain code quality, we use Black for code formatting and Flake8 for linting. You will need to set them up before contributing.
Install Black and Flake8

First, make sure you have the required dependencies:

```bash

pip install -r requirements.txt
```

### 5. Make Your Changes

Implement your changes and make sure to follow the project's coding style and standards.

- Ensure your code is clean, well-documented, and follows Python's PEP 8 style guide.
- Use Black to format your code:

  ```bash

    black .
    ```

- Use Flake8 to lint your code and catch any style violations:

  ```bash

    flake8 .
    ```

- Write clear, concise commit messages.

- Ensure your code is well-documented.

- If applicable, add tests for your changes to ensure they work as intended. Make sure all tests pass before submitting your contribution.

### 6. Commit Your Changes

When you're satisfied with your changes, commit them with a clear and descriptive commit message. 

```bash
git add .
git commit -m "Add a brief description of your changes"
```

### 7. Push to Your Branch

Push your changes to your forked repository:

```bash
git push origin your-feature-branch
```

### 6. Open a Pull Request

Go to the original **VetDataHub** repository and open a pull request (PR). Include a detailed description of your changes and reference any related issues.

### 7. Participate in the Review Process

Once your PR is submitted, the maintainers will review your changes. Be open to feedback and make necessary adjustments as requested.

## Reporting Issues

If you encounter a bug or have a feature request, please open an issue in the repository. Include the following information:

- A clear and descriptive title.
- A detailed description of the issue or feature.
- Steps to reproduce the issue (if applicable).
- Any relevant screenshots or code snippets.
