#!/usr/bin/env python3
# -*- coding: utf-8 -*-


print("datetime")
from datetime import datetime
now = datetime.now()
print("now: ", now, " time stamp: ", now.timestamp())
time = datetime(2000,1,1,12,30)
print(time, " time stamp: ", time.timestamp())
print("time stamp: ", now.timestamp(), " time: ", datetime.fromtimestamp(now.timestamp()))


print("\nbase64")
import base64
str = b"qwer"
b64 = base64.b64encode(str)
print("before base64: ", str, " after base64: ", b64)

import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
print("\nrequests")
import requests
r = requests.get("https://www.baidu.com")
print(r.status_code)
print(r.text)
