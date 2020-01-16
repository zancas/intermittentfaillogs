#! /usr/bin/env python3

from decimal import Decimal as D
from pprint import pprint as pp
import simplejson as json
import sys
import matplotlib
import matplotlib.pyplot as plt
from pathlib import Path

class PathExtractor:
    def __init__(self, log_name):
        self.logpath = Path(log_name).absolute()
        self._extract_names()

    def _extract_names(self):
        self.log_base = self.logpath.parts[-1]
        self.test_name = self.logpath.parts[-2]
        self.core_name = self.log_base.rstrip(".log")
        self.log_data_ancestor =  self.logpath.parent.parent.parent 

class PathSetter:
    def __init__(self, pathextractor):
        self._construct_json_data_path(pathextractor)

    def _construct_json_data_path(self, pe):
        self.data_dirpath = pe.log_data_ancestor / "latencydata" / pe.test_name
        self.data_path = self.data_dirpath / Path( pe.core_name + ".json")

def plot(latencies):
    xs = range(len(latencies))
    ys = latencies
    plt.title("z_getoperationresult 'success' to z_listunspent latency")
    plt.ylabel('seconds')
    plt.xlabel('iteration')
    plt.plot(xs, ys, '.')
    plt.savefig("20_async_all_latencies.png")



def main():
    path_extractor = PathExtractor(sys.argv[1])
    paths = PathSetter(path_extractor)
    pp(paths.data_path)


if __name__ == '__main__':
    main()
