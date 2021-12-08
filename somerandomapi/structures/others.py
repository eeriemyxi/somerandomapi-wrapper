from somerandomapi.endpoint import Endpoint
from typing import Optional, IO
from somerandomapi import http
from dataclasses import dataclass


@dataclass
class MCNameHistory:
    name: str
    changed_to_at: str


@dataclass
class MC:
    username: str
    uuid: str
    name_history: list[MCNameHistory]


@dataclass
class Lyrics:
    title: str
    author: str
    lyrics: str
    thumbnail: str
    link: str


@dataclass
class Meme:
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


endpoint = Endpoint(_get_other, _async_get_other)


meme: Meme = endpoint("meme")


joke: str = endpoint("joke")


def chatbot(message: str, key: str) -> str:
    return endpoint(chatbot, message=message, key=key)


def mc(username: str) -> MC:
    return endpoint(mc, username=username)


def lyrics(title: str) -> Lyrics:
    return endpoint(lyrics, title=title)


def colorviewer(hex: str) -> IO:
    return endpoint("canvas/colorviewer", hex=hex)


def youtube_comment(
    avatar: str, username: str, comment: str, key: Optional[str] = None
) -> IO:
    return endpoint(
        "canvas/youtube-comment",
        username=username,
        avatar=avatar,
        comment=comment,
        key=key,
    )
