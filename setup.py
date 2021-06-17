#! /usr/bin/env python3

import re
import ast
from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()


_version_re = re.compile(r'__version__\s+=\s+(.*)')


with open('ipscoop/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))


requirements = [    
    'maxminddb>=2.0.3',
    'requests>=2.25.1',
    'tqdm>=4.61.0',
]


setup(
    name='ipscoop',
    version=version,
    description="Fast Ip Scoop",
    long_description=readme,
    author="anbuhckr",
    author_email='anbu.hckr@hotmail.com',
    url='https://github.com/anbuhckr/ipscoop',
    packages=find_packages(),
    package_dir={},    
    include_package_data=True,    
    install_requires=requirements,
    license="GNU GENERAL PUBLIC LICENSE",
    zip_safe=False,
    keywords='ipscoop',
    classifiers=[
        'Development Status :: 1 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: GNU GENERAL PUBLIC LICENSE',
        'Natural Language :: English',       
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: IP'
    ],
)
