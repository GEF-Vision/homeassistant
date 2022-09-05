import httpx
import logging


class VisionAuthenticationError(Exception):
    pass


class VisionConnectionError(Exception):
    pass


class VisionClient(object):
    def __init__(
        self, username: str, password: str, plant: str, url: str = "vision.gef.fi"
    ):
        self.username = username
        self.password = password
        self.api = url
        self.token = None
        self.log = logging.getLogger(self.__class__.__name__)
        self.plant = plant
        self.client = httpx.AsyncClient()

    def get_api_url(self, endpoint: str):
        return f"https://{self.api}/api/v2/{endpoint}"

    def get_headers(self):
        return {"Authorization": f"Token {self.token}"}

    async def get_permissions(self):
        r = await self.client.get(
            self.get_api_url(f"plant/{self.plant}/permission/"),
            headers=self.get_headers(),
        )
        if r.status_code == 200:
            self.permissions = r.json()
            return True
        else:
            raise RuntimeError("Request failed")

    async def authenticate(self):
        data = {"username": self.username, "password": self.password}
        try:
            r = await self.client.post(self.get_api_url("auth/token/"), json=data)
        except httpx.RequestError as err:
            raise VisionConnectionError("Request failed") from err
        if r.status_code == 200:
            self.token = r.json().get("token", "")
            return True
        else:
            raise VisionAuthenticationError("Authentication failed")

    async def fetch_plant(self, uuid: str):
        if not self.token:
            raise ValueError("Not authenticated")
        r = await self.client.get(
            self.get_api_url(f"plant/{uuid}/"), headers=self.get_headers()
        )
        if r.status_code == 200:
            return r.json()
        else:
            raise VisionConnectionError("Request failed")

    async def get_capabilities(self, uuid: str):
        if not self.token:
            raise ValueError("Not authenticated")
        r = await self.client.get(
            self.get_api_url(f"plant/{uuid}/"), headers=self.get_headers()
        )
        if r.status_code == 200:
            print(r.json())
            return {
                "has_energymeter": True if r.json().get("consumption", None) else False,
                "has_production": True if r.json().get("production", None) else False,
            }
        else:
            raise VisionConnectionError("Request failed")
