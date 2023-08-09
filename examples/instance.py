
## python examples/instance.py db0

import os
import argparse
import json
from pythonseer import Fediseer

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('-d', '--fediverse_domain', action='store', required=False, type=str, help="the fediverse instance domain for which to look up details")
args = arg_parser.parse_args()



fediverse_domain = args.fediverse_domain
if not fediverse_domain:
    fediverse_domain = os.getenv('FEDIVERSE_DOMAIN', "lemmy.dbzer0.com")
if not fediverse_domain:
    raise Exception("You need to provide a fediverse domain via env var or arg")

fediseer = Fediseer()
details = fediseer.whitelist.get_domain(fediverse_domain)
if details:
    print(json.dumps(details, indent=4))
else:
    print("Retrieval of instance details failed")
