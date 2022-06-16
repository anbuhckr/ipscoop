#! /usr/bin/env python3

import ipscoop, sys, ipaddress
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
        try:
            ip = ipaddress.ip_address(args.data)
            print(ip_scoop.data(str(ip)))
        except:
            print("Not valid IPv4/IPv6 address!")
            sys.exit(1)
    elif args.cidr:
        try:
            ip = ipaddress.ip_address(args.cidr)
            print(ip_scoop.data(str(ip)).cidr)
        except:
            print("Not valid IPv4/IPv6 address!")
            sys.exit(1)
    elif args.range:
        try:
            ip = ipaddress.ip_address(args.range)
            print(ip_scoop.data(str(ip)).range)
        except:
            print("Not valid IPv4/IPv6 address!")
            sys.exit(1)
    elif args.country:
        try:
            ip = ipaddress.ip_address(args.country)
            print(ip_scoop.data(str(ip)).country)
        except:
            print("Not valid IPv4/IPv6 address!")
            sys.exit(1)
    elif args.tzid:
        try:
            ip = ipaddress.ip_address(args.tzid)
            print(ip_scoop.data(str(ip)).tzid)
        except:
            print("Not valid IPv4/IPv6 address!")
            sys.exit(1)
    elif args.lat:
        try:
            ip = ipaddress.ip_address(args.lat)
            print(ip_scoop.data(str(ip)).lat)
        except:
            print("Not valid IPv4/IPv6 address!")
            sys.exit(1)
    elif args.lon:
        try:
            ip = ipaddress.ip_address(args.lon)
            print(ip_scoop.data(str(ip)).lon)
        except:
            print("Not valid IPv4/IPv6 address!")
            sys.exit(1)
    elif args.acc:
        try:
            ip = ipaddress.ip_address(args.acc)
            print(ip_scoop.data(str(ip)).acc)
        except:
            print("Not valid IPv4/IPv6 address!")
            sys.exit(1)
    elif args.isp:
        try:
            ip = ipaddress.ip_address(args.isp)
            print(ip_scoop.data(str(ip)).isp)
        except:
            print("Not valid IPv4/IPv6 address!")
            sys.exit(1)
    elif args.asn:
        try:
            ip = ipaddress.ip_address(args.asn)
            print(ip_scoop.data(str(ip)).asn)
        except:
            print("Not valid IPv4/IPv6 address!")
            sys.exit(1)
    elif args.org:
        try:
            ip = ipaddress.ip_address(args.org)
            print(ip_scoop.data(str(ip)).org)
        except:
            print("Not valid IPv4/IPv6 address!")
            sys.exit(1)
    else:
        print('usage: ipscoop.py [-h]')
        sys.exit(1)
    sys.exit(0)
