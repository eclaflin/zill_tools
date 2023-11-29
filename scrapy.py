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

# what is an object of the BeautifulSoup class?  what can i do with that to make json.loads() easier?
content = BeautifulSoup(res.text, 'html.parser').find("script", {"id": "__NEXT_DATA__"})

pre_data = json.loads(content.text)
# how do I more efficientyly parse a json structure
data = json.loads(pre_data['props']['pageProps']['componentProps']['gdpClientCache'])

# data is a variable containing the output of json .loads 
# so what is that that I am accessing with .keys(), is it a dictionary?
keys_view = data.keys()

# if data.keys() is a list, why do I need to cast keys_view to a list?  isn't it already a list?
first_key = list(keys_view)[0]

# first key is a dictionary that contains all of the data that I want 
print(data[first_key]['property'])

