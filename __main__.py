from user import User
import asyncio

token = "token"


async def main():
    user = User(token=token)

    # await user.solve_forever() майним или решаем, или и то и то в екзекуторе

    await user.mine_forever()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
