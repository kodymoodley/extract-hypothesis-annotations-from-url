#!/usr/bin/env python2
"""
Print out the fingerprint of the given PDF file.

Exit with non-zero status code if fingerprinting the file fails.

Installation:

1. Create a new Python virtual environment

2. Install PDFMiner from git (because the version on PyPI is out of date and
   missing AES v2 decryption support):

   pip install git+https://github.com/euske/pdfminer.git

Usage:

    ./fingerprint.py /path/to/file.pdf

This code was written by Sean Hammond: https://www.seanh.cc/2017/11/22/pdf-fingerprinting/

"""
import hashlib
import sys

import pdfminer.pdfparser
import pdfminer.pdfdocument


def hexify(byte_string):
    ba = bytearray(byte_string)

    def byte_to_hex(b):
        hex_string = hex(b)

        if hex_string.startswith('0x'):
            hex_string = hex_string[2:]

        if len(hex_string) == 1:
            hex_string = '0' + hex_string

        return hex_string

    return ''.join([byte_to_hex(b) for b in ba])


def hash_of_first_kilobyte(path):
    f = open(path, 'rb')
    h = hashlib.md5()
    h.update(f.read(1024))
    return h.hexdigest()


def file_id_from(path):
    """
    Return the PDF file identifier from the given file as a hex string.

    Returns None if the document doesn't contain a file identifier.

    """
    parser = pdfminer.pdfparser.PDFParser(open(path, 'rb'))
    document = pdfminer.pdfdocument.PDFDocument(parser)

    for xref in document.xrefs:
        if xref.trailer:
            trailer = xref.trailer

            try:
                id_array = trailer["ID"]
            except KeyError:
                continue

            # Resolve indirect object references.
            try:
                id_array = id_array.resolve()
            except AttributeError:
                pass

            try:
                file_id = id_array[0]
            except TypeError:
                continue

            return hexify(file_id)


def fingerprint(path):
    return file_id_from(path) or hash_of_first_kilobyte(path)


# if __name__ == '__main__':
#     print fingerprint(sys.argv[1])