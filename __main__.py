from user import User
import asyncio

token = "token"


async def main():
    user = User(token=token)

    # майним или решаем, или и то и то
    # await user.solve_forever()
    # await user.mine_forever()

    await user.mine_and_solve_forever()


if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
