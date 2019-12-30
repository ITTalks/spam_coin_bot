from user import User
import asyncio
import logging
from multiprocessing import Process


logging.basicConfig(level=logging.INFO)

token = "token"


async def main(start_, end_):

    user = User(token=token)

    # майним или решаем, или и то и то
    # await user.solve_forever()
    # await user.mine_forever()

    await user.mine_forever(start_, end_)


def start(start_, end_):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(start_, end_))


if __name__ == '__main__':
    processes = 3

    step = 2**64 // processes

    for proc in range(processes):
        start__ = step * proc
        end__ = step * (proc+1)
        Process(target=start, args=(start__, end__)).start()
