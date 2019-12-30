from user import User
import asyncio
import logging
from multiprocessing import Process


logging.basicConfig(level=logging.INFO)

token = "token"


async def main():

    user = User(token=token)

    # майним или решаем, или и то и то
    # await user.solve_forever()
    await user.mine_forever()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
