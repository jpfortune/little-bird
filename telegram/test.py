#!/usr/bin/env python
import asyncio
import logging
import os
import re
import time

from bridge_client import BridgeClient
from telegram_client import TG_Client

WORD_REGEX = re.compile("(\w{2,})+")

logging.basicConfig(level=logging.INFO)


class Worker:
    def __init__(self, loop, queue, bridge_client, check_set=None):
        self._loop = loop
        self._queue = queue
        self.bridge_client = bridge_client
        self.check_set = check_set

    async def run(self):
        # asyncio.ensure_future(self.process_message_queue())
        logging.debug(f"Check Set: {self.check_set}")
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
            out = []
            if words:
                logging.info(f"Words: {words}")
                for word in words:
                    if word.lower() in self.check_set:
                        out.append(word.lower())
                # out = [word.lower() for word in words if word.lower() in self.check_set]
                logging.info(f"Parsed: {out}")

            if out:
                posted = msg.date.strftime("%Y-%m-%d %H:%M:%S")

                # TODO create look ups tasks (perhaps this could be celery beat
                # server side
                author = "na"
                if msg.from_id:
                    author = str(msg.from_id)

                self.bridge_client.add_record(posted, author, "telegram", out)


def main():
    check_set = set()
    with open("cryptos.txt") as f:
        for word in f.readlines():
            check_set.add(word.strip().lower())

    loop = asyncio.get_event_loop()
    queue = asyncio.Queue(loop=loop)

    bc = BridgeClient("bridge")

    worker = Worker(loop, queue, bc, check_set=check_set)

    tg_client = TG_Client(loop, queue)

    loop.run_until_complete(asyncio.gather(tg_client.run(), worker.run()))

    loop.close()


if __name__ == "__main__":
    main()
