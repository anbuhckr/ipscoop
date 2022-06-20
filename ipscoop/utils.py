#! /usr/bin/env python3

import os, requests
from tqdm import tqdm

PACKAGE_DIR = os.path.dirname(os.path.realpath(__file__))
DB_FILE = os.path.join(PACKAGE_DIR, 'ipscoop.mmdb')

def download():
    url = 'https://github.com/gimblong/panci/releases/download/v0.0.1/ipscoop.mmdb.gz'
    response = requests.get(url, stream=True)
    total_size_in_bytes= int(response.headers.get('content-length', 0))
    block_size = 1024
    progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True, desc='download ipscoop.mmdb')
    with open(DB_FILE, 'wb') as f:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            f.write(data)
    progress_bar.close()
    if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
        os.remove(DB_FILE)
        print('Failed to download, check your connection!')
