#! /usr/bin/env python3

import maxminddb, os, requests, hashlib
from tqdm import tqdm

PACKAGE_DIR = os.path.dirname(os.path.realpath(__file__))
DB_FILE = os.path.join(PACKAGE_DIR, 'rbs_db.mmdb')
MD_FILE = os.path.join(PACKAGE_DIR, 'MD5.txt')

class IpScoop():

    def __init__(self, ip:str) -> None:
#         self.download_data()
#         self.check_md5()         
        self.ip = ip
        self.reader = maxminddb.open_database(DB_FILE)
        self.data = self.reader.get(self.ip)
        self.cidr = self.data['cidr']
        self.range = self.data['range']
        self.country = self.data['country']
        self.tzid = self.data['tzid']
        self.geo = {'lat': self.data['lat'], 'lon': self.data['lon']}
        
    def download_data(self):
        if not os.path.exists(DB_FILE):    
            url = 'https://github.com/anbuhckr/ipscoop/releases/download/v0.1.0/rbs_db.mmdb'
            response = requests.get(url, stream=True)
            total_size_in_bytes= int(response.headers.get('content-length', 0))
            block_size = 1024
            progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True, desc='download rbs_db.mmdb')
            with open(DB_FILE, 'wb') as file:
                for data in response.iter_content(block_size):
                    progress_bar.update(len(data))
                    file.write(data)
            progress_bar.close()
            if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
                os.remove(DB_FILE)
                return self.download_data()           

    def check_md5(self):
        if not os.path.exists(MD_FILE):
            with open(DB_FILE, 'rb') as f:
                file_hash = hashlib.md5()
                while chunk := f.read(8192):
                    file_hash.update(chunk)
            if file_hash.hexdigest() != '26624ba99cc4c00513e4c571890758fc':
                os.remove(DB_FILE)
                self.download_data()
                return self.check_md5()
            with open(MD_FILE, 'w') as md:
                md.write('26624ba99cc4c00513e4c571890758fc')
