#! /usr/bin/env python3

import maxminddb, os, urllib3

PACKAGE_DIR = os.path.dirname(os.path.realpath(__file__))
DB_FILE = os.path.join(PACKAGE_DIR, 'rbs_db.mmdb')

class IpScoop():

    def __init__(self, ip:str) -> None:        
        if not os.path.exists(DB_FILE):
            self.download_data()
        self.ip = ip
        self.reader = maxminddb.open_database(DB_FILE)
        self.data = self.reader.get(self.ip)
        self.cidr = self.data['cidr']
        self.range = self.data['range']
        self.country = self.data['country']
        self.tzid = self.data['tzid']
        self.geo = {'lat': self.data['lat'], 'lon': self.data['lon']}
        
    def download_data(self):   
        urllib3.disable_warnings()
        url = 'https://github.com/anbuhckr/ipscoop/releases/download/v0.1.0/rbs_db.mmdb'
        with urllib3.PoolManager() as http:
            r = http.request('GET', url)
            with open(DB_FILE, 'wb') as fout:
                fout.write(r.data)
