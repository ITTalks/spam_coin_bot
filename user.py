from workers.miner import Miner
from workers.solver import Solver
from workers.base_api import ApiBase
import logging


class User(ApiBase):
    def __init__(self, token: str):
        super().__init__(token)

    async def solve_forever(self):
        solver: Solver = Solver(token=self.token)
        await solver.solve_forever()

    async def mine_forever(self, start: int, end: int, thread_name: str):
        miner: Miner = Miner(token=self.token)
        await miner.mine_forever(start, end, thread_name)

    async def send_coin(self, user_id: int, amount: int):
        params = {"user_id": user_id, "amount": amount}
        r = await self.api_request("balance.transfer", params=params)
        logging.info(f"Balance sent with status {r}")
        return r

    async def get_balance(self):
        balance = await self.api_request("balance.get")
        return balance
