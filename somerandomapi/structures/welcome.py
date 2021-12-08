from somerandomapi.sync_async_handler import SyncAsyncHandler
from somerandomapi import http


def welcome(
    key: str,
    image: int,
    background: str,
    type: str,
    avatar: str,
    username: str,
    discriminator: int,
    guild_name: str,
    text_color: str,
    member_count: int,
):
    """
    Docs: https://some-random-api.ml/docs/canvas/welcome

    Attribute
    ---------
    - key
        - This endpoint requires a key to use but even if the key is expired it is fine.
    - image
        - It must be between 1 and 7.
    - backround
        - Must be one of these:
            - stars
            - stars2
            - rainbowgradient
            - rainbow
            - sunset
            - night
            - blobday
            - blobnight
            - space
            - gaming1
            - gaming3
            - gaming2
            - gaming4
    - type
        - Could be either `join` or `leave`
    - avatar
    - username
        - Maximum 30 characters
    - discriminator
    - guild_name
    - text_color
    - member_count
    """
    return SyncAsyncHandler(
        get_welcome,
        async_get_welcome,
        key=key,
        image=image,
        background=background,
        type=type,
        avatar=avatar,
        username=username,
        discriminator=discriminator,
        guildName=guild_name,
        textcolor=text_color,
        memberCount=member_count,
    )


class Query:
    def __init__(self, queries):
        self.__dict__.update(queries)


async def async_get_welcome(**queries):
    query = Query(queries)
    queries.pop("image", None)
    queries.pop("background", None)
    async with http.GET(
        ("welcome", "img", str(query.image), query.background), queries
    ) as response:
        return response


def get_welcome(**queries):
    query = Query(queries)
    queries.pop("image", None)
    queries.pop("background", None)
    with http.GET(("img", query.image, query.background), queries) as response:
        return response
