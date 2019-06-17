#!/usr/bin/env python
import time

from bridge_client import BridgeClient
from telegram_client import TG_Client


# url = "http://bridge:8000/records/"

# data = {
#    "posted": "2000-10-10 12:34:56",
#    "author": "hollaholla",
#    "platform": "yo momma",
#    "keywords": ["icx", "ven", "xrp"],
# }


SESSION = os.environ.get("TG_SESSION")
API_ID = os.environ.get("TG_API_ID")
API_HASH = os.environ.get("TG_API_HASH")


def main():
    try:
        tg_client = TG_Client()
        )
    except Exception:
        pass

    try:
        bc = BridgeClient("bridge")
    except Exception:
        pass

    # data = {
    #    "posted": "2000-10-10 12:34:56",
    #    "author": "hollaholla",
    #    "platform": "yo momma",
    #    "keywords": ["icx", "ven", "xrp"],
    # }

    data = bc.add_record(
        "2000-10-10 12:34:56", "holla4adolla", "twitgram", ["icx", "ven", "xrp"]
    )
    data = bc.add_record(
        "2000-10-10 12:34:56", "holla4adolla", "twitgram", ["icx", "ven", "xrp"]
    )
    data = bc.add_record(
        "2000-10-10 12:34:56", "holla4adolla", "twitgram", ["icx", "ven", "xrp"]
    )
    data = bc.add_channel(12345, "dummy_channel")
    print(f"{data.content}")

    while True:
        try:
            data = bc.get_channels()
            print(f"{data.content}")
        except Exception:
            pass
        time.sleep(10)


if __name__ == "__main__":
    main()
