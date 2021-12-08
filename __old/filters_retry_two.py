from typing import Optional, IO
from somerandomapi import http
from somerandomapi.sync_async_handler import SyncAsyncHandler


# class Endpoint:
#     def __init__(self, func, callable, coro, **kwargs):
#         self.kwargs = kwargs
#         self.func = func
#         self.callable = callable
#         self.coro = coro

#     def __call__(self):
#         SyncAsyncHandler(self.callable, self.coro, self.func.__name__, **self.kwargs)
class Endpoint:
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def __call__(self):
        return SyncAsyncHandler(_get_filter, _async_get_filter, self.func.__endpoint__, *self.args, **self.kwargs)

def endpoint(name=None):
    def inner(func):
        setattr(func, "__endpoint__", name or func.__name__)
        return func
    return inner
    # return Endpoint(func, _get_filter, _async_get_filter, **func())

async def _async_get_filter(filter: str, **queries: dict) -> IO:
    async with http.GET(("canvas", filter.lower()), queries) as response:
        return response

def _get_filter(filter: str, **queries: dict) -> IO:
    with http.GET(("canvas", filter.lower()), queries) as response:
        return response

class FilterMeta:
    @endpoint()
    def greyscale(self, avatar: str, key: str):
        return Endpoint(self.greyscale, avatar=avatar, key=key)

    # def invert(self, avatar: str, key: str):
    #     return SyncAsyncHandler(
    #         self._get_filter, self._async_get_filter, self.filter, avatar=avatar, key=key
    #     )
    # def invert_greyscale(self, avatar: str, key: str):
    #     return SyncAsyncHandler(
    #         self._get_filter, self._async_get_filter, self.filter, avatar=avatar, key=key
    #     )
    # def brightness(self, avatar: str, brightness: Optional[float] = None, key: Optional[str] = None):
    #     return SyncAsyncHandler(
    #         self._get_filter,
    #         self._async_get_filter,
    #         self.filter,
    #         avatar=avatar,
    #         brightness=brightness,
    #         key=key,
    #     )
    # def threshold(self, avatar: str, threshold: Optional[str] = None, key: Optional[str] = None):
    #     return SyncAsyncHandler(
    #         self._get_filter,
    #         self._async_get_filter,
    #         self.filter,
    #         avatar=avatar,
    #         threshold=threshold,
    #         key=key,
    #     )
    # def sepia(self, avatar: str, key: str):
    #     return SyncAsyncHandler(
    #         self._get_filter, self._async_get_filter, "sepia", avatar=avatar, key=key
    #     )
    # def red(self, avatar: str, key: str):
    #     return SyncAsyncHandler(
    #         self._get_filter, self._async_get_filter, self.filter, avatar=avatar, key=key
    #     )
    # def green(self, avatar: str, key: str):
    #     return SyncAsyncHandler(
    #         self._get_filter, self._async_get_filter, self.filter, avatar=avatar, key=key
    #     )
    # def bloo(self, avatar: str, key: str):
    #     return SyncAsyncHandler(
    #         self._get_filter, self._async_get_filter, self.filter, avatar=avatar, key=key
    #     )
    # def blurple(self, avatar: str, key: str):
    #     return SyncAsyncHandler(
    #         self._get_filter, self._async_get_filter, self.filter, avatar=avatar, key=key
    #     )
    # def blurple2(self, avatar: str, key: str):
    #     return SyncAsyncHandler(
    #         self._get_filter, self._async_get_filter, self.filter, avatar=avatar, key=key
    #     )
    # def color(self, avatar: str, color: Optional[str] = None, key: Optional[str] = None):
    #     return SyncAsyncHandler(
    #         self._get_filter,
    #         self._async_get_filter,
    #         self.filter,
    #         avatar=avatar,
    #         color=color,
    #         key=key,
    #     )
    # async def _async_get_filter(self, filter: str, **queries: dict) -> IO:
    #     async with http.GET(("canvas", filter.lower()), queries) as response:
    #         return response

    # def _get_filter(self, filter: str, **queries: dict) -> IO:
    #     with http.GET(("canvas", filter.lower()), queries) as response:
    #         return response


# class FilterMeta(metaclass=Filter):
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
    pass
