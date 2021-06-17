#! /usr/bin/env python3

import maxminddb, os
from argparse import ArgumentParser

parser = ArgumentParser()    
parser.add_argument('-data', help="show ip data", default=None, type=str)
parser.add_argument('-cidr', help="show ip cidr", default=None, type=str)
parser.add_argument('-range', help="show ip range", default=None, type=str)
parser.add_argument('-country', help="show ip country", default=None, type=str)
parser.add_argument('-tzid', help="show ip timezone", default=None, type=str)
parser.add_argument('-geo', help="show ip geo", default=None, type=str)
args = parser.parse_args()

PACKAGE_DIR = os.path.dirname(os.path.realpath(__file__))
DB_FILE = os.path.join(PACKAGE_DIR, 'rbs_db.mmdb')

class IpScoop():

    def __init__(self, ip:str) -> None:
        self.ip = ip
        self.reader = maxminddb.open_database(DB_FILE)
        self.data = self.reader.get(self.ip)
        self.cidr = self.data['cidr']
        self.range = self.data['range']
        self.country = self.data['country']
        self.tzid = self.data['tzid']
        self.geo = {'lat': self.data['lat'], 'lon': self.data['lon']}
        
if __name__ == '__main__':
    if args.data:
        ip_scoop = IpScoop(args.data)
        print(ip_scoop.data)
    elif args.cidr:
        ip_scoop = IpScoop(args.cidr)
        print(ip_scoop.cidr)
    elif args.range:
        ip_scoop = IpScoop(args.range)
        print(ip_scoop.range) 
    elif args.country:
        ip_scoop = IpScoop(args.country)
        print(ip_scoop.country)    
    elif args.tzid:
        ip_scoop = IpScoop(args.tzid)
        print(ip_scoop.tzid)   
    elif args.geo:
        ip_scoop = IpScoop(args.geo)
        print(ip_scoop.geo)
    else:
        print('usage: ipscoop.py [-h]')   
    sys.exit()
