#! /usr/bin/env python3

import maxminddb

class CustomDict(dict):
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
    __getattr__ = dict.__getitem__

class IpScoop():

    def __init__(self, mmdb_path):
        self.reader = maxminddb.open_database(mmdb_path)

    def data(self, ip):
        return CustomDict(self.reader.get(ip))
