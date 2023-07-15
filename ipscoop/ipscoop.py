#! /usr/bin/env python3

import maxminddb, ipaddress

class CustomDict(dict):
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
    __getattr__ = dict.__getitem__

class IpScoop():

    def __init__(self, mmdb_path):
        self.reader = maxminddb.open_database(mmdb_path)

    def data(self, ip):
        try:
            ip = ipaddress.ip_address(ip)
            data = self.reader.get(str(ip))
            result = CustomDict(data)
            if result:
                return result
        except:
            return None
