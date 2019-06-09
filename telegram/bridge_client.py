#!/usr/bin/env python
import logging
import requests
import time


ROUTES = {
    "channels": "/telegram/",
    "records": "/records/",
    "theroute": "/telegram/{x}/",
}


class BridgeServerError(Exception):
    pass


class BridgeClient(object):
    def __init__(self, host, port=8000, max_retries=5):
        self.host = host
        self.port = port
        self.url = f"http://{self.host}:{self.port}"
        self.max_retries = max_retries

        self.is_lively()

    def is_lively(self):
        """
        Check if the server is lively
        """
        attempts = 0
        while attempts < self.max_retries:
            try:
                requests.get(self.url)
                return
            except Exception as e:
                attempts += 1
                error = e
                time.sleep(5)
        raise BridgeServerError(error)

    def _get(self, path, **kwargs):
        """
        Wrapper around requests.get
        """
        url = f"{self.url}{path}"
        for _ in range(self.max_retries):
            try:
                return requests.get(url, **kwargs)
            except requests.ConnectionError as e:
                logging.error(
                    "could not establish connection to %s: %s" % (url, str(e))
                )
                continue
            else:
                break
        else:
            raise BridgeServerError(
                "hit max amount of retries, could not execute method %s" % url
            )

    def _post(self, path, **kwargs):
        """
        Wrapper around requests.post
        """
        url = f"{self.url}{path}"
        for _ in range(self.max_retries):
            try:
                return requests.post(url, **kwargs)
            except requests.ConnectionError as e:
                logging.error(
                    "could not establish connection to %s: %s" % (url, str(e))
                )
                continue
            else:
                break
        else:
            raise BridgeServerError(
                "hit max amount of retries, could not execute method %s" % url
            )

    def _delete(self, path, **kwargs):
        """
        Wrapper around requests.delete
        """
        url = f"{self.url}{path}"
        for _ in range(self.max_retries):
            try:
                return requests.delete(url, **kwargs)
            except requests.ConnectionError as e:
                logging.error(
                    "could not establish connection to %s: %s" % (url, str(e))
                )
                continue
            else:
                break
        else:
            raise BridgeServerError(
                "hit max amount of retries, could not execute method %s" % url
            )

    def get_channels(self):
        return self._get(ROUTES["channels"])

    def add_channel(self, channel_id, name):
        "Adds a channel to the database"
        return self._post(
            ROUTES["channels"], json={"channel_id": channel_id, "name": name}
        )

    def add_record(self, posted, author, platform, keywords):
        return self._post(
            ROUTES["records"],
            json={
                "posted": posted,
                "author": author,
                "platform": platform,
                "keywords": keywords,
            },
        )

    def sample_post_URL_DATA(self, x, y, z):
        return self._post(ROUTES["theroute"].format(x=x), json={"y": y, "z": z})
