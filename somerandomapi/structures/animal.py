from dataclasses import dataclass

from somerandomapi import http
from somerandomapi.endpoint import Endpoint


@dataclass
class AnimalResponse:
    fact: str
    image: str


class Animal:
    async def _async_get_animal(animal: str):
        async with http.GET(("animal", animal.lower())) as response:
            get = response.json().get
            DC = AnimalResponse(fact=get("fact"), image=get("image"))
            return DC

    def _get_animal(animal: str):
        with http.GET(("animal", animal.lower())) as response:
            get = response.json().get
            DC = AnimalResponse(fact=get("fact"), image=get("image"))
            return DC

    _endpoint = Endpoint(_get_animal, _async_get_animal)

    dog: AnimalResponse = _endpoint("dog")
    cat: AnimalResponse = _endpoint("cat")
    panda: AnimalResponse = _endpoint("panda")
    fox: AnimalResponse = _endpoint("fox")
    red_panda: AnimalResponse = _endpoint("red_panda")
    koala: AnimalResponse = _endpoint("koala")
    bird: AnimalResponse = _endpoint("bird")
    raccoon: AnimalResponse = _endpoint("raccoon")
    kangaroo: AnimalResponse = _endpoint("kangaroo")
    whale: AnimalResponse = _endpoint("whale")
