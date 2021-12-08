import somerandomapi
# # import asyncio

with somerandomapi.Filter.greyscale(key="u9epAaOr8RrTCMle62hxnVCGf", avatar="https://cdn.discordapp.com/avatars/764897680060973067/f3593c937adabc2da8bb8185f85dc5e3.png?size=4096") as resp:
    print(type(resp))
# async def main():
#     async with somerandomapi.Welcome("u9epAaOr8RrTCMle62hxnVCGf", 1, "stars2", "join", "https://cdn.discordapp.com/avatars/764897680060973067/f3593c937adabc2da8bb8185f85dc5e3.png?size=4096", "Myxi", 4444, "Server Name", "red", 333) as resp:
#         with open("hi.png", "wb") as f:
#             f.write(resp)
#             f.close()

# asyncio.run(main())