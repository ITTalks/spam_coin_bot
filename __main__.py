import asyncio


token = "token"
process_value = 10


async def start():
    for i in range(process_value):

        start_ = ((2 ** 64) // process_value) * i
        end = ((2 ** 64) // process_value) * (i + 1)

        if i == process_value - 1:
            p = await asyncio.subprocess.create_subprocess_shell(
                f"python mine.py {start_} {end} {i} {token}"
            )
            await p.wait()

        else:
            await asyncio.subprocess.create_subprocess_shell(
                f"python mine.py {start_} {end} {i} {token}"
            )


if __name__ == "__main__":
    loop = asyncio.ProactorEventLoop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(start())
