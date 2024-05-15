from .types.app_types import AppConfig
from .api.get_data import load_data, EndpointUrl


class App():
    APP_NAME = "The App"
    __config: AppConfig

    def __init__(self, config: AppConfig) -> None:
        self.__config = config

    @property
    def config(self) -> AppConfig:
        return self.__config

    @config.setter
    def config(self, value) -> None:
        self.__config = value

    @config.deleter
    def config(self) -> None:
        del self.__config

    def __repr__(self) -> str:
        return self.APP_NAME

    def start(self) -> None:
        print(f"Starting `{self}` with configuration `{self.config}`")

    def print_events(self) -> None:
        endpoint = EndpointUrl.parse(self.config["ENDPOINT_URL"])
        data = load_data(endpoint=endpoint, use_local=True)

        for evt in data["events"]:
            (
                name,
                headline,
                start_time,
                end_time
            ) = (
                evt["name"],
                evt["headline"],
                evt["start_time"],
                evt["end_time"]
            )
            print("-"*79)
            print(name)
            print(headline)
            print(
                f"{start_time} - " +
                f"{end_time}")
            print("-"*79)
