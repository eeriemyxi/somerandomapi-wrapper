"""
Docs: https://some-random-api.ml/docs/endpoints/animal

Attributes
----------
- dog: `AnimalResponse`
- cat: `AnimalResponse`
- panda: `AnimalResponse`
- fox: `AnimalResponse`
- red_panda: `AnimalResponse`
- koala: `AnimalResponse`
- bird: `AnimalResponse`
- raccoon: `AnimalResponse`
- kangaroo: `AnimalResponse`
"""

from dataclasses import dataclass
from somerandomapi import http
from somerandomapi.endpoint import Endpoint


@dataclass
class AnimalResponse:
    """
    Attributes
    ----------
    - fact: `str`
    - image: `str`
    """

    fact: str
    image: str


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


endpoint = Endpoint(_get_animal, _async_get_animal)

dog: AnimalResponse = endpoint("dog")
cat: AnimalResponse = endpoint("cat")
panda: AnimalResponse = endpoint("panda")
fox: AnimalResponse = endpoint("fox")
red_panda: AnimalResponse = endpoint("red_panda")
koala: AnimalResponse = endpoint("koala")
bird: AnimalResponse = endpoint("bird")
raccoon: AnimalResponse = endpoint("raccoon")
kangaroo: AnimalResponse = endpoint("kangaroo")
whale: AnimalResponse = endpoint("whale")
