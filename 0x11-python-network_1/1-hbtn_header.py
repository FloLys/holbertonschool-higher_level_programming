#!/usr/bin/python3
""" Show the X-Request-Id variable found in the header of the response url """
import urllib.request
from sys import argv


if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as response:
        html = response.info()
        print(html.get('X-Request-Id'))
