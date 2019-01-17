#!/usr/bin/env python3
from os import environ

from telethon import TelegramClient

async def update_handler(update):
    print(update)

def main():
    client = TelegramClient(
        environ.get('TG_SESSION', 'session'),
        int(environ['TG_API_ID']),
        environ['TG_API_HASH'],
        proxy=None
    ).start()
    
    client.add_event_handler(update_handler)

    with client:
        client.run_until_disconnected()

if __name__ == "__main__":
    main()
