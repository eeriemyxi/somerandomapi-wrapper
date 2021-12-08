import somerandomapi
import asyncio


async def main():
    async with somerandomapi.Other.joke as r:
        print(r)

asyncio.run(main())
