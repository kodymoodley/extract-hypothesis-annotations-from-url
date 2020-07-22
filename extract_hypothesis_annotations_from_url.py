#!/usr/bin/env python
# coding: utf-8
# Usage: python extract_hypothesis_annotations_from_url.py --help
# Description: An extensible Python script for extracting Hypothes.is (https://web.hypothes.is/) annotations from a web page located at a given URL
# License: GNU AFFERO GENERAL PUBLIC LICENCE Version 3 (https://www.gnu.org/licenses/agpl-3.0.en.html)

import argparse
import sys
import re
import requests
import json
import urllib.parse
from requests.auth import HTTPBasicAuth

# Commandline interface description
parser = argparse.ArgumentParser()
parser.add_argument("URL", help="The URL of the page you wish to extract Hypothes.is annotations from")
parser.add_argument("API_KEY", help="Your Hypothes.is API key which you can find here: https://hypothes.is/account/developer")
parser.add_argument("-u", "--username", help="If you only wish to extract annotations by a particular user, specify their Hypothes.is username here")
parser.add_argument("-g", "--groupid", help="If you wish to only extract annotations made within a particular Hypothes.is annotation group, specify the Hypothes.is annotation group ID here. A Hypothes.is annotation group ID looks like a random sequence of upper and lower case characters and numbers. It can be found under the Groups menu after logging into your Hypothes.is account on the web interface.")
args = parser.parse_args()

# Check if input string is a valid HTTP URL
def is_valid_url(url):
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    return (re.match(regex, url) is not None)

# Send API search request and return the result
def search_query(api_key, query_url):
    headers = {
        "Content-Type": "application/json;charset=utf-8",
    }
    headers["Authorization"] = "Bearer " + api_key
    r = requests.get(query_url, headers=headers)
    json_result = r.json()
    if r.ok:
        return json_result
    else:
        raise Exception("Error executing API search query")

# Check if input URL is valid
if is_valid_url(sys.argv[1])==False:
    sys.exit("Input URL is invalid")
else:
    # 1. API base URL
    hypothesis_api_base_url = 'https://hypothes.is/api/'
    hypothesis_search_api_endpoint = hypothesis_api_base_url + 'search?'

    # 2. Formulate API query components
    api_query = {}
    # a) Input URL to extract annotations from
    api_query['uri'] = sys.argv[1]
    # b) OPTIONAL: only extract annotations from this Hypothes.is user. I.e., the Hypothes.is username of the annotator.
    if args.username:
        api_query['user'] = args.username
    # c) OPTIONAL: only extract annotations from this Hypothes.is annotation group. I.e., the Hypothes.is group ID from which to extract annotations.
    if args.groupid:
        api_query['group'] = args.groupid

    # 3. URL encoding of the API query
    api_request_url = urllib.parse.urlencode(api_query)

    # 4. Attach the API query URL to the base URL of the Hypothes.is search API
    final_api_request_url = hypothesis_search_api_endpoint + api_request_url

    # 5. Get the API key
    api_key = sys.argv[2]

    # 6. Execute the API search query
    api_request_results = search_query(api_key, final_api_request_url)

    # 7. Print the resulting annotations. In this example, we only print the:
    # a) date of the annotation,
    # b) name of the annotator,
    # c) highlighted text,
    # d) annotation tags (if any) for this text
    count = 1
    print()
    for item in api_request_results['rows']:
        if ('target' in item):
            if (len(item['target']) > 0):
                targ = item['target']
                if ('selector' in targ[0]):
                    for selector in targ[0]['selector']:
                        if selector['type'] == 'TextQuoteSelector':
                            print("Annotation #" + str(count) + ":")
                            print("-----------------")
                            print("date: " + item['created'])
                            print("annotator: " + item['user'])
                            print("highlighted text: " + selector['exact'])
                            print("annotation tags: | ", end='')
                            for tag in item['tags']:
                                print(tag + " | ", end = '')
                            print()
                            count = count + 1             
        print()
