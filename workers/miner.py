import random

from .base_api import ApiBase
import hashlib
import websockets
import logging


class Miner(ApiBase):
    def __init__(self, token: str):
        super().__init__(token)

        self.check_dict = {
            "3": 50000,
            "4": 100000,
            "5": 200000,
            "6": 500000,
            "7": 800000,
            "8": 1000000,
            "9": 1500000,
            "10": 2000000,
        }

    async def solve_block(self, start, end, thread_name):
        async with websockets.connect("wss://mining.rcx.at/") as websocket:
            hash_info = await websocket.recv()
            zero_value_start, hash_first = hash_info.split(":")

            i = 0
            for nonce in reversed(range(start, end)):
                to_hash = (hash_first + str(nonce)).encode()
                sha = hashlib.sha256(bytes(to_hash))

                if i == self.check_dict[zero_value_start]:
                    hash_info = await websocket.recv()
                    zero_value, hash_ = hash_info.split(":")
                    if hash_ != hash_first:
                        logging.info(f" thread-{thread_name}: Changed hash to {hash_}")
                        nonce = start
                        hash_first = hash_
                    if zero_value != zero_value_start:
                        logging.info(
                            f" thread-{thread_name}: Changed zero_value to {zero_value}"
                        )
                        zero_value_start = zero_value
                    i = 0

                if sha.hexdigest().startswith("0" * int(zero_value_start)):
                    r = await self.api_request("mining.send", params={"nonce": nonce})
                    logging.info(f"{thread_name} Block found! Solve block status - {r}")
                    return r
                i += 1

    async def mine_forever(self, start, end, thread_name):
        logging.info(f"thread-{thread_name}: Starting mining...")
        while True:
            try:
                await self.solve_block(start, end, thread_name)
            except KeyboardInterrupt:
                exit(0)
            except Exception as e:
                logging.error(f"thread-{thread_name}: {e}")
                continue

    async def mine_forever_random(self, start, end, thread_name):
        logging.info(f"thread-{thread_name}: Starting random mining...")
        while True:
            try:
                nonce = random.randint(start, end)
                r = await self.api_request("mining.send", params={"nonce": nonce})
                if r == "ok":
                    logging.info(f"{thread_name}: Block found! Solve block status - {r}")
            except KeyboardInterrupt:
                exit(0)
            except Exception as e:
                logging.error(f"thread-{thread_name}: {e}")
                continue
