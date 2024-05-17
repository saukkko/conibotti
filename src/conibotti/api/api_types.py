from typing import TypeAlias, TypedDict, List
from urllib3.util import Url
from datetime import datetime

EventList: TypeAlias = List["EventData"]


class EventData(TypedDict):
    slug: str
    name: str
    headline: str
    venue_name: str
    homepage_url: Url
    start_time: datetime
    end_time: datetime
    cancelled: bool


class ConitData(TypedDict):
    hostname: str
    title: str
    events: EventList
