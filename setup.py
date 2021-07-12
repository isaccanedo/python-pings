# -*- coding:utf-8 -*-

try:
  import setuptools
  from setuptools import setup
except ImportError:
  print("Please install setuptools.")

setup_options = dict(
    name        = "pings",
    description = "Cliente de ping simples em Python 3 usando pacote icmp via soquete de baixo nível.",
    author      = "Isac Canedo",    
    license     = "GPL",
    url         = "https://github.com/isaccanedo/python-pings",
    classifiers = [
      "Programming Language :: Python :: 3",
      "Programming Language :: Python :: 3.6",
      'License :: OSI Approved :: GNU General Public License (GPL)'
    ]
)
setup_options["version"] = "0.0.1"
setup_options.update(dict(
  packages         = ['pings'],
))

setup(**setup_options)
