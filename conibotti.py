from os import getenv
from src.app import App
from src.types.app_types import AppConfig
from dotenv.dotenv import load_dotenv


load_dotenv(".env")


CONFIG: AppConfig = {
    "ENDPOINT_URL": "https://kompassi.eu/api/v1/listings/conit.fi",
    "APPLICATION_ID": "1084717088091934791",
    "PUBLIC_KEY":
        "bcb4f28e5920851f2a1bd8ea1ab3fc7e1234a4e227a4c80e2b4fb1b6eb0df109",
    "TOKEN": None
}


def main() -> None:
    CONFIG["TOKEN"] = getenv("TOKEN", None)
    app = App(config=CONFIG)
    app.start()
    app.print_events()


if __name__ == "__main__":
    main()
