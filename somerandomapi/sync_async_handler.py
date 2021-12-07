from typing import Callable, Coroutine


class SyncAsyncHandler:
    def __init__(self, sync_func: Callable, async_func: Coroutine, *args, **kwargs):
        self.sync_func = sync_func
        self.async_func = async_func
        self.args = args
        self.kwargs = {k:v for k,v in kwargs.items() if v is not None}

    def __enter__(self):
        return self.sync_func(*self.args, **self.kwargs)

    def __exit__(self, exc_type, exc, tb):
        pass

    async def __aenter__(self):
        return await self.async_func(*self.args, **self.kwargs)

    async def __aexit__(self, exc_type, exc, tb):
        pass
