from typing import Any, List, Optional, Union

from pythonseer.requestor import Request, Requestor
from pythonseer.types import FormatType


class Hesitation:
    def __init__(self, _requestor: Requestor):
        self._requestor = _requestor

    def create(
        self,
        domain: str,
        reason: str = None,
        evidence: str = None,
    ) -> Optional[dict]:
        """
        Create a hesitation
        Requires to be logged-in

        Args:
            domain (str)
            reason (str), optional
            evidence (str), optional

        Returns:
            Optional[dict]: put data if successful
        """
        payload = {}
        if reason is not None:
            payload["reason"] = reason
        if evidence is not None:
            payload["evidence"] = evidence
        return self._requestor.api(Request.PUT, f"/hesitations/{domain}", json=payload)

    def modify(
        self,
        domain: str,
        reason: str = None,
        evidence: str = None,
    ) -> Optional[dict]:
        """
        modify a hesitation
        Requires to be logged-in

        Args:
            domain (str)
            reason (str), optional
            evidence (str), optional

        Returns:
            Optional[dict]: patch data if successful
        """
        payload = {}
        if reason is not None:
            payload["reason"] = reason
        if evidence is not None:
            payload["evidence"] = evidence
        return self._requestor.api(Request.PATCH, f"/hesitations/{domain}", json=payload)

    def delete(
        self,
        domain: str,
    ) -> Optional[dict]:
        """
        Withdraw a hesitation
        Requires to be logged-in

        Args:
            domain (str)

        Returns:
            Optional[dict]: delete data if successful
        """
        return self._requestor.api(Request.DELETE, f"/hesitations/{domain}")

    def get_received(self, domain: str = None, format: Optional[FormatType] = FormatType.FULL) -> Optional[dict]:
        """
        Retrieve hesitations received by specific domain
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
                raise Exception("Must provide a domain or login to GET /hesitations/ endpoint")
        endpoint = f"/hesitations/{domain}{format.get_query('?')}"
        return self._requestor.api(Request.GET, endpoint)

    def get_given(
        self,
        domain_set: set = None,
        reasons: set = None,
        min_hesitations: int = 1,
        format: Optional[FormatType] = FormatType.FULL,
    ) -> Optional[dict]:
        """
        Retrieve hesitations given out by specific domain
        Does not require to be logged-in
        If logged-in, defaults to user's home domain

        Args:
            domain_set (set or str), optional
            reasons (set or str), optional
            min_hesitations (int), optional
            format (Optional[FormatType], optional): Defaults to FormatType.FULL.

        Returns:
            Optional[dict]: get data if successful
        """
        if not domain_set:
            domain_csv = self._requestor.home_domain
            if not domain_csv:
                raise Exception("Must provide a domain or login to GET /hesitations_given/ endpoint")
        # Handle sending the domain name as str gracefully
        elif type(domain_set) is str:
            domain_csv = domain_set
        elif type(domain_set) is set:
            domain_csv = ",".join(domain_set)
        else:
            raise Exception("'domain' has to be a set or a string")
        reasons_query = ""
        if reasons is not None:
            if type(reasons) is str:
                reasons_csv = reasons
            else:
                reasons_csv = ",".join(reasons)
            reasons_query = f"&reasons_csv={reasons_csv}"
        endpoint = (
            f"/hesitations_given/{domain_csv}?min_hesitations={min_hesitations}{reasons_query}{format.get_query('&')}"
        )
        return self._requestor.api(Request.GET, endpoint)
