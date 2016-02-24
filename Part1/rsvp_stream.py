#!/usr/bin/env python
import json
import requests
import time
import sys

#copy list of imports from 
# "https://github.com/mikedewar/RealTimeStorytelling/blob/master/1/monitor-NYT-citibikes.py"
# I found this site with a similar project regarding RSVPs: 
# http://www.markhneedham.com/blog/2015/11/28/python-parsing-a-json-http-chunking-stream/
#while True:
#        r = requests.get("http://stream.meetup.com/2/rsvps")
#	print json.loads(r)
#	#json.dumps({"t": r.json()["mtime"]})
#	sys.stdout.flush()
	
r = requests.get('http://stream.meetup.com/2/rsvps', stream=True)
for line in r.iter_lines():
    event = json.loads(line)
    print json.dumps({"t": time.time()})
    sys.stdout.flush()
    time.sleep(2)
