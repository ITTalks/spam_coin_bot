import aiohttp


class ApiBase:
    def __init__(self, token: str):
        self.session = aiohttp.ClientSession()
        self.token = token
        self.url = "https://coin.rcx.at/api/{}/{}"

    async def api_request(self, method, params=None):
        if params is None:
            params = {}
        async with self.session.get(
            self.url.format(self.token, method), params=params
        ) as response:
            resp = await response.text()
            return resp
