import os
from pathlib import Path


def _dotenv_exists(p: Path) -> bool:
    return p.exists() and p.is_file() and not p.is_symlink()


def load_dotenv(dotenv_file: str = ".env", *,
                override: bool = False,
                encoding: str = "utf-8") -> None:
    p = Path(dotenv_file).resolve(strict=False)

    # do nothing if there is no .env file
    if not _dotenv_exists(p):
        return

    with p.open("rb", buffering=4096) as f:
        # iterate over lines and read key=value pairs stripping any trailing
        # newline or whitespace
        while line := f.readline():
            k, v = line.decode(encoding).split("=", 1)
            v = v.rstrip()

            # update os.environ only and only if called with override=True or
            # if env var does not exist
            if override or not os.getenv(k, None):
                # strip single or double quotes but not both
                v = v.strip("'") if v.strip("'") != v else v.strip('"')

                # update the env var
                os.environ.update({k: v})
