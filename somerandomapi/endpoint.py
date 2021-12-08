from typing import Callable, Union
from inspect import isfunction
from .sync_async_handler import SyncAsyncHandler


class Endpoint:
    def __init__(self, sync_func, async_func):
        self.sync_func = sync_func
        self.async_func = async_func

    def __call__(self, name: Union[Callable, str], **kwargs):
        return SyncAsyncHandler(
            self.sync_func,
            self.async_func,
            name.__name__ if isfunction(name) else name,
            **kwargs
        )
