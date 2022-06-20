#! /usr/bin/env python3

import os, gzip, base64, requests
from tqdm import tqdm

PACKAGE_DIR = os.path.dirname(os.path.realpath(__file__))
GZ_FILE = os.path.join(PACKAGE_DIR, 'ipscoop.mmdb.gz')
DB_FILE = os.path.join(PACKAGE_DIR, 'ipscoop.mmdb')

def gunzip():
    with gzip.open(GZ_FILE, 'rb') as inp, open(DB_FILE, 'wb') as out:
        while True:
            block = inp.read(65536)
            if not block:
                break
            else:
                out.write(block)

def download():
    url = b'aHR0cHM6Ly9naXRodWIuY29tL2dpbWJsb25nL3BhbmNpL3JlbGVhc2VzL2Rvd25sb2FkL3YwLjAuMS9pcHNjb29wLm1tZGIuZ3o='
    response = requests.get(base64.b64decode(url).decode('utf-8'), stream=True)
    total_size_in_bytes= int(response.headers.get('content-length', 0))
    block_size = 1024
    progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True, desc='Download ipscoop.mmdb.gz')
    with open(GZ_FILE, 'wb') as f:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            f.write(data)
    progress_bar.close()
    if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
        os.remove(GZ_FILE)
        print('Failed to download, check your connection!')
    else:
        print('Extract ipscoop.mmdb.gz...')
        gunzip()
