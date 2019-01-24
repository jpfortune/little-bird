#!/usr/bin/env python3
import asyncio
import logging

from cruncher import Cruncher

from platforms.telegram import LBTelegramClient
logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)

from os import environ


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    queue = asyncio.Queue(loop=loop)
    cruncher = Cruncher(loop, queue)

    client = LBTelegramClient(
        environ.get('TG_SESSION', 'session'),
        int(environ['TG_API_ID']),
        environ['TG_API_HASH'],
        loop,
        queue
    )

    loop.run_until_complete(asyncio.gather(
        client.run(),
        cruncher.sweep(),
        cruncher.process_message_queue(),
        cruncher.periodic_print()
    ))
