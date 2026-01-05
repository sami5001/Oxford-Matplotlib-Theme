# Contributing to Oxford Matplotlib Theme

Thank you for your interest in contributing to the Oxford Matplotlib Theme!

## Development Setup

```bash
# Clone the repository
git clone https://github.com/sami5001/oxford-matplotlib-theme.git
cd oxford-matplotlib-theme

# Install in development mode with all dependencies
pip install -e ".[all]"
```

## Code Style

- Follow [PEP 8](https://peps.python.org/pep-0008/) guidelines
- Use [Black](https://github.com/psf/black) for code formatting (line-length=100)
- Add type hints to all public functions
- Write [NumPy-style docstrings](https://numpydoc.readthedocs.io/en/latest/format.html)

## Running Tests

```bash
# Run all tests
pytest -v

# Run with coverage
pytest --cov=oxford_matplotlib_theme --cov-report=term-missing

# Run a specific test file
pytest tests/test_colors.py -v
```

## Code Quality Checks

```bash
# Format code
black oxford_matplotlib_theme tests

# Lint
flake8 oxford_matplotlib_theme tests

# Type checking
mypy oxford_matplotlib_theme
```

## Pull Request Process

1. Fork the repository and create a feature branch
2. Make your changes with appropriate tests
3. Ensure all tests pass: `pytest -v`
4. Ensure code is formatted: `black --check .`
5. Update documentation if needed
6. Submit a pull request with a clear description

## Adding New Colors

When adding new Oxford colors:
1. Verify the color is from official [Oxford Brand Guidelines](https://communications.admin.ox.ac.uk/communications-resources/visual-identity/identity-guidelines/colours)
2. Add to `OxfordColors` class in `colors.py` with Pantone code comment
3. Add to `OXFORD_COLORS` dictionary
4. Add tests in `test_colors.py`

## Adding New Presets

When adding new presets:
1. Add configuration to `PRESETS` dict in `presets.py`
2. Include description, style_base, color_cycle, and font_scale
3. Add tests in `test_presets.py`

## Questions?

For questions about Oxford brand guidelines, contact the [Oxford Communications Office](https://communications.admin.ox.ac.uk/).

For package-related questions, open an issue on GitHub.
