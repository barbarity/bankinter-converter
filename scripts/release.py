#!/usr/bin/env python3
"""Script to help with releasing new versions."""

import re
import sys
from pathlib import Path


def update_version(version: str) -> None:
    """Update version in pyproject.toml."""
    pyproject_path = Path("pyproject.toml")
    content = pyproject_path.read_text()

    # Update version
    content = re.sub(r'version = "[\d.]+"', f'version = "{version}"', content)

    pyproject_path.write_text(content)
    print(f"Updated version to {version} in pyproject.toml")


def main():
    """Main function."""
    if len(sys.argv) != 2:
        print("Usage: python scripts/release.py <version>")
        print("Example: python scripts/release.py 0.2.0")
        sys.exit(1)

    version = sys.argv[1]

    # Validate version format
    if not re.match(r"^\d+\.\d+\.\d+$", version):
        print("Error: Version must be in format X.Y.Z (e.g., 0.2.0)")
        sys.exit(1)

    print(f"Preparing release {version}...")

    # Update version in pyproject.toml
    update_version(version)

    print(f"\nRelease {version} prepared!")
    print("\nNext steps:")
    print(f"1. Commit changes: git add . && git commit -m 'Release {version}'")
    print("2. Push to main: git push origin main")
    print("3. Create GitHub release:")
    print("   - Go to GitHub repository")
    print("   - Click 'Releases' → 'Create a new release'")
    print(f"   - Set tag to v{version}")
    print("   - Add release notes and publish")
    print("4. GitHub Actions will automatically publish to PyPI")
    print("\nNote: Project uses src/ layout structure for better packaging practices.")


if __name__ == "__main__":
    main()
