from pathlib import Path
import sys

from sphinx.cmd import build as sphinx_build


def build() -> None:
    doc_path = Path("doc")
    if not doc_path.exists():
        print("No 'doc/' directory found. Please create one with 'phink init'.")
        sys.exit(1)

    build_path = doc_path / "_build"

    sphinx_build.main([str(doc_path), str(build_path)])
