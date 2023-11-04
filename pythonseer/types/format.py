from enum import Enum, auto


class FormatType(Enum):
    FULL = auto()
    LIST = auto()
    CSV = auto()

    def get_query(self, query_join=""):
        if self == FormatType.FULL:
            return ""
        elif self == FormatType.LIST:
            return f"{query_join}domains=true"
        elif self == FormatType.CSV:
            return f"{query_join}csv=true"
