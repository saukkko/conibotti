from interactions import Client, Intents, to_snowflake

from api.get_data import load_data, EndpointUrl
from api.api_types import ConitData, EventData
from .app_types import AppConfig


class App():
    __config: AppConfig
    __bot: Client

    @property
    def bot(self) -> Client:
        return self.__bot

    @bot.setter
    def bot(self, value: Client):
        self.__bot = value

    @property
    def config(self) -> AppConfig:
        return self.__config

    @config.setter
    def config(self, value) -> None:
        self.__config = value

    def __init__(self, config: AppConfig) -> None:
        DEBUG = config["DEBUG"]
        debug_scope = to_snowflake(691669279376146452 if DEBUG else 0)

        self.config = config
        self.bot = Client(intents=Intents.DEFAULT,
                          debug_scope=debug_scope)

    def __info__(self) -> str:
        app_name, app_version = (
            self.config["APP_NAME"], self.config["APP_VERSION"])
        return f"{app_name} - v{app_version}"

    def __str__(self) -> str:
        return self.__info__()

    def __repr__(self) -> str:
        return self.__info__()

    def __ascii__(self) -> str:
        return self.__info__()

    def format_event_data(self, event: EventData):
        header = f"## {event["name"]}"

        content = ""

        start_dt = event["start_time"]
        end_dt = event["end_time"]

        content += f"> {event["headline"]}\n"
        content += f"> Tapahtuma alkaa: <t:{start_dt.timestamp():.0f}:F>\n"
        content += f"> Tapahtuma päättyy: <t:{end_dt.timestamp():.0f}:F>\n"
        content += f"> Lisätiedot: <{event["homepage_url"]}>\n"

        return "\n".join([header, content])

    def list_events(self, *, data: ConitData | None = None) -> str:
        data = (
            load_data(
                endpoint=EndpointUrl.parse(self.config["ENDPOINT_URL"]))
            if not data
            else data
        )

        header = "# Suomen conitapahtumat"
        footer = f"Datan tarjoaa {data["title"]}"
        content = ""

        for event in data["events"]:
            content += self.format_event_data(event)
            content += "\n"

        return "\n".join([header, content, footer])

    def get_event(self, slug: str, *, data: ConitData | None = None) -> str:
        data = (
            load_data(
                endpoint=EndpointUrl.parse(self.config["ENDPOINT_URL"]))
            if not data
            else data
        )

        footer = f"Datan tarjoaa {data["title"]}"
        content = ""

        for event in data["events"]:
            if event["slug"] == slug:
                content += self.format_event_data(event)
                break
            elif event["slug"].find(slug) >= 0:
                content += self.format_event_data(event)
                break
            elif event["name"].lower().find(slug) >= 0:
                content += self.format_event_data(event)
                break
            else:
                continue
        if len(content) < 1:
            return "Ei löytynyt :("
        else:
            return "\n".join([content, footer])

    def print_events(self) -> None:
        """
        Print events from local file to console
        """
        _ = EndpointUrl
        data = load_data(endpoint=_, use_local=True)

        self.list_events(data=data)
