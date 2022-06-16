#! /usr/bin/env python3

import ipscoop, sys
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('-db', help="mmdb path",default='ipscoop.mmdb', type=str)
parser.add_argument('-ip', help="ip address", default=None, type=str)
args = parser.parse_args()

if __name__ == '__main__':
    try:
        ip_scoop = ipscoop.IpScoop(args.db)
    except:
        print("mmdb file not found!")
        sys.exit(1)
    if args.ip:
        data = ip_scoop.data(args.ip)
        if data:
            print(data)
        else:
            print("Data not found!")
    else:
        print('usage: ipscoop.py [-h]')
    sys.exit(0)
