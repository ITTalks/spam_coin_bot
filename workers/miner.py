from .base_api import ApiBase
import hashlib
import websockets
import logging


class Miner(ApiBase):
    def __init__(self, token: str):
        super().__init__(token)

    @staticmethod
    async def get_hash():
        async with websockets.connect("wss://mining.rolang.site/") as websocket:
            hash_ = await websocket.recv()
            return hash_

    async def solve_block(self, start):
        hash_ = await self.get_hash()

        for nonce in range(start, 2 ** 64):
            to_hash = (hash_ + str(nonce)).encode()
            sha = hashlib.sha256(bytes(to_hash))

            if sha.hexdigest().startswith("000000"):
                r = await self.api_request("mining.send", params={"nonce": nonce})
                logging.info(f"Block found! Solve block status - {r}")
                return r

    async def mine_forever(self, processes_value):
        logging.info(f"Starting mining in {processes_value} processes")
        while True:
            step = (2 ** 64) // processes_value

            for proc in range(1, processes_value):
                start = step * proc
                await self.solve_block(start)
