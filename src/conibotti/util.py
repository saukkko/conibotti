from os import getenv
from sys import argv, orig_argv


def is_debug() -> bool:
    return any([
        getenv("DEBUG") is not None,
        "--debug" in argv,
        "--debug" in orig_argv
    ])


def validate_env():
    if getenv("DEBUG") and getenv("PRODUCTION"):
        raise ValueError(" ".join([
            "Both DEBUG and PRODUCTION environment variables are set.",
            "Only one may be set."]))
