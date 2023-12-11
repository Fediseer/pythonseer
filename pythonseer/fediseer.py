import logging
import time
from typing import Any, Optional

from pythonseer.censure import Censure
from pythonseer.endorsement import Endorsement
from pythonseer.guarantee import Guarantee
from pythonseer.hesitation import Hesitation
from pythonseer.requestor import Request, Requestor
from pythonseer.suspicions import Suspicions
from pythonseer.whitelist import Whitelist

logger = logging.getLogger(__name__)


class Fediseer:
    _requestor: Requestor

    def __init__(self, api_base_url: str = "https://fediseer.com") -> None:
        self._requestor = Requestor()
        self._requestor.set_fediseer_domain(api_base_url)
        self.censure = Censure(self._requestor)
        self.hesitation = Hesitation(self._requestor)
        self.endorsement = Endorsement(self._requestor)
        self.guarantee = Guarantee(self._requestor)
        self.suspicions = Suspicions(self._requestor)
        self.whitelist = Whitelist(self._requestor)

    def log_in(self, apikey: str) -> bool:
        return self._requestor.log_in(apikey)
