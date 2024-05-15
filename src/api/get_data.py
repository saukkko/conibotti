import requests
from urllib3.util import Url, parse_url
from pathlib import Path
from json import load as json_load

from .decoder import decode_hook
from .types.api_types import ConitData


class EndpointUrl(Url):
    @staticmethod
    def parse(url: str) -> "EndpointUrl":
        _url: Url = parse_url(url=url)
        (
            scheme, auth, host,
            port, path, query,
            fragment
        ) = _url
        return EndpointUrl(scheme=scheme, auth=auth, host=host,
                           port=port, path=path, query=query,
                           fragment=fragment)

    def __repr__(self) -> str:
        return self.url


def load_data(endpoint: EndpointUrl, *, use_local: bool = False) -> ConitData:
    data: ConitData
    if use_local:
        with Path("data/conit.fi.json").open("rb") as f:
            data = json_load(f, object_hook=decode_hook)
    else:
        req = requests.get(url=endpoint.url)
        return req.json(object_hook=decode_hook)

    return data
