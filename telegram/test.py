#!/usr/bin/env python
import asyncio
import logging
import os
import re
import time

from bridge_client import BridgeClient
from telegram_client import TG_Client

WORD_REGEX = re.compile("(\w{3,})+")
# words = re.findall(WORD_REGEX, msg)

logging.basicConfig(level=logging.INFO)


class Worker:
    def __init__(self, loop, queue, bridge_client=BridgeClient("bridge")):
        self._loop = loop
        self._queue = queue
        self.bridge_client = bridge_client

    async def run(self):
        # asyncio.ensure_future(self.process_message_queue())
        while True:
            try:
                raw_message = await self._queue.get()
            except Exception:
                logging.exception("Error while processing queue")

            logging.info("Parsing: %s" % raw_message)

            # TODO Should we compile the regex for speed gains?
            # TODO Maybe it's faster if we compiled a regex of everything in
            # self.check_set
            words = re.findall(WORD_REGEX, raw_message.message)
            logging.info("Words Parsed: %s" % words)
            if words:
                self.bridge_client.add_record(
                    "2000-10-10 12:34:56", "holla4adolla", "telegram", words
                )

    async def process_message_queue(self):
        while True:
            try:
                msg = await self._queue.get()
            except Exception:
                logging.exception("Error while processing queue")

            logging.info("Parsing: %s" % msg)

            # TODO Should we compile the regex for speed gains?
            # TODO Maybe it's faster if we compiled a regex of everything in
            # self.check_set
            words = re.findall(WORD_REGEX, msg.message)
            # may need to figure things out depending on the timezone
            # information of the message
            posted = msg.date.strftime("%Y-%m-%d, %H:%M:%S")

            # TODO create look ups tasks (perhaps this could be celery beat
            # server side
            author = "na"
            if msg.from_id:
                author = str(msg.from_id)

            logging.info("Words Parsed: %s" % words)
            await self.bridge_client.add_record(
                posted, author, "telegram", words
            )


def main():
    loop = asyncio.get_event_loop()
    queue = asyncio.Queue(loop=loop)

    worker = Worker(loop, queue)

    tg_client = TG_Client(loop, queue)

    loop.run_until_complete(asyncio.gather(tg_client.run(), worker.run()))

    loop.close()


if __name__ == "__main__":
    main()
