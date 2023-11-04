## python examples/suspicions.py db0

from pythonseer import Fediseer
from pythonseer.types import FormatType

fediseer = Fediseer()
suspicions = fediseer.suspicions.get(activity_suspicion=30, format=FormatType.LIST)
if suspicions:
    print(f"The following instances are considered suspicious {suspicions['domains']}")
else:
    print("Retrieval of suspicious instances failed")
