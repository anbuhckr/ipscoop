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
            return CustomDict(data)
        except:
            pass
        return "Not valid IPv4/IPv6 address!"

    def cidr(self, ip):
        try:
            ip = ipaddress.ip_address(ip)
            data = self.reader.get(str(ip))
            return CustomDict(data).cidr
        except:
            pass
        return "Not valid IPv4/IPv6 address!"

    def range(self, ip):
        try:
            ip = ipaddress.ip_address(ip)
            data = self.reader.get(str(ip))
            return CustomDict(data).range
        except:
            pass
        return "Not valid IPv4/IPv6 address!"

    def country(self, ip):
        try:
            ip = ipaddress.ip_address(ip)
            data = self.reader.get(str(ip))
            return CustomDict(data).country
        except:
            pass
        return "Not valid IPv4/IPv6 address!"

    def tzid(self, ip):
        try:
            ip = ipaddress.ip_address(ip)
            data = self.reader.get(str(ip))
            return CustomDict(data).tzid
        except:
            pass
        return "Not valid IPv4/IPv6 address!"

    def lat(self, ip):
        try:
            ip = ipaddress.ip_address(ip)
            data = self.reader.get(str(ip))
            return CustomDict(data).lat
        except:
            pass
        return "Not valid IPv4/IPv6 address!"

    def lon(self, ip):
        try:
            ip = ipaddress.ip_address(ip)
            data = self.reader.get(str(ip))
            return CustomDict(data).lon
        except:
            pass
        return "Not valid IPv4/IPv6 address!"

    def acc(self, ip):
        try:
            ip = ipaddress.ip_address(ip)
            data = self.reader.get(str(ip))
            return CustomDict(data).acc
        except:
            pass
        return "Not valid IPv4/IPv6 address!"

    def isp(self, ip):
        try:
            ip = ipaddress.ip_address(ip)
            data = self.reader.get(str(ip))
            return CustomDict(data).isp
        except:
            pass
        return "Not valid IPv4/IPv6 address!"

    def asn(self, ip):
        try:
            ip = ipaddress.ip_address(ip)
            data = self.reader.get(str(ip))
            return CustomDict(data).asn
        except:
            pass
        return "Not valid IPv4/IPv6 address!"

    def org(self, ip):
        try:
            ip = ipaddress.ip_address(ip)
            data = self.reader.get(str(ip))
            return CustomDict(data).org
        except:
            pass
        return "Not valid IPv4/IPv6 address!"
