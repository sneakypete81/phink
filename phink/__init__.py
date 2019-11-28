import pkg_resources

__version__ = pkg_resources.get_distribution(__package__).version

from .cli import main

__all__ = [main]
