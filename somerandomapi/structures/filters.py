from typing import IO, Optional

from somerandomapi import http
from somerandomapi.endpoint import Endpoint


async def _async_get_filter(filter: str, **queries: dict) -> IO:
    async with http.GET(("canvas", filter.lower()), queries) as response:
        return response.content


def _get_filter(filter: str, **queries: dict) -> IO:
    with http.GET(("canvas", filter.lower()), queries) as response:
        return response.content


_endpoint = Endpoint(_get_filter, _async_get_filter)


class Filter:
    @staticmethod
    def greyscale(avatar: str, key: str) -> IO:
        return _endpoint("greyscale", avatar=avatar, key=key)

    @staticmethod
    def invert(avatar: str, key: str) -> IO:
        return _endpoint("invert", avatar=avatar, key=key)

    @staticmethod
    def invert_greyscale(avatar: str, key: str) -> IO:
        return _endpoint("invert_greyscale", avatar=avatar, key=key)

    @staticmethod
    def brightness(
        avatar: str, brightness: Optional[float] = None, key: Optional[str] = None
    ) -> IO:
        return _endpoint(brightness, avatar=avatar, key=key, brightness=brightness)

    @staticmethod
    def threshold(
        avatar: str, threshold: Optional[str] = None, key: Optional[str] = None
    ) -> IO:
        return _endpoint(threshold, avatar=avatar, key=key, threshold=threshold)

    @staticmethod
    def sepia(avatar: str, key: str) -> IO:
        return _endpoint("sepia", avatar=avatar, key=key)

    @staticmethod
    def red(avatar: str, key: str) -> IO:
        return _endpoint("red", avatar=avatar, key=key)

    @staticmethod
    def green(avatar: str, key: str) -> IO:
        return _endpoint("green", avatar=avatar, key=key)

    @staticmethod
    def blue(avatar: str, key: str) -> IO:
        return _endpoint("blue", avatar=avatar, key=key)

    @staticmethod
    def blurple(avatar: str, key: str) -> IO:
        return _endpoint("blurple", avatar=avatar, key=key)

    @staticmethod
    def blurple2(avatar: str, key: str) -> IO:
        return _endpoint("blurple2", avatar=avatar, key=key)

    @staticmethod
    def color(
        avatar: str, color: Optional[str] = None, key: Optional[str] = None
    ) -> IO:
        return _endpoint("color", avatar=avatar, key=key, color=color)

    @staticmethod
    def blur(avatar: str, key: Optional[str] = None) -> IO:
        return _endpoint("blur", avatar=avatar, key=key)

    @staticmethod
    def gay(avatar: str, key: Optional[str] = None) -> IO:
        return _endpoint("gay", avatar=avatar, key=key)

    @staticmethod
    def glass(avatar: str, key: Optional[str] = None) -> IO:
        return _endpoint("glass", avatar=avatar, key=key)

    @staticmethod
    def wasted(avatar: str, key: Optional[str] = None) -> IO:
        return _endpoint("wasted", avatar=avatar, key=key)

    @staticmethod
    def pixelate(avatar: str, key: Optional[str] = None) -> IO:
        return _endpoint("pixelate", avatar=avatar, key=key)

    @staticmethod
    def lolice(avatar: str, key: Optional[str] = None) -> IO:
        return _endpoint("lolice", avatar=avatar, key=key)

    @staticmethod
    def horny_card(avatar: str, key: Optional[str] = None) -> IO:
        return _endpoint("simp", avatar=avatar, key=key)

    @staticmethod
    def simp_card(avatar: str, key: Optional[str] = None) -> IO:
        return _endpoint("simpcard", avatar=avatar, key=key)

    @staticmethod
    def stupid(avatar: str, dog: str, key: Optional[str] = None) -> IO:
        return _endpoint("its-so-stupid", avatar=avatar, dog=dog, key=key)

    @staticmethod
    def triggered(avatar: str, key: Optional[str] = None) -> IO:
        return _endpoint("triggered", avatar=avatar, key=key)

    @staticmethod
    def tweet(
        avatar: str,
        username: str,
        display_name: str,
        comment: str,
        replies: Optional[int] = None,
        retweets: Optional[int] = None,
        likes: Optional[int] = None,
        theme: str = None,
        key: Optional[str] = None,
    ) -> IO:
        return _endpoint(
            "tweet",
            avatar=avatar,
            username=username,
            display_name=display_name,
            comment=comment,
            replies=replies,
            retweets=retweets,
            likes=likes,
            theme=theme,
            key=key,
        )
