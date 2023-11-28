import json
import requests
import re
from bs4 import BeautifulSoup

headers = {
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br, zstd',
    'accept-language': 'en-US,en;q=0.9',
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
}

url = 'https://www.zillow.com/homedetails/15-Maine-Ter-A-Somerville-MA-02145/2054344316_zpid/'

res = requests.get(headers=headers, url=url)

content = BeautifulSoup(res.text, 'html.parser').find("script", {"id": "__NEXT_DATA__"})

pre_data = json.loads(content.text)

data = json.loads(pre_data['props']['pageProps']['componentProps']['gdpClientCache'])

keys_view = data.keys()

first_key = list(keys_view)[0]

print(data[first_key]['property'])

