#!/usr/bin/env python
import json
import sys
#import datetime

lastMsg = 0.00

while True:
   
    # load json on inbound stream
    line = sys.stdin.readline()
    d = json.loads(line)
    if lastMsg == 0.00:
        lastMsg = d["t"]
        continue

    #form time in between messages
    delta = d["t"] - lastMsg
    #_d1 = datetime.strptime(lastMsg, "%a %b %d %H:%M:%S %Y")
    #_d2 = datetime.strptime(d["t"], "%a %b %d %H:%M:%S %Y")
    #diff = _d2 - _d1
    #deltaSec = diff.seconds
    
    print json.dumps({"t":d["t"], "delta": delta})
    sys.stdout.flush()

    #update last message
    lastMsg = d["t"]
