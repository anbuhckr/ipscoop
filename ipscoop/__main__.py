#! /usr/bin/env python3

import ipscoop, sys
from argparse import ArgumentParser

parser = ArgumentParser()    
parser.add_argument('-data', help="show ip data", default=None, type=str)
parser.add_argument('-cidr', help="show ip cidr", default=None, type=str)
parser.add_argument('-range', help="show ip range", default=None, type=str)
parser.add_argument('-country', help="show ip country", default=None, type=str)
parser.add_argument('-tzid', help="show ip timezone", default=None, type=str)
parser.add_argument('-geo', help="show ip geo", default=None, type=str)
args = parser.parse_args()

if __name__ == '__main__':
    if args.data:
        ip_scoop = ipscoop.IpScoop(args.data)
        print(ip_scoop.data)
    elif args.cidr:
        ip_scoop = ipscoop.IpScoop(args.cidr)
        print(ip_scoop.cidr)
    elif args.range:
        ip_scoop = ipscoop.IpScoop(args.range)
        print(ip_scoop.range) 
    elif args.country:
        ip_scoop =ipscoop.IpScoop(args.country)
        print(ip_scoop.country)    
    elif args.tzid:
        ip_scoop = ipscoop.IpScoop(args.tzid)
        print(ip_scoop.tzid)   
    elif args.geo:
        ip_scoop = ipscoop.IpScoop(args.geo)
        print(ip_scoop.geo)
    else:
        print('usage: ipscoop.py [-h]')   
    sys.exit()
