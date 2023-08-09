from typing import Any, List, Optional, Union

from pythonseer.requestor import Request, Requestor
from pythonseer.types import FormatType


class Whitelist:
    def __init__(self, _requestor: Requestor):
        self._requestor = _requestor

    def get(
        self,
        endorsements: int = 0,
        guarantors: int = 1,
        format: Optional[FormatType] = FormatType.FULL
    ) -> Optional[dict]:
        """
        Get complete fediseer whitelist
        Does not require to be logged-in

        Args:
            endorsements (Optional(int), optional): Defaults to 0
            guarantors (Optional(int), optional): Defaults to 1
            format (Optional[FormatType], optional): Defaults to FormatType.FULL.

        Returns:
            Optional[dict]: put data if successful
        """
        endpoint = f"/whitelist?endorsements={endorsements}&guarantors={guarantors}{format.get_query('&')}"
        return self._requestor.api(Request.GET, endpoint)

    def get_domain(
        self,
        domain: str,
    ) -> Optional[dict]:
        """
        Get fediseer domain info
        Does not require to be logged-in
        If logged-in, defaults to user's home domain

        Args:
            domain (str)

        Returns:
            Optional[dict]: put data if successful
        """
        return self._requestor.api(Request.GET, f"/whitelist/{domain}")

    def claim(
        self,
        domain: str,
    ) -> Optional[dict]:
        """
        Claim a domain
        Does not require to be logged-in

        Args:
            domain (str)

        Returns:
            Optional[dict]: put data if successful
        """
        return self._requestor.api(Request.PUT, f"/whitelist/{domain}")

    def unclaim(
        self,
        domain: str,
    ) -> Optional[dict]:
        """
        Delete a domain claim
        Requires to be logged-in

        Args:
            domain (str)

        Returns:
            Optional[dict]: delete data if successful
        """
        return self._requestor.api(Request.DELETE, f"/whitelist/{domain}")

    def reset_apikey(
        self,
        domain: str,
    ) -> Optional[dict]:
        """
        Resets the API key of an admin
        Requires to be logged-in

        Args:
            domain (str)

        Returns:
            Optional[dict]: delete data if successful
        """
        return self._requestor.api(Request.PATCH, f"/whitelist/{domain}")
