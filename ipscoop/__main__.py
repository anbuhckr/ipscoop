#! /usr/bin/env python3

import ipscoop, sys
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('-db', help="mmdb path",default='ipscoop.mmdb', type=str)
parser.add_argument('-data', help="show ip data", default=None, type=str)
parser.add_argument('-cidr', help="show ip cidr", default=None, type=str)
parser.add_argument('-range', help="show ip range", default=None, type=str)
parser.add_argument('-country', help="show ip country", default=None, type=str)
parser.add_argument('-tzid', help="show ip timezone", default=None, type=str)
parser.add_argument('-lat', help="show latitude", default=None, type=str)
parser.add_argument('-lon', help="show longitude", default=None, type=str)
parser.add_argument('-acc', help="show longitude", default=None, type=str)
parser.add_argument('-isp', help="show isp", default=None, type=str)
parser.add_argument('-asn', help="show asn", default=None, type=str)
parser.add_argument('-org', help="show org", default=None, type=str)
args = parser.parse_args()

if __name__ == '__main__':
    try:
        ip_scoop = ipscoop.IpScoop(args.db)
    except:
        print("mmdb file not found!")
        sys.exit(1)
    if args.data:
        print(ip_scoop.data(args.data))
    elif args.cidr:
        print(ip_scoop.cidr(args.cidr))
    elif args.range:
        print(ip_scoop.range(args.range))
    elif args.country:
        print(ip_scoop.country(args.country))
    elif args.tzid:
        print(ip_scoop.tzid(args.tzid))
    elif args.lat:
        print(ip_scoop.lat(args.lat))
    elif args.lon:
        print(ip_scoop.lon(args.lon))
    elif args.acc:
        print(ip_scoop.acc(args.acc))
    elif args.isp:
        print(ip_scoop.isp(args.isp))
    elif args.asn:
        print(ip_scoop.asn(args.asn))
    elif args.org:
        print(ip_scoop.org(args.org))
    else:
        print('usage: ipscoop.py [-h]')
        sys.exit(1)
    sys.exit(0)
