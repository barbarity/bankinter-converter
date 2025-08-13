# Release Guide

This guide explains how to release new versions of bankinter-converter to PyPI.

## Prerequisites

1. **PyPI Account**: Create an account at [PyPI](https://pypi.org/account/register/)
2. **API Token**: Generate an API token in your PyPI account settings
3. **GitHub Secret**: Add your PyPI API token as a GitHub secret named `PYPI_API_TOKEN`

## Release Process

### 1. Prepare the Release

```bash
# Update version using the release script
python scripts/release.py 0.2.0

# Or manually update version in pyproject.toml
# version = "0.2.0"
```

### 2. Test Locally

```bash
# Install dependencies
uv sync

# Run tests
uv run pytest

# Check code quality
uv run ruff check .

# Test the build
uv run python -m build
```

### 3. Commit and Tag

```bash
# Commit changes
git add .
git commit -m "Release 0.2.0"

# Create and push tag
git tag v0.2.0
git push origin v0.2.0
```

### 4. Automated Release

Once you push the tag, GitHub Actions will automatically:

1. Run all tests
2. Check code quality
3. Build the package
4. Publish to PyPI
5. Create a GitHub release

## Installation Methods

After publishing to PyPI, users can install your package using:

### uvx (Recommended)
```bash
# Run directly
uvx bankinter-converter --help

# Install globally
uvx install bankinter-converter
```

### uv
```bash
# Install globally
uv tool install bankinter-converter
```

### pip
```bash
pip install bankinter-converter
```

## Version Management

- **Patch releases** (0.1.1): Bug fixes
- **Minor releases** (0.2.0): New features, backward compatible
- **Major releases** (1.0.0): Breaking changes

## Troubleshooting

### PyPI Publishing Fails
- Check that `PYPI_API_TOKEN` secret is set in GitHub
- Verify the package name is available on PyPI
- Ensure all required fields are in `pyproject.toml`

### Tests Fail
- Run tests locally before tagging
- Check that all dependencies are properly specified
- Verify Python version compatibility

### Build Fails
- Ensure `pyproject.toml` is properly formatted
- Check that all required fields are present
- Verify the package structure is correct
