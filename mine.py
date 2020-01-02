from user import User
import asyncio
import sys
import logging

logging.basicConfig(level=logging.INFO)


start, end, thread_name, token = (
    int(sys.argv[1]),
    int(sys.argv[2]),
    int(sys.argv[3]),
    sys.argv[4],
)


async def main():
    user = User(token=token)

    await user.mine_forever(start=start, end=end, thread_name=thread_name)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
