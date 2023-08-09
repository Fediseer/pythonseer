
## python examples/user.py db0

import os
import argparse
import json
from pythonseer import Fediseer
from pythonseer.types import FormatType


pythonseer = Fediseer()
suspicions = pythonseer.suspicions.get(
    activity_suspicion=30,
    format=FormatType.LIST
)
if suspicions:
    print(f"The following instances are considered suspicious {suspicions}")
else:
    print("Retrieval of suspicious instances failed")
