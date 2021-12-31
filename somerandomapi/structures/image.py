from somerandomapi import http
from somerandomapi.endpoint import Endpoint


class Image:
    async def _async_get_image(animal: str):
        async with http.GET(("img", animal.lower())) as response:
            get = response.json().get
            return get("link")

    def _get_image(animal: str):
        with http.GET(("img", animal.lower())) as response:
            get = response.json().get
            return get("link")

    _endpoint = Endpoint(_get_image, _async_get_image)

    dog: str = _endpoint("dog")
    cat: str = _endpoint("cat")
    panda: str = _endpoint("panda")
    fox: str = _endpoint("fox")
    red_panda: str = _endpoint("red_panda")
    koala: str = _endpoint("koala")
    bird: str = _endpoint("birb")
    raccoon: str = _endpoint("raccoon")
    kangaroo: str = _endpoint("kangaroo")
    whale: str = _endpoint("whale")
    pikachu: str = _endpoint("pikachu")
