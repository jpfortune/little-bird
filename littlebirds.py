#!/usr/bin/env python3
import asyncio
import logging

from platforms.telegram import LBTelegramClient
logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)

from os import environ

async def pull_from_queue(queue):
    while True:
        msg = await queue.get()
        logging.info('dequeued: %s' % msg)
        await asyncio.sleep(0)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    queue = asyncio.Queue(loop=loop)

    client = LBTelegramClient(
        environ.get('TG_SESSION', 'session'),
        int(environ['TG_API_ID']),
        environ['TG_API_HASH'],
        loop,
        queue
    )
    consumer = pull_from_queue(queue)

    loop.run_until_complete(asyncio.gather(client.run(), consumer))
