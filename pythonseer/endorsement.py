from typing import Any, List, Optional, Union

from pythonseer.requestor import Request, Requestor
from pythonseer.types import FormatType


class Endorsement:
    def __init__(self, _requestor: Requestor):
        self._requestor = _requestor

    def create(
        self,
        domain: str,
    ) -> Optional[dict]:
        """
        Create an endorsement
        Requires to be logged-in

        Args:
            domain (str)

        Returns:
            Optional[dict]: put data if successful
        """
        return self._requestor.api(Request.PUT, f"/endorsements/{domain}")

    def delete(
        self,
        domain: str,
    ) -> Optional[dict]:
        """
        Withdraw an endorsements
        Requires to be logged-in

        Args:
            domain (str)

        Returns:
            Optional[dict]: delete data if successful
        """
        return self._requestor.api(Request.DELETE, f"/endorsements/{domain}")

    def get_received(
        self,
        domain: str = None,
        format: Optional[FormatType] = FormatType.FULL
    ) -> Optional[dict]:
        """
        Retrieve endorsements received by specific domain
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
                raise Exception("Must provide a domain or login to GET /endorsements/ endpoint")
        endpoint =  f"/endorsements/{domain}{format.get_query('?')}"
        return self._requestor.api(Request.GET, endpoint)

    def get_given(
        self,
        domain_set: set = None,
        format: Optional[FormatType] = FormatType.FULL
    ) -> Optional[dict]:
        """
        Retrieve censures given out by specific domain
        Does not require to be logged-in
        If logged-in, defaults to user's home domain

        Args:
            domain_set (set)
            domains (str)
            format (Optional[FormatType], optional): Defaults to FormatType.FULL.

        Returns:
            Optional[dict]: get data if successful
        """
        if not domain_set:
            domain_csv = self._requestor.home_domain
            if not domain_csv:
                raise Exception("Must provide a domain or login to GET /approvals/ endpoint")
        else:
            domain_csv = ','.join(domain_set)
        endpoint =  f"/approvals/{domain_csv}{format.get_query('?')}"
        return self._requestor.api(Request.GET, endpoint)
