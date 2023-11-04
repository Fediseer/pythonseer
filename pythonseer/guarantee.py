from typing import Any, List, Optional, Union

from pythonseer.requestor import Request, Requestor
from pythonseer.types import FormatType


class Guarantee:
    def __init__(self, _requestor: Requestor):
        self._requestor = _requestor

    def create(
        self,
        domain: str,
    ) -> Optional[dict]:
        """
        Create a guarantee
        Requires to be logged-in

        Args:
            domain (str)

        Returns:
            Optional[dict]: put data if successful
        """
        return self._requestor.api(Request.PUT, f"/guarantees/{domain}")

    def delete(
        self,
        domain: str,
    ) -> Optional[dict]:
        """
        Withdraw a guarantee
        Requires to be logged-in

        Args:
            domain (str)

        Returns:
            Optional[dict]: delete data if successful
        """
        return self._requestor.api(Request.DELETE, f"/guarantees/{domain}")

    def get_received(self, domain: str = None, format: Optional[FormatType] = FormatType.FULL) -> Optional[dict]:
        """
        Retrieve guarantees received by specific domain
        Does not require to be logged-in
        If logged-in, defaults to user's home domain

        Args:
            domain (str)
            format (Optional[FormatType], optional): Defaults to FormatType.FULL.

        Returns:
            Optional[dict]: get data if successful
        """
        if not domain:
            domain = self._requestor.home_domain
            if not domain:
                raise Exception("Must provide a domain or login to GET /guarantees/ endpoint")
        endpoint = f"/guarantees/{domain}{format.get_query('?')}"
        return self._requestor.api(Request.GET, endpoint)

    def get_given(self, domain: set = None, format: Optional[FormatType] = FormatType.FULL) -> Optional[dict]:
        """
        Retrieve guarantees given out by specific domain
        Does not require to be logged-in
        If logged-in, defaults to user's home domain

        Args:
            domain_set (set)
            domains (str)
            format (Optional[FormatType], optional): Defaults to FormatType.FULL.

        Returns:
            Optional[dict]: get data if successful
        """
        if not domain:
            domain = self._requestor.home_domain
            if not domain:
                raise Exception("Must provide a domain or login to GET /guarantors/ endpoint")
        endpoint = f"/guarantors/{domain}{format.get_query('?')}"
        return self._requestor.api(Request.GET, endpoint)
