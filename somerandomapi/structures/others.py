from dataclasses import dataclass
from typing import IO, Optional

from somerandomapi import http
from somerandomapi.endpoint import Endpoint


@dataclass
class MCNameHistory:
    """This is just a dataclass. Use :meth:`somerandomapi.Other.mc`"""
    name: str
    changed_to_at: str


@dataclass
class MC:
    """This is just a dataclass. Use :meth:`somerandomapi.Other.mc`"""
    username: str
    uuid: str
    name_history: list[MCNameHistory]


@dataclass
class Lyrics:
    """This is just a dataclass. Use :meth:`somerandomapi.Other.lyrics`"""
    title: str
    author: str
    lyrics: str
    thumbnail: str
    link: str


@dataclass
class Meme:
    """This is just a dataclass. Use :meth:`somerandomapi.Other.meme`"""
    id: int
    image: str
    caption: str
    category: str


def _get_other(endpoint: str, **queries):
    with http.GET(endpoint, queries) as resp:
        return endpoint_handler(endpoint, resp)


async def _async_get_other(endpoint: str, **queries):
    async with http.GET(endpoint, queries) as resp:
        return endpoint_handler(endpoint, resp)


def endpoint_handler(endpoint: str, resp):
    endpoint = endpoint.lower()
    if endpoint in ("canvas/youtube-comment", "canvas/colorviewer"):
        return resp.content
    resp = resp.json()

    if endpoint == "chatbot":
        return resp["response"]
    elif endpoint == "mc":
        return MC(
            username=resp["username"],
            uuid=resp["uuid"],
            name_history=[
                MCNameHistory(name=d["name"], changed_to_at=d["changedToAt"])
                for d in resp["name_history"]
            ],
        )
    elif endpoint == "lyrics":
        return Lyrics(
            title=resp["title"],
            author=resp["author"],
            lyrics=resp["lyrics"],
            thumbnail=resp["thumbnail"]["genius"],
            link=resp["links"]["genius"],
        )
    elif endpoint == "meme":
        return Meme(
            id=int(resp["id"]),
            image=resp["image"],
            caption=resp["caption"],
            category=resp["category"],
        )
    elif endpoint == "joke":
        return resp["joke"]
    
    elif endpoint == "canvas/rgb":
        return resp["r"], resp['g'], resp["b"]
    
    elif endpoint == "canvas/hex":
        return resp["hex"]


_endpoint = Endpoint(_get_other, _async_get_other)


class Other:
    meme: Meme = _endpoint("meme")

    joke: str = _endpoint("joke")

    @staticmethod
    def chatbot(message: str, key: str) -> str:
        return _endpoint("chatbot", message=message, key=key)

    @staticmethod
    def mc(username: str) -> MC:
        return _endpoint("mc", username=username)

    @staticmethod
    def lyrics(title: str) -> Lyrics:
        return _endpoint("lyrics", title=title)

    @staticmethod
    def colorviewer(hex: str) -> IO:
        return _endpoint("canvas/colorviewer", hex=hex)

    @staticmethod
    def youtube_comment(
        avatar: str, username: str, comment: str, key: Optional[str] = None
    ) -> IO:
        return _endpoint(
            "canvas/youtube-comment",
            username=username,
            avatar=avatar,
            comment=comment,
            key=key,
        )
    
    @staticmethod
    def as_hex(rgb: tuple[int, int, int]) -> str:
        return _endpoint("canvas/hex", rgb=",".join(rgb))

    @staticmethod
    def as_rgb(hex: str) -> tuple[int, int, int]:
        return _endpoint("canvas/rgb", hex=hex)