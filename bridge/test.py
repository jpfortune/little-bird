#!/usr/bin/env python
# import django
# import sys
# from pprint import pprint as pp
#
# django.setup()
#
# from api.serializers import RecordSerializer, KeywordListSerializer
# from api.models import Record
#
# data = {
#    "posted": "2000-10-10 12:34:56",
#    "author": "hollaholla",
#    "platform": "yo momma",
#    "keywords": ["icx", "ven", "xrp"],
# }
#
# s = RecordSerializer(data=data)
#
# if not s.is_valid():
#    print(f"Try again: {s.errors}")
#    sys.exit(0)
#
# s.save()
#
# print("WE GUCCI")
#
# for r in Record.objects.all():
#    cereal = RecordSerializer(r)
#    print(cereal.data)
# x = KeywordListSerializer()
# y = RecordSerializer()
# print(repr(x))
# print(repr(y))
# import code
#
# code.interact(local=locals())

import code
import django

django.setup()
from api.tasks import add

code.interact(local=locals())
