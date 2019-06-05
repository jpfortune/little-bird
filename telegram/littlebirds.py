#!/usr/bin/env python3
import requests
import time
import json
from pprint import pprint as pp

url = "http://bridge:8000/records/"

data = {
    "posted": "2000-10-10 12:34:56",
    "author": "hollaholla",
    "platform": "yo momma",
    "keywords": ["icx", "ven", "xrp"],
}

while True:
    r = requests.post(url, data=json.dumps(data))
    pp(r)
    print("sleeping")
    time.sleep(5)

import argparse
import asyncio
import logging

from cruncher import Cruncher

from platforms.telegram import LBTelegramClient

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)

from os import environ

parser = argparse.ArgumentParser(
    description=("Calculate the TopN number of words seen in messages from " "Telegram")
)
parser.add_argument(
    "--lookback",
    dest="lookback",
    type=int,
    default=300,
    help="only keep words that have been seen in the last number of seconds",
)
parser.add_argument(
    "--print-interval",
    dest="print_interval",
    type=int,
    default=30,
    help="interval in seconds for periodic printing of the most common words",
)
parser.add_argument(
    "--crypto-only",
    dest="crypto_only",
    action="store_true",
    help="only check for crypto tickers pulled from coin market cap",
)
parser.add_argument(
    "--topn",
    dest="topn",
    type=int,
    default=25,
    help="print only the topn number words seen",
)

# TODO Fill in this place holder function
def get_tickers():
    return None


# TODO Add code to check for environment variables
if __name__ == "__main__":

    args = parser.parse_args()
    loop = asyncio.get_event_loop()
    queue = asyncio.Queue(loop=loop)

    check_set = None
    if args.crypto_only:
        check_set = get_tickers()

    cruncher = Cruncher(
        loop,
        queue,
        check_set=check_set,
        lookback=args.lookback,
        topn=args.topn,
        print_interval=args.print_interval,
    )

    client = LBTelegramClient(
        environ.get("TG_SESSION", "session"),
        int(environ["TG_API_ID"]),
        environ["TG_API_HASH"],
        loop,
        queue,
    )

    loop.run_until_complete(asyncio.gather(client.run(), cruncher.run()))

    loop.close()
