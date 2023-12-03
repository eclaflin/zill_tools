import json
import requests
import re 
from bs4 import BeautifulSoup
import sys

headers = {
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br, zstd',
    'accept-language': 'en-US,en;q=0.9',
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
}

url = 'https://www.zillow.com/homedetails/15-Maine-Ter-A-Somerville-MA-02145/2054344316_zpid/'

res = requests.get(headers=headers, url=url)

soup = BeautifulSoup(res.text, 'html.parser')

#tag = soup.script
#print(tag.string)

script_tag = soup.find(attrs={"id":"__NEXT_DATA__","type":"application/json"})

# check if the soup.find successfully found a <script> tag
if script_tag:
    
    # extract content of script string
    script_content = script_tag.string

    # load content to json object
    data_dict = json.loads(script_content)

    # extract desired data:
    try:

        page_data = json.loads(data_dict['props']['pageProps']['componentProps']['gdpClientCache'])
        listing_data = page_data[list(page_data.keys())[0]]['property']
 
        print(listing_data.keys())

    except KeyError as e:
        print(f"Error accessing nested keys:{e}")

else:
    print("Script tag not found")


        
    

