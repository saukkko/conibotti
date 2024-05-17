from typing import TypedDict


class AppConfig(TypedDict):
    APP_NAME: str
    APP_VERSION: str
    ENDPOINT_URL: str
    APPLICATION_ID: str | None
    PUBLIC_KEY: str | None
    TOKEN: str | None
    DEBUG: bool | None
