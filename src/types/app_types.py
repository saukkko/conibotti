from typing import TypedDict


class AppConfig(TypedDict):
    ENDPOINT_URL: str
    APPLICATION_ID: str
    PUBLIC_KEY: str
    TOKEN: str | None
