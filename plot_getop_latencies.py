#! /usr/bin/env python3

from decimal import Decimal as D
import simplejson as json
import sys
import matplotlib
import matplotlib.pyplot as plt
from pathlib import Path

run_path = Path(sys.argv[1])
with open(run_path) as fh: 
    for l in fh.readlines():
        if l.startswith("[Decimal('"):
            lstring = l.replace("Decimal(", "").replace(")", "")
            break

    lstring = lstring.replace("'", '"')
    latencies = list(map(D, json.loads(lstring)))
    print(len(latencies))
    print(sum(latencies)/len(latencies))
    xs = range(len(latencies))
    ys = latencies
    plt.title("z_getoperationresult 'success' to z_listunspent latency")
    plt.ylabel('seconds')
    plt.xlabel('iteration')
    plt.plot(xs, ys, '.')
    plt.savefig("20_async_all_latencies.png")



