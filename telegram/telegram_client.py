#!/usr/bin/env python
import asyncio
import logging

import os
import re

from telethon import TelegramClient


class EnvironmentVariableNotSet(Exception):
    pass


class UserNotAuthorized(Exception):
    pass


class TG_Client(TelegramClient):
    def __init__(
        self,
        loop,
        queue,
        session=os.environ.get("TG_SESSION"),
        api_id=os.environ.get("TG_API_ID"),
        api_hash=os.environ.get("TG_API_HASH"),
        proxy=None,
    ):
        if session is None:
            raise EnvironmentVariableNotSet("TG_SESSION")

        if not os.path.isfile(session + ".session"):
            raise FileNotFoundError("Session file not found.")

        super().__init__(session, api_id, api_hash, loop=loop, proxy=proxy)
        logging.info("Connecting to Telegram servers...")

        # self._loop = loop
        self._message_queue = queue

        try:
            self._loop.run_until_complete(self.connect())
        except ConnectionError:
            logging.warning("Initial connection failed. Retrying...")
            self._loop.run_until_complete(self.connect())

        if not self._loop.run_until_complete(self.is_user_authorized()):
            raise UserNotAuthorized()

        logging.info("Connected to Telegram servers.")

    async def run(self):
        self.add_event_handler(self.update_handler)
        while True:
            await asyncio.sleep(5)

    async def update_handler(self, update):
        try:
            msg = update.message
        except AttributeError:
            return

        if msg.message is None or len(msg.message) == 0:
            return

        logging.debug(f"Message received: {msg}")
        await self._message_queue.put(msg)

        # def get_telegram_client():
        # dialogs = client.get_dialogs()

        # for d in dialogs:
        #    if d.is_channel:
        #        print(f"{d.name}")
        #        pp(vars(d))

        # client.add_event_handler(handler)

        # print("(Press Ctrl+C to stop this)")
        # return client


if __name__ == "__main__":
    session = os.environ.get("TG_SESSION")
    api_id = os.environ.get("TG_API_ID")
    api_hash = os.environ.get("TG_API_HASH")

    # TODO Add some error halding here
    with TelegramClient(session, api_id, api_hash) as client:
        client.disconnect()
