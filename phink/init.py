from pathlib import Path
from typing import Optional


def init() -> None:
    doc_path = Path("doc")
    if doc_path.exists():
        raise FileExistsError(f"'doc/' directory already exists.")
    create_dirs(doc_path)

    data = Data.get_user_input()
    data.doc_path = doc_path
    create_readme_symlink(data)
    apply_template("conf.py", data)
    apply_template("index.rst", data)
    apply_template("customising.md", data)
    apply_template("api.md", data)

    print()
    print(f"Documentation source has been written to '{doc_path}/'.")
    print("Please edit it as you wish.")
    print("Use 'phink build' to generate the HTML.")


def create_dirs(doc_path: Path) -> None:
    doc_path.mkdir()
    (doc_path / "_static").mkdir()


class Data:
    project: str
    author: str
    project_section_underline: str

    @classmethod
    def get_user_input(cls) -> "Data":
        data = cls()
        data.project = cls.ask("Project name")
        data.author = cls.ask("Author")
        data.project_section_underline = "=" * len(data.project)
        return data

    @staticmethod
    def ask(question):
        answer = input(f"{question}: ")
        if answer == "":
            raise ValueError("No answer given - aborting.")
        return answer

    def __getattr__(self, name: str) -> str:
        if name.startswith("_section_underline_"):
            return "=" * len(getattr(self, name[19:]))

        raise AttributeError


def create_readme_symlink(data: Data) -> None:
    readme_source_path = data.doc_path / ".." / "README.md"
    if not readme_source_path.exists():
        apply_template("README.md", data, output_path=(data.doc_path / ".."))

    symlink = data.doc_path / "README.md"
    symlink.symlink_to(Path("..") / "README.md")


def apply_template(
    template_name: str, data: Data, output_path: Optional[Path] = None
) -> None:
    if output_path is None:
        output_path = data.doc_path
    template_path = Path(__file__).parent / "templates" / template_name
    template = template_path.read_text()
    text = template.format(data=data)
    (output_path / template_name).write_text(text)
