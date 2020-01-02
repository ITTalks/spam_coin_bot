from user import User
import asyncio
import sys
import logging

logging.basicConfig(level=logging.INFO)

token = "token"


async def main():
    user = User(token=token)

    # эта штука будет спамить на сервер рандомными nonce
    # await user.mine_forever_random(start=int(sys.argv[1]), end=int(sys.argv[2]), thread_name=int(sys.argv[3]))

    await user.mine_forever(start=int(sys.argv[1]),
                            end=int(sys.argv[2]),
                            thread_name=int(sys.argv[3]))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
