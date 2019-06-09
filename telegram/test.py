#!/usr/bin/env python
import time

from bridge_client import BridgeClient


# url = "http://bridge:8000/records/"

# data = {
#    "posted": "2000-10-10 12:34:56",
#    "author": "hollaholla",
#    "platform": "yo momma",
#    "keywords": ["icx", "ven", "xrp"],
# }


# def get_telegram_client():
#    dialogs = client.get_dialogs()
#
#    for d in dialogs:
#        if d.is_channel:
#            print(f"{d.name}")
#            pp(vars(d))
#
#    client.add_event_handler(handler)
#    return client
#
#    print("(Press Ctrl+C to stop this)")
#    return client

# async def handler(update):
#    print(update)


def main():
    # client = TG_Client(session, api_id, api_hash, proxy=proxy)
    bc = BridgeClient("bridge")

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
