import somerandomapi
import asyncio


async def main():
    async with somerandomapi.Anime.hug as r:
        print(r)

if __name__ == "__main__":
    asyncio.run(main())
