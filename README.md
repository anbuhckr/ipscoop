# ipscoop

[![GitHub issues](https://img.shields.io/github/issues/anbuhckr/ipscoop)](https://github.com/anbuhckr/ipscoop/issues)
[![GitHub forks](https://img.shields.io/github/forks/anbuhckr/ipscoop)](https://github.com/anbuhckr/ipscoop/network)
[![GitHub stars](https://img.shields.io/github/stars/anbuhckr/ipscoop)](https://github.com/anbuhckr/ipscoop/stargazers)
[![GitHub license](https://img.shields.io/github/license/anbuhckr/ipscoop)](https://github.com/anbuhckr/ipscoop/blob/main/LICENSE)
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

Download db file for first time:

```
$ python3 -m ipscoop.IpScoop('8.8.8.8')
```

Get all ip data:

```
$ python3 -m ipscoop.IpScoop('8.8.8.8').data
```

Get ip cidr:

```
$ python3 -m ipscoop.IpScoop('8.8.8.8').cidr
```

Get ip range:

```
$ python3 -m ipscoop.IpScoop('8.8.8.8').range
```

Get ip country:

```
$ python3 -m ipscoop.IpScoop('8.8.8.8').country
```

Get ip timezone id:

```
$ python3 -m ipscoop.IpScoop('8.8.8.8').tzid
```

Get ip geo:

```
$ python3 -m ipscoop.IpScoop('8.8.8.8').geo
```

## Getting Started

``` python
#! /usr/bin/env python3

ftom ipscoop import IpScoop

#load ip
ip_scoop = IpScoop('8.8.8.8')

#all data 
print(f'data: {ip_scoop.data}')

#cidr
print(f'cidr: {ip_scoop.cidr}')

#range
print(f'range: {ip_scoop.range}')

#country
print(f'country: {ip_scoop.country}')

#timezone id 
print(f'timezoneid: {ip_scoop.tzid}'))

#geo 
print(f'geo: {ip_scoop.geo}'))
```

## Ref

* [maxminddb](https://github.com/maxmind/MaxMind-DB-Reader-python)
