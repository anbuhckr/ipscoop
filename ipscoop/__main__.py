#! /usr/bin/env python3

import ipscoop, sys, os
from ipscoop import utils
from argparse import ArgumentParser

PACKAGE_DIR = os.path.dirname(os.path.realpath(__file__))
DB_FILE = os.path.join(PACKAGE_DIR, 'ipscoop.mmdb')

parser = ArgumentParser()
parser.add_argument("-db", help="mmdb path",default=DB_FILE, type=str)
parser.add_argument("-ip", help="ip address", default=None, type=str)
parser.add_argument("--download", help="download mmdb file", default=False, action="store_true")
args = parser.parse_args()

if __name__ == '__main__':
    if args.download:
        utils.download()
        sys.exit(0)
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
