# ipscoop

[![GitHub issues](https://img.shields.io/github/issues/anbuhckr/ipscoop)](https://github.com/anbuhckr/ipscoop/issues)
[![GitHub forks](https://img.shields.io/github/forks/anbuhckr/ipscoop)](https://github.com/anbuhckr/ipscoop/network)
[![GitHub stars](https://img.shields.io/github/stars/anbuhckr/ipscoop)](https://github.com/anbuhckr/ipscoop/stargazers)
[![GitHub license](https://img.shields.io/github/license/anbuhckr/ipscoop)](./LICENSE)
![PyPI - Python Version](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8%20%7C%203.9-blue)

Fast IP Scoop

## Table of Contents

* [Installation](#installation)
* [CLI](#CLI)
* [Getting Started](#getting-started)
* [Ref](#ref)


## Installation

To install ipscoop, simply:

```
$ python3 -m pip install -U git+https://github.com/anbuhckr/ipscoop.git
```

or from source:

```
$ python3 setup.py install
```

## CLI

Download mmdb:

```
$ python3 -m ipscoop --download
```

Usage:

```
$ python3 -m ipscoop -ip 8.8.8.8
```

## Getting Started

``` python
#! /usr/bin/env python3

import ipscoop, os
from ipscoop import IpScoop

ipscoop_path = os.path.dirname(ipscoop.__file__)
db_path = os.path.join(ipscoop_path, 'ipscoop.mmdb')

#load ip
ip_scoop = IpScoop(db_path)

#all data
data = ip_scoop.data('8.8.8.8')
if data:
    print(f'data: {data}')
else:
    print('Data not found!')
  
#cidr
print(f'cidr: {data.cidr}')
```

## Ref

* [maxminddb](https://github.com/maxmind/MaxMind-DB-Reader-python)
