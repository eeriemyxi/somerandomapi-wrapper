import httpx
from yarl import URL
from typing import Optional, Union

BASE_URL = "https://some-random-api.ml"


class API_ERROR(Exception):
    def __init__(self, message, http_code):
        self.http_code = http_code
        self.message = message
        super().__init__(self.message)


class GET:
    def __init__(self, endpoint: Union[tuple[str], str], queries: Optional[dict] = None):
        self.endpoint = endpoint
        self.queries = queries if queries else dict()
        self.queries = {k:str(v) for k, v in self.queries.items() if v is not None}
        self.base_url = URL(BASE_URL)

    def __enter__(self):
        resp = httpx.get(self.parse_url())
        return self.response(resp)

    async def __aenter__(self):
        async with httpx.AsyncClient() as client:
            resp = await client.get(self.parse_url())
            return self.response(resp)

    def parse_url(self):
        if isinstance(self.endpoint, tuple):
            url = self.base_url
            for path in self.endpoint:
                url /= path
        else:
            url = self.base_url / self.endpoint
        url = url.with_query(self.queries)
        return url.human_repr()

    def response(self, resp):
        content_type = resp.headers.get("content-type").split(";")[0].strip()
        if content_type == "application/json":
            error = resp.json().get("error")
            if error is not None:
                raise API_ERROR(error, resp.status_code)
            else:
                return resp
        elif "image" in content_type:
            return resp.content

    def __exit__(self, exc_type, exc, tb):
        pass

    async def __aexit__(self, exc_type, exc, tb):
        pass
