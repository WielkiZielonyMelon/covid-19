import argparse
import codecs
import json
import os
import time

from lxml import html
import requests

import common

parser = argparse. ArgumentParser()
parser.add_argument("--page", type=str, help="Web page that data will be extracted from", default="https://www.gov.pl/web/koronawirus/wykaz-zarazen-koronawirusem-sars-cov-2")
parser.add_argument("--delay", type=int, help="After what time page will be downloaded again", default=3600)
parser.add_argument("--xpath", type=str, help="xpath query with data to extract", default="pre[@id=\"registerData\"]")
parser.add_argument("--key", type=str, help="Extract value of this key", default="parsedData")
parser.add_argument("--target_dir", type=str, help="Target directory to save extracted data", default="data")
args = parser.parse_args()

while True:
    page = requests.get(args.page)
    # Make sure encoding is set, otherwise we loose Polish letters
    tree = html.fromstring(page.content.decode("utf-8"))

    # This part contains interesting stuff
    vovoidships_stats = tree.xpath('//' + args.xpath + '/text()')[0]
    vovoidships_stats = json.loads(vovoidships_stats)
    # Only interested in parsed data
    vovoidships_stats = json.loads(vovoidships_stats[args.key])

    # Save data to a file
    filename = common.DATA_FILENAME_HEADER + time.strftime("%Y%m%d-%H%M%S") + "." + common.DATA_FILENAME_EXT
    filename = os.path.join(args.target_dir, filename)
    with codecs.open(filename, "w", "utf-8") as f:
        json.dump(vovoidships_stats, f, ensure_ascii=False)

    time.sleep(args.delay)
