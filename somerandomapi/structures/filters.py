from typing import Optional, IO
from somerandomapi import http
from somerandomapi.constants import FILTERS
from somerandomapi.sync_async_handler import SyncAsyncHandler


class FilterData:
    def __init__(self, filter, get_filter, async_get_filter):
        self.filter = filter
        self.get_filter = get_filter
        self.async_get_filter = async_get_filter

    def __call__(self, avatar: str, key: str):
        """
        Attributes
        ----------
        - avatar
        - key
        """
        return SyncAsyncHandler(
            self.get_filter, self.async_get_filter, self.filter, avatar=avatar, key=key
        )


class FilterColor(FilterData):
    def __call__(
        self, avatar: str, color: Optional[str] = None, key: Optional[str] = None
    ):
        """
        Attributes
        ----------
        - avatar
        - color
        - key
        """
        return SyncAsyncHandler(
            self.get_filter,
            self.async_get_filter,
            self.filter,
            avatar=avatar,
            color=color,
            key=key,
        )


class FilterThreshold(FilterData):
    def __call__(
        self, avatar: str, threshold: Optional[str] = None, key: Optional[str] = None
    ):
        """
        Attributes
        ----------
        - avatar
        - threshold
        - key
        """
        return SyncAsyncHandler(
            self.get_filter,
            self.async_get_filter,
            self.filter,
            avatar=avatar,
            threshold=threshold,
            key=key,
        )


class FilterBrightness(FilterData):
    def __call__(
        self, avatar: str, brightness: Optional[float] = None, key: Optional[str] = None
    ):
        """
        Attributes
        ----------
        - avatar
        - brightness
        - key
        """
        return SyncAsyncHandler(
            self.get_filter,
            self.async_get_filter,
            self.filter,
            avatar=avatar,
            brightness=brightness,
            key=key,
        )


class Filter(type):
    def __getattr__(self, filter):
        if filter.upper() in FILTERS:
            args = (filter, self.get_filter, self.async_get_filter)
            match filter.lower():
                case "brightness":
                    return FilterBrightness(*args)
                case "threshold":
                    return FilterThreshold(*args)
                case "color":
                    return FilterColor(*args)
                case _:
                    return FilterData(*args)
        else:
            raise AttributeError("Unknown filter.") from None

    async def async_get_filter(self, filter: str, **queries: dict) -> IO:
        async with http.GET(("canvas", filter.lower()), queries) as response:
            return response

    def get_filter(self, filter: str, **queries: dict) -> IO:
        with http.GET(("canvas", filter.lower()), queries) as response:
            return response


class FilterMeta(metaclass=Filter):
    """
    Docs: https://some-random-api.ml/docs/canvas/filter

    Attributes
    ----------
    - greyscale: `FilterData`
    - invert: `FilterData`
    - invert_greyscale: `FilterData`
    - brightness: `FilterBrightness`
    - threshold: `FilterThreshold`
    - sepia: `FilterData`
    - red: `FilterData`
    - green: `FilterData`
    - bloo: `FilterData`
    - blurple: `FilterData`
    - blurple2: `FilterData`
    - color: `FilterColor`
    """
    greyscale: FilterData
    invert: FilterData
    invert_greyscale: FilterData
    brightness: FilterBrightness
    threshold: FilterThreshold
    sepia: FilterData
    red: FilterData
    green: FilterData
    bloo: FilterData
    blurple: FilterData
    blurple2: FilterData
    color: FilterColor

    pass
