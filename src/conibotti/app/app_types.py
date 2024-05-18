from typing import Any, Literal, Required, TypedDict


class AppConfig(TypedDict):
    APP_NAME: str
    APP_VERSION: str
    ENDPOINT_URL: str
    APPLICATION_ID: str | None
    PUBLIC_KEY: str | None
    TOKEN: str | None
    DEBUG: bool | None


class LogConfig(TypedDict):
    version: Required[Literal[1]]
    formatters: dict[str, Any]
    filters: dict[str, Any] | None
    handlers: dict[str, Any]
    loggers: dict[str, Any]
    root: Any | None
    incremental: bool
    disable_existing_loggers: bool
