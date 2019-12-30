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
    # await user.mine_forever()

    await user.mine_forever(processes_value=3)


def start():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())


if __name__ == '__main__':
    for _ in range(3):
        Process(target=start).start()
