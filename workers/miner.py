import _hashlib

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

    async def solve_block(self, start: int, end: int, process_name: str):
        async with websockets.connect("wss://mining.rcx.at/") as websocket:
            hash_info: str = await websocket.recv()
            zero_value_start, hash_first = hash_info.split(":")

            i = 0
            for nonce in reversed(range(start, end)):
                to_hash: bytes = (hash_first + str(nonce)).encode()
                sha: _hashlib.HASH = hashlib.sha256(to_hash)

                if i == self.check_dict[zero_value_start]:
                    hash_info: str = await websocket.recv()
                    zero_value, hash_ = hash_info.split(":")
                    if hash_ != hash_first:
                        logging.info(f"process-{process_name}: Changed hash to {hash_}")
                        nonce = start
                        hash_first = hash_
                    if zero_value != zero_value_start:
                        logging.info(
                            f"process-{process_name}: Changed zero_value to {zero_value}"
                        )
                        zero_value_start = zero_value
                    i = 0

                if sha.hexdigest().startswith("0" * int(zero_value_start)):
                    r = await self.api_request("mining.send", params={"nonce": nonce})
                    logging.info(
                        f"process-{process_name}: Block found! Solve block status - {r}"
                    )
                    return r
                i += 1

    async def mine_forever(self, start: int, end: int, process_name: str):
        logging.info(f"process-{process_name}: Starting mining...")
        while True:
            try:
                await self.solve_block(start, end, process_name)
            except KeyboardInterrupt:
                exit(0)
            except Exception as e:
                logging.error(f"process-{process_name}: {e}")
                continue
