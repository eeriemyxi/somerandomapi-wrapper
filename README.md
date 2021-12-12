# Overview

`somerandomapi` is an API Wrapper for [some-random-api.ml](https://some-random-api.ml/)

## Examples

### Asynchronous

```py
from somerandomapi import Animal
import asyncio


async def main():
    async with Animal.dog as resp:
        print(
            f"Fact: {resp.fact}",
            f"Image: {resp.image}",
            sep="\n"
        )
asyncio.run(main())
```

### Synchronous

```py
from somerandomapi import Animal


with Animal.dog as resp:
    print(
        f"Fact: {resp.fact}",
        f"Image: {resp.image}",
        sep="\n"
    )
```
Easy, isn't it?

# [Documentation](https://m-y-x-i.github.io/some-random-api-API-Wrapper/html/somerandomapi.html)
I am not completely happy with the docs and its still being fixed but its pretty usable, [**click here to check it.**](https://m-y-x-i.github.io/some-random-api-API-Wrapper/html/somerandomapi.html)

# Note
- I added support for all endpoints except `binary` and `base64` because Python has built-in libraries for those operations which are faster. However, if someone makes a good pull request for it, I will merge it.

# How to install
- Manual
    - First clone the repository.
    - Install the packages listed in [requirements.txt](/requirements.txt)
        - `py -m pip install -r requirements.txt`
    - Copy the folder [somerandomapi](/somerandomapi) to where you want to use it.
    - You may then use the wrapper by importing `somerandomapi`.
- Pypi
    - `py -m pip install somerandomapiml`
    - That's it.
