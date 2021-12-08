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

# Note
- Not all endpoints has been added yet. However those will be added soon.
- There is currently no online documentation. I have added detailed docstrings, you can read those. DM me, `Myxi#1818` on Discord, if you are confused with anything.
- I will not add it to Pypi until I add support for all the endpoints. Follow the steps listed below to use it.

# How to install
- First clone the repository.
- Copy the folder [somerandomapi](/somerandomapi) to where you want to use it.
- You may then use the wrapper by importing `somerandomapi`.