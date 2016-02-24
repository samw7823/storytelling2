import time
import json
import sys
import numpy

while True:

    print json.dumps({"t":time.time()})
    sys.stdout.flush()

    delta_t = numpy.random.exponential(2)

    
    time.sleep(delta_t)
