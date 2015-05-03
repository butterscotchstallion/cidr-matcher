# -*- coding: utf-8 -*-
from netaddr import IPAddress, IPNetwork
import sys
from termcolor import colored

if len(sys.argv) < 2:
    sys.exit("Usage: python %s 127.0.0.1 127.0.0.0/8" % sys.argv[0])

ip = sys.argv[1]
cidr = sys.argv[2]

def match_cidr(ip, cidr):
    try:
        network = IPNetwork(u"%s" % cidr)
        is_in_network = IPAddress(u"%s" % ip) in network
        
        return {
            "match": is_in_network,
            "size": network.size
        }
        
    except:
        sys.exit("%s: Invalid input." % colored("ERROR", "red"))

info = match_cidr(ip, cidr)
is_match = info["match"]
size = "{:,}".format(info["size"])

in_network_bit = "%s :: %s (%s IPs)" % (colored(ip, "yellow"), colored(cidr, "yellow"), colored(size, "red"))

print

if is_match:
    print "%s %s" % (colored("MATCH", "green"), in_network_bit)
else:
    print "%s %s" % (colored("NO MATCH", "red"), in_network_bit)

print

    
