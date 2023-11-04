## python examples/censures.py db0

import argparse
import os

from pythonseer import Fediseer
from pythonseer.types import FormatType

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument(
    "-d",
    "--fediverse_domain",
    action="store",
    required=False,
    type=str,
    help="the fediverse instance domain for which to look up censures",
)
arg_parser.add_argument(
    "-m",
    "--min_hesitations",
    action="store",
    required=False,
    default=1,
    type=int,
    help="The min amount of hesitations to require for each instance",
)
arg_parser.add_argument(
    "-r", "--reasons", action="store", required=False, type=str, help="A csv of reasons with which to filter intances"
)
args = arg_parser.parse_args()


fediverse_domain = args.fediverse_domain
if not fediverse_domain:
    fediverse_domain = os.getenv("FEDIVERSE_DOMAIN", "lemmy.dbzer0.com,lemmings.world,lemmy.world")
if not fediverse_domain:
    raise Exception("You need to provide a fediverse domain via env var or arg")

fediseer = Fediseer()
hesitations = fediseer.hesitation.get_given(
    domain_set=fediverse_domain, reasons=args.reasons, min_hesitations=args.min_hesitations, format=FormatType.CSV
)
if hesitations:
    print(f"{fediverse_domain} has hesitated against the following instances: {hesitations['csv']}")
else:
    print("Retrieval of instance hesitations failed")
