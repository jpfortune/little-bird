#!/usr/bin/env python
import argparse
import json
import os
import requests
import time

import sqlite3
from pprint import pprint as pp

from telethon import TelegramClient, events, sync

session = os.environ.get("TG_SESSION")
api_id = os.environ.get("TG_API_ID")
api_hash = os.environ.get("TG_API_HASH")
proxy = None


class TG_Client(TelegramClient):
    def __init__(self, session, api_id, api_hash, proxy=None):
        self.client = TelegramClient(session, api_id, api_hash, proxy=proxy)
