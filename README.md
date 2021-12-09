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

# [Documentation](https://m-y-x-i.github.io/somerandomapi.ml-api-wrapper/html/somerandomapi.html)
I am not completely happy with the docs and its still being fixed but its pretty usable, [**click here to check it.**](https://m-y-x-i.github.io/somerandomapi.ml-api-wrapper/html/somerandomapi.html)

# Note
- Not all endpoints has been added yet. However those will be added soon.
- I will not add it to Pypi until I add support for all the endpoints. Follow the steps listed below to use it.

# How to install
- First clone the repository.
- Install the packages listed in [requirements.txt](/requirements.txt)
    - `py -m pip install -r requirements.txt`
- Copy the folder [somerandomapi](/somerandomapi) to where you want to use it.
- You may then use the wrapper by importing `somerandomapi`.
