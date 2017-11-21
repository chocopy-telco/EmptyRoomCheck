from django.shortcuts import render
from django.conf import settings
from functools import reduce
from redis import StrictRedis
from redis_collections import List

import os


def index(request):
    ip = getattr(settings, 'RS_HOST', 'localhost')
    port = getattr(settings, 'RS_PORT', 'def_port')
    pw = getattr(settings, 'RS_PASSWORD', 'def_password')
    redis_connection = StrictRedis(host=ip, port=port, db=0, password=pw)
    r = List(redis=redis_connection, key="rp3:00000000448f5428")

    latest_val = r[-60:-1]  # last 60 sec
    latest_val.sort()
    middle_val = latest_val[20:40]  # middle of value
    avg_val = reduce(lambda x, y: x + y, middle_val) / len(middle_val)
    # is_empty = False if avg_val < 1800 else True
    is_empty = False if avg_val < 2200 else True
    print(avg_val, is_empty)
 
    context = {
        'is_empty': is_empty,
        'avg': avg_val,
    }
    return render(request, 'index.html', context)
