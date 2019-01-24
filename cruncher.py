import asyncio
import logging
import collections
import re
import time

from datetime import datetime, timedelta

WORD_REGEX = re.compile("(\w{3,})+")

class Cruncher():
    def __init__(self, loop, queue, check_set=None):
        self._queue = queue
        self._loop = loop

        self.check_set = check_set
        self.counter = collections.Counter()
        self.all_words = WordList()
        self.lookback = 180

    async def sweep(self):
        while True:
            print("Sweeping >")
            time = datetime.now() - timedelta(seconds=self.lookback)
            while (self.all_words.head and time > self.all_words.head.time):
                # if there are too many words to behead we may need to add
                # an async sleep
                word = self.all_words.behead()

                # This cuases a bug where some words have counts of less than 1
                # if self.counter[word] == 1:
                if self.counter[word] <= 1:
                    # without try/except a keyerror can occur
                    try:
                        self.counter.pop(word)
                        print("removed from queue: %s" % word)
                    except KeyError:
                        pass
                else:
                    self.counter[word] -= 1

            await asyncio.sleep(30)

    async def process_message_queue(self):
        while True:
            raw_message = await self._queue.get()
            logging.info('dequeued: %s' % raw_message)

            #TODO Should we compile the regex for speed gains?
            #TODO Maybe it's faster if we compiled a regex of everything in
            # self.check_set
            out = []
            words = re.findall(WORD_REGEX, raw_message)

            if self.check_set:
                for word in words:
                    if word.lower() in self.check_set:
                        self.all_words.append(word.lower())
                        self.counter[word] += 1

            else:
                for word in words:
                    if word:
                        self.all_words.append(word.lower())
                        self.counter[word] += 1

            print("Words: {}".format(words))

    async def periodic_print(self):
        while True:
            print("Current Snapshot")
            for word in self.counter.most_common():
                print(word)
            await asyncio.sleep(30)


class _Node():
    def __init__(self, word, next=None):
        self.time = datetime.now()
        self.word = word
        self.next = next


class WordList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def print(self):
        current = self.head
        while current:
            print("{} - {}".format(current.time, current.word))
            current = current.next

    def append(self, word):
        new_node = _Node(word)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def behead(self):
        if self.head == None:
            return
        word = self.head.word
        self.head = self.head.next
        self.length -= 1
        return word
