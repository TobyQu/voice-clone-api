# Contributing Guide

Thank you for your interest in the Voice Clone API project! We welcome various forms of contribution, including but not limited to code contributions, documentation improvements, issue reports, and feature requests.

## How to Contribute

### Reporting Issues

If you find a problem or have an improvement suggestion, please submit it using GitHub's Issues feature and include the following information:

1. A brief description of the issue
2. The environment in which the issue occurs (OS, Python version, etc.)
3. Steps to reproduce the issue
4. Expected behavior and actual behavior
5. Relevant error messages and logs

### Code Contribution

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Code Review

All submitted code will be reviewed. To speed up the review process:

- Ensure the code adheres to the project's coding style
- Add tests for new features
- Keep the scope of changes as small as possible
- Write clear commit messages

## Development Guide

### Setting Up Development Environment

```bash
# Clone the repository
git clone https://github.com/yourusername/voice-clone-api.git
cd voice-clone-api

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install -r requirements-dev.txt
```

### Code Style

We use [black](https://github.com/psf/black) and [isort](https://github.com/PyCQA/isort) for code formatting, and [flake8](https://github.com/PyCQA/flake8) for code checking:

```bash
# Format code
black app tests
isort app tests

# Check code
flake8 app tests
```

### Testing

When adding new features, please be sure to add corresponding tests. Run tests:

```bash
pytest tests/
```

All tests must pass for code submitted to the main branch.

## Documentation Contribution

Documentation is an important part of the project. If you find errors in the documentation or would like to improve it, feel free to submit a PR.

## Version Control and Release

We use [Semantic Versioning](https://semver.org/). If your contribution will change the API or add important features, please record these changes in CHANGELOG.md.

## Code of Conduct

Please refer to [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for our community code of conduct.

## License

By contributing code, you agree that your contribution will be released under the project's [LICENSE](LICENSE). 