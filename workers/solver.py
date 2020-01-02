from .base_api import ApiBase
import logging


class Solver(ApiBase):
    def __init__(self, token: str):
        super().__init__(token)

    async def solve_one(self):
        expr = await self.api_request(method="solve.get")
        result = int(eval(expr))

        params = {"result": result}

        resp = await self.api_request(method="solve.send", params=params)
        logging.info(f"Solved! Solve status - {resp}")
        return resp

    async def solve_forever(self):
        logging.info("Starting solving...")
        while True:
            await self.solve_one()
