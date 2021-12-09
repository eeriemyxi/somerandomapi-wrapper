from somerandomapi import http
from somerandomapi.endpoint import Endpoint


class Fact:
    async def _async_get_image(animal: str):
        async with http.GET(("facts", animal.lower())) as response:
            get = response.json().get
            return get("fact")

    def _get_image(animal: str):
        with http.GET(("facts", animal.lower())) as response:
            get = response.json().get
            get = response.json().get
            return get("fact")

    _endpoint = Endpoint(_get_image, _async_get_image)

    dog: str = _endpoint("dog")
    cat: str = _endpoint("cat")
    panda: str = _endpoint("panda")
    fox: str = _endpoint("fox")
    koala: str = _endpoint("koala")
    bird: str = _endpoint("birb")
    raccoon: str = _endpoint("raccoon")
    kangaroo: str = _endpoint("kangaroo")
    whale: str = _endpoint("whale")
    elephant: str = _endpoint("elephant")
    giraffe: str = _endpoint("giraffe")
