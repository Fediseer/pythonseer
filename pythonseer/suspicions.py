from typing import Any, List, Optional, Union

from pythonseer.requestor import Request, Requestor
from pythonseer.types import FormatType


class Suspicions:
    def __init__(self, _requestor: Requestor):
        self._requestor = _requestor

    def get(
        self, activity_suspicion: int = 20, active_suspicion: int = 500, format: Optional[FormatType] = FormatType.FULL
    ) -> Optional[dict]:
        """
        Get complete fediseer suspicions list
        Does not require to be logged-in

        Args:
            domain (str)
            activity_suspicion (Optional(int), optional): Defaults to 20
            active_suspicion (Optional(int), optional): Defaults to 500
            format (Optional[FormatType], optional): Defaults to FormatType.FULL.

        Returns:
            Optional[dict]: put data if successful
        """
        endpoint = f"/instances?activity_suspicion={activity_suspicion}&active_suspicion={active_suspicion}{format.get_query('&')}"
        return self._requestor.api(Request.GET, endpoint)
