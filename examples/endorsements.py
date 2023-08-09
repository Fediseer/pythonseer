
## python examples/endorsements.py db0

import os
import argparse
from pythonseer import Fediseer
from pythonseer.types import FormatType


arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('-d', '--fediverse_domain', action='store', required=False, type=str, help="the fediverse instance domain for which to look up endorsements")
args = arg_parser.parse_args()



fediverse_domain = args.fediverse_domain
if not fediverse_domain:
    fediverse_domain = os.getenv('FEDIVERSE_DOMAIN', "lemmy.dbzer0.com")
if not fediverse_domain:
    raise Exception("You need to provide a fediverse domain via env var or arg")

fediseer = Fediseer()
endorsements = fediseer.endorsement.get_received(fediverse_domain, FormatType.LIST)
if endorsements:
    print(f"{fediverse_domain} has been endorsed by the following instances: {endorsements['domains']}")
else:
    print("Retrieval of instance endorsements failed")
