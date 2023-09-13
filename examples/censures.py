
## python examples/censures.py db0

import os
import argparse
from pythonseer import Fediseer
from pythonseer.types import FormatType


arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('-d', '--fediverse_domain', action='store', required=False, type=str, help="the fediverse instance domain for which to look up censures")
args = arg_parser.parse_args()



fediverse_domain = args.fediverse_domain
if not fediverse_domain:
    fediverse_domain = os.getenv('FEDIVERSE_DOMAIN', "lemmy.dbzer0.com,lemmings.world,lemmy.world")
if not fediverse_domain:
    raise Exception("You need to provide a fediverse domain via env var or arg")

fediseer = Fediseer()
censures = fediseer.censure.get_given(fediverse_domain, FormatType.CSV)
if censures:
    print(f"{fediverse_domain} has censured the following instances: {censures['csv']}")
else:
    print("Retrieval of instance censures failed")
