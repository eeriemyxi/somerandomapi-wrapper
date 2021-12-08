from dataclasses import dataclass
from somerandomapi import http
from somerandomapi.constants import ANIMALS
from somerandomapi.sync_async_handler import SyncAsyncHandler


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


class Animal(type):
    def __getattr__(self, animal):
        if animal.upper() in ANIMALS:
            return SyncAsyncHandler(self.get_animal, self.async_get_animal, animal)
        else:
            raise AttributeError("Unknown animal.") from None

    async def async_get_animal(self, animal: str):
        async with http.GET(("animal", animal.lower())) as response:
            get = response.json().get
            DC = AnimalResponse(fact=get("fact"), image=get("image"))
            return DC

    def get_animal(self, animal: str):
        with http.GET(("animal", animal.lower())) as response:
            get = response.json().get
            DC = AnimalResponse(fact=get("fact"), image=get("image"))
            return DC


class AnimalMeta(metaclass=Animal):
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
    dog: AnimalResponse
    cat: AnimalResponse
    panda: AnimalResponse
    fox: AnimalResponse
    red_panda: AnimalResponse
    koala: AnimalResponse
    bird: AnimalResponse
    raccoon: AnimalResponse
    kangaroo: AnimalResponse

    pass
