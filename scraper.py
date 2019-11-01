import requests
import json
from selectorlib import Extractor
import argparse

argparser = argparse.ArgumentParser()
argparser.add_argument('url', help='Amazon Product Details URL')

extd = Extractor.from_yaml_file('amazon.yml')  # Extracting data from yml

browser = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'
headers = {'User-Agent': browser}

args = argparser.parse_args()  # Download Webpage with requests
req = requests.get(args.url, headers=headers)

res = extd.extract(req.text)

print(json.dumps(res, indent=True))  # Dump to json file
