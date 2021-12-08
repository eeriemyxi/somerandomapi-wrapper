"""
Docs: https://some-random-api.ml/docs/endpoints/animu

Attributes
----------
- wink: `AnimeResponse`
- pat: `AnimeResponse`
- hug: `AnimeResponse`
"""

from dataclasses import dataclass
from somerandomapi import http
from somerandomapi.endpoint import Endpoint


@dataclass
class AnimeResponse:
    """
    Attributes
    ----------
    - link: `str`
    """
    link: str

async def _async_get_anime(category: str):
    async with http.GET(("animu", category.lower())) as response:
        get = response.json().get
        DC = AnimeResponse(link=get("link"))
        return DC

def _get_anime(category: str):
    with http.GET(("animu", category.lower())) as response:
        get = response.json().get
        DC = AnimeResponse(link=get("link"))
        return DC

endpoint = Endpoint(_get_anime, _async_get_anime)

wink: AnimeResponse = endpoint("end")
pat: AnimeResponse = endpoint("pat")
hug: AnimeResponse = endpoint("hug")