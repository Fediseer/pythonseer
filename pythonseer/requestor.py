import logging
from enum import Enum
from typing import Optional

import requests

logger = logging.getLogger(__name__)


class Request(Enum):
    GET = "GET"
    PUT = "PUT"
    POST = "POST"
    DELETE = "DELETE"
    PATCH = "PATCH"


REQUEST_MAP = {
    Request.GET: requests.get,
    Request.PUT: requests.put,
    Request.POST: requests.post,
    Request.DELETE: requests.delete,
    Request.PATCH: requests.patch,
}


class Requestor:
    fediseer_domain: Optional[str] = None
    headers: Optional[str] = None
    api_url: Optional[str] = None
    home_domain: Optional[str] = None

    def __init__(self):
        self.headers = {
            "Client-Agent": "pythonseer:0.1:@db0@lemmy.dbzer0.com",
        }

    def set_api_base_url(self, base_url: str) -> None:
        self.api_url = f"{base_url}/api/v1"

    def set_fediseer_domain(self, domain: str):
        self.fediseer_domain = domain
        self.set_api_base_url(self.fediseer_domain)
        try:
            req = requests.get(f"{self.fediseer_domain}/api", headers=self.headers, timeout=2)
        except Exception as err:
            logger.error(f"Could not reach expected Fediseer instance URL: {err}")
            return
        logger.info(f"Connected successfully to Fediseer {self.fediseer_domain}")

    def api(self, method: Request, endpoint: str, **kwargs) -> Optional[dict]:
        logger.info(f"Requesting API {method} {endpoint}")
        try:
            r = REQUEST_MAP[method](f"{self.api_url}{endpoint}", headers=self.headers, **kwargs)
        except Exception as err:
            logger.error(f"Error encountered while {method} on endpoint {endpoint}: {err}")
            return
        if not r.ok:
            logger.error(f"Error encountered while {method} on endpoint {endpoint}: {r.text}")
            return
        return r.json()

    def log_in(self, api_key: str) -> bool:
        self.headers["apikey"] = api_key
        login_req = self.api(Request.POST, "/find_instance", timeout=3)
        if not login_req.ok:
            return False
        self.home_domain = login_req["domain"]
        return True

    def log_out(self) -> None:
        del self.headers["apikey"]
