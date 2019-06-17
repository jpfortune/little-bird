#!/usr/bin/env python
import os

from telethon import TelegramClient


class EnvironmentVariableNotSet(Exception):
    pass


class TG_Client(TelegramClient):
    def __init__(
        self,
        session=os.environ.get("TG_SESSION"),
        api_id=os.environ.get("TG_API_ID"),
        api_hash=os.environ.get("TG_API_HASH"),
        proxy=None,
    ):
        if session is None:
            raise EnvironmentVariableNotSet("TG_SESSION")

        if not os.path.isfile(session):
            raise FileNotFoundError("Session file not found.")

        self.client = TelegramClient(session, api_id, api_hash, proxy=proxy)

        self.client.add_event_handler(handler)

        # def get_telegram_client():
        # dialogs = client.get_dialogs()

        # for d in dialogs:
        #    if d.is_channel:
        #        print(f"{d.name}")
        #        pp(vars(d))

        # client.add_event_handler(handler)

        # print("(Press Ctrl+C to stop this)")
        # return client


async def handler(update):
    print(update)


if __name__ == "__main__":

    with TelegramClient() as client:
        client.disconnect()
