"""
Docs: https://some-random-api.ml/docs/endpoints/animu

Attributes
----------
- wink: `str`
- pat: `str`
- hug: `str`
"""

from somerandomapi import http
from somerandomapi.endpoint import Endpoint


class Anime:
    async def _async_get_anime(category: str):
        async with http.GET(("animu", category.lower())) as response:
            get = response.json().get
            return get("link")

    def _get_anime(category: str):
        with http.GET(("animu", category.lower())) as response:
            get = response.json().get
            return get("link")

    _endpoint = Endpoint(_get_anime, _async_get_anime)

    wink: str = _endpoint("end")
    pat: str = _endpoint("pat")
    hug: str = _endpoint("hug")
    face_palm: str = _endpoint("face-palm")
    quote: str = _endpoint("quote")
