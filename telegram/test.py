#!/usr/bin/env python
import sqlite3
import os

from telethon import TelegramClient, events, sync

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.

session = os.environ.get("TG_SESSION", "printer")
api_id = get_env("TG_API_ID", "Enter your API ID: ", int)
api_hash = get_env("TG_API_HASH", "Enter your API hash: ")
proxy = None  # https://github.com/Anorov/PySocks


# This is our update handler. It is called when a new update arrives.
async def handler(update):
    print(update)


# Use the client in a `with` block. It calls `start/disconnect` automatically.
with TelegramClient(session, api_id, api_hash, proxy=proxy) as client:
    # Register the update handler so that it gets called
    client.add_event_handler(handler)

    # Run the client until Ctrl+C is pressed, or the client disconnects
    print("(Press Ctrl+C to stop this)")
    client.run_until_disconnected()
