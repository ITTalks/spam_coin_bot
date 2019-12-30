from .base_api import ApiBase


class Solver(ApiBase):
    def __init__(self, token):
        super().__init__(token)

    async def solve_one(self):
        expr = await self.api_request(method="solve.get")
        result = int(eval(expr))

        params = {"result": result}

        resp = await self.api_request(method="solve.send", params=params)
        print(resp)
        return resp

    async def solve_forever(self):
        while True:
            await self.solve_one()
