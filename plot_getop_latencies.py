#! /usr/bin/env python3

from decimal import Decimal as D
import simplejson as json
import sys
import matplotlib
import matplotlib.pyplot as plt
from pathlib import Path

def plot(latencies):
    xs = range(len(latencies))
    ys = latencies
    plt.title("z_getoperationresult 'success' to z_listunspent latency")
    plt.ylabel('seconds')
    plt.xlabel('iteration')
    plt.plot(xs, ys, '.')
    plt.savefig("20_async_all_latencies.png")

def _extract_latency_data(latency_data):
    lstring = lstring.replace("'", '"')
    latencies = list(map(D, json.loads(lstring)))
    print(len(latencies))
    print(sum(latencies)/len(latencies))
    plot(latencies)

def _extract_names(run_path):
    run_log = run_path.parts[-1]

def main():
    run_path = Path(sys.argv[1])


if __name__ == '__main__':
    main()
