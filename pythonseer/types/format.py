from enum import Enum, auto


class FormatType(Enum):
    FULL = auto()
    LIST = auto()
    CSV = auto()

    @classmethod
    def get_query(cls, query_join=''):
        if cls == cls.FULL:
            return ""
        elif cls == cls.LIST:
            return f"{query_join}domains=true"
        elif cls == cls.CSV:
            return f"{query_join}csv=true"
