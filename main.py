#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import argparse
import requests

GOOGLE_BOOK_PREFIX = "https://www.googleapis.com/books/v1/volumes?q=isbn:"

def argparser():
    """Parses command line options and returns an args object"""
    parser = argparse.ArgumentParser()
    parser.add_argument('--isbn', default="316148410X",
                        help="Specify an isbn as an argument")
    return parser

def print_result(r):
    print("status code =", r.status_code)
    print("headers =", r.headers)
    print("content =", r.content)

def main():
    parser = argparser()
    args = parser.parse_args()

    if args.isbn:
        book_url = GOOGLE_BOOK_PREFIX + args.isbn
        r = requests.get(book_url)
        print_result(r)
    else:
        return parser.print_help()


if __name__ == "__main__":
    main()