#! /usr/bin/env python3

from decimal import Decimal as D
import simplejson as json
import matplotlib
import matplotlib.pyplot as plt

with open("./looplogs/zgetoperation_latent_success.py/zgetoperation_latent_success_4dbe0ef64e07caec2ba9d71776baf1ff6164f96f.log") as fh: 
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
    plt.savefig("20_aync_all_latencies.png")



