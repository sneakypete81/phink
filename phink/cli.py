import sys
from typing import List

from .build import build
from .init import init


def main(args: List[str] = sys.argv[1:]) -> None:
    if args == []:
        args = ["build"]

    command = args[0]
    if command == "build":
        build()
    elif command == "init":
        init()
    else:
        print(f"Invalid command: {command}")
        sys.exit(1)
