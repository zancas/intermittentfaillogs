#! /usr/bin/env python3

from decimal import Decimal as D
from pprint import pprint as pp
import simplejson as json
import sys
import matplotlib
import matplotlib.pyplot as plt
from pathlib import Path

class PathExtracts:
    def __init__(self, log_name):
        self.logpath = Path(log_name).absolute()
        self._extract_names()

    def _extract_names(self):
        self.log_base = self.logpath.parts[-1]
        self.test_name = self.logpath.parts[-2]
        self.core_name = self.log_base.rstrip(".log")
        self.log_data_ancestor =  self.logpath.parent.parent.parent 

class PathResults:
    def __init__(self, pathextractor):
        self.pathextractor = pathextractor
        self._construct_json_data_path(pathextractor)

    def _construct_json_data_path(self, pe):
        self.data_dirpath = pe.log_data_ancestor / "latencydata" / pe.test_name
        self.data_path = self.data_dirpath / Path( pe.core_name + ".json")


def _set_plot_labels_title():
    plt.title("z_getoperationresult 'success' to z_listunspent latency")
    plt.ylabel('seconds')
    plt.xlabel('iteration')

def plot_datavector(latencies, pathextractor, symbol):
    xs = range(len(latencies))
    ys = latencies
    plt.plot(xs, ys, symbol)

def extract_latencies(logpath):
    lines = open(logpath).readlines()
    tagindex = lines.index("lagtimes are:\n")
    latency_line = lines[tagindex+1]
    lagtimes = json.loads(latency_line.replace("'", '"'))
    return [D(x) for x in lagtimes]

def main():
    _set_plot_labels_title()
    path_extractor1 = PathExtracts(sys.argv[1])
    latencies1 = extract_latencies(path_extractor1.logpath)
    plot_datavector(latencies1, path_extractor1, '.')
    if len(sys.argv) == 3:
        path_extractor2 = PathExtracts(sys.argv[2])
        latencies1 = extract_latencies(path_extractor2.logpath)
        plot_datavector(latencies1, path_extractor2, 'rx')
        outputbasename = path_extractor1.core_name + '_v_' + path_extractor2.core_name + '.png'
        plt.savefig( Path("./pngs/" ) / Path( outputbasename ) )
    else:
        plt.savefig( Path("./pngs/" ) / Path(pathextractor1.core_name + ".png") )

if __name__ == '__main__':
    main()
