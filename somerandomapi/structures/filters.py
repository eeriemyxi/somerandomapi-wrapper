"""
Docs: https://some-random-api.ml/docs/canvas/filter

Methods
-------
- greyscale
- invert
- invert_greyscale
- brightness
- threshold
- sepia
- red
- green
- bloo
- blurple
- blurple2
- color
"""

from typing import Optional, IO
from somerandomapi import http
from somerandomapi.endpoint import Endpoint


async def _async_get_filter(filter: str, **queries: dict) -> IO:
    async with http.GET(("canvas", filter.lower()), queries) as response:
        return response


def _get_filter(filter: str, **queries: dict) -> IO:
    with http.GET(("canvas", filter.lower()), queries) as response:
        return response

endpoint = Endpoint(_get_filter, _async_get_filter)

def greyscale(avatar: str, key: str) -> IO:
    return endpoint(greyscale, avatar=avatar, key=key)


def invert(avatar: str, key: str) -> IO:
    return endpoint(invert, avatar=avatar, key=key)


def invert_greyscale(avatar: str, key: str) -> IO:
    return endpoint(invert_greyscale, avatar=avatar, key=key)


def brightness(
    avatar: str, brightness: Optional[float] = None, key: Optional[str] = None
) -> IO:
    return endpoint(brightness, avatar=avatar, key=key, brightness=brightness)


def threshold(avatar: str, threshold: Optional[str] = None, key: Optional[str] = None) -> IO:
    return endpoint(threshold, avatar=avatar, key=key, threshold=threshold)


def sepia(avatar: str, key: str) -> IO:
    return endpoint(sepia, avatar=avatar, key=key)


def red(avatar: str, key: str) -> IO:
    return endpoint(red, avatar=avatar, key=key)


def green(avatar: str, key: str) -> IO:
    return endpoint(green, avatar=avatar, key=key)


def bloo(avatar: str, key: str) -> IO:
    return endpoint(bloo, avatar=avatar, key=key)


def blurple(avatar: str, key: str) -> IO:
    return endpoint(blurple, avatar=avatar, key=key)


def blurple2(avatar: str, key: str) -> IO:
    return endpoint(blurple2, avatar=avatar, key=key)


def color(avatar: str, color: Optional[str] = None, key: Optional[str] = None) -> IO:
    return endpoint("color", avatar=avatar, key=key, color=color)