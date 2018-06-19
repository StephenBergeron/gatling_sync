#!/usr/bin/python3
__author__ = 'Stephen Bergeron'

import json
import sys
import getopt

ifile = ''
ofile = ''

try:
    myopts, args = getopt.getopt(sys.argv[1:], "i:o:")
except getopt.GetoptError as e:
    print (str(e))
    print("Usage: %s -i input -o output" % sys.argv[0])
    sys.exit(2)

for option, argument in myopts:
    if option == '-i':
        ifile = argument
    elif option == '-o':
        ofile = argument


# Display input and output file name passed as the args
print ("Input file : %s and output file: %s" % (ifile, ofile))





# # # locate stats.json from gatling and load it into an object

# # simulation = '/home/stn/cache/ppas_svv03_a/context.decorator.1529240901/'
# # stats_json = simulation + 'validationsimulation-false/js/stats.json'

with open(ifile, 'r') as f:
    stats = json.load(f)


def mystats(e):
    tau = e['stats']
    print(tau['name'] + '|' + str(tau['percentiles3']['ok']))


def contents_keys(h):
    tau = h['contents'].keys()
    print (tau)
    return tau


contents_keys(stats)

txs = stats['contents']['group_schedrules-92d01']['contents']

for tx in sorted(txs.keys()):
    mystats(txs[tx])


# # # pdb.set_trace()

# # # print(os.environ['CACHEDIR'])

# # # def print_a_list(a_list):
# # #     for item in a_list:
# # #         print(item)
# # # print_a_list(files)
