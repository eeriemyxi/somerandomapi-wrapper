from dataclasses import dataclass
from somerandomapi import http
from somerandomapi.constants import ANIME
from somerandomapi.sync_async_handler import SyncAsyncHandler


@dataclass
class AnimeResponse:
    """
    Attributes
    ----------
    - link: `str`
    """
    link: str


class Anime(type):
    def __getattr__(self, category):
        if category.upper() in ANIME:
            return SyncAsyncHandler(self.get_anime, self.async_get_anime, category)
        else:
            raise AttributeError("Unknown category.") from None

    async def async_get_anime(self, category: str):
        async with http.GET(("animu", category.lower())) as response:
            get = response.json().get
            DC = AnimeResponse(link=get("link"))
            return DC

    def get_anime(self, category: str):
        with http.GET(("animu", category.lower())) as response:
            get = response.json().get
            DC = AnimeResponse(link=get("link"))
            return DC

class AnimeMeta(metaclass=Anime):
    """
    Docs: https://some-random-api.ml/docs/endpoints/animu

    Attributes
    ----------
    - wink: `AnimeResponse`
    - pat: `AnimeResponse`
    - hug: `AnimeResponse`
    """
    wink: AnimeResponse
    pat: AnimeResponse
    hug: AnimeResponse
    pass
