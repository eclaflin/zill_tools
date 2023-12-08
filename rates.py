""" 
module to pull expected interest rate, given a property listing, appraised value, and expected down payment
This will need to do a couple things:
    1. validate the expected LTV ratio of the mortgage, given down payment and appraised value of the home
    2. scrape latest interest rates
    3. return the best option (e.g. between FHA vs. traditional)
"""

import requests
from bs4 import BeautifulSoup

def get_latest_rate():

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-encoding': 'gzip, deflate, br, zstd',
        'accept-language': 'en-US,en;q=0.9',
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        'upgrade-insecure-requests':'1',
    }

    url = 'https://fred.stlouisfed.org/series/OBMMIC30YFLVGT80FGE740'

    response=requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        span_tag = soup.find('span', class_='series-meta-observation-value')
        value = span_tag.text
        
        return value

    else:
         print(f"Failed to retrieve the page. Status code: {response.status_code}") 