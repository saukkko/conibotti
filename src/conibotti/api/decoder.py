from datetime import datetime, UTC
from typing import Dict, Any
from urllib3.util import parse_url, Url


class JSONObject(Dict[str, str | Any]):
    ...


def decode_date(date_str: str) -> datetime:
    return datetime.fromisoformat(date_str).astimezone(tz=UTC)


def decode_url(url_str: str) -> Url:
    return parse_url(url_str)


def decode_hook(obj: Dict[str, str | Any]) -> Dict[str, str | Any]:
    o = obj.copy()
    for k, v in obj.items():
        match k:
            case "homepage_url":
                v = decode_url(v)
            case "start_time" | "end_time":
                v = decode_date(v)
                pass
            case _:
                pass
        o.update({k: v})
    return o
