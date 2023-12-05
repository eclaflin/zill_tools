import json
import requests
import re 
import sys
from bs4 import BeautifulSoup
from typing import Dict

#url = 'https://www.zillow.com/homedetails/15-Maine-Ter-A-Somerville-MA-02145/2054344316_zpid/'

def scrape_page(url):

    headers = {
        'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br, zstd',
        'accept-language': 'en-US,en;q=0.9',
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    }

    res = requests.get(url, headers=headers)

    soup = BeautifulSoup(res.text, 'html.parser')

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
    
            return listing_data

        except KeyError as e:
            print(f"Error accessing nested keys:{e}")

    else:
        print("Script tag not found")

class PropertyListing:
    
    def __init__(self, 
                 zpid, 
                 city, 
                 state, 
                 homeStatus, 
                 address, 
                 bedrooms, 
                 bathrooms, 
                 price, 
                 yearBuilt, 
                 streetAddress, 
                 zipcode, 
                 homeType, 
                 monthlyHoaFee,
                 livingArea,
                 taxHistory, 
                 priceHistory, 
                 timeOnZillow, 
                 pageViewCount, 
                 favoriteCount,
                 daysOnZillow, 
                 latitude, 
                 longitude,
                 propertyTaxRate,
                 lotSize,
                 annualHomeownersInsurance):
        
        self.zpid = zpid 
        self.city = city 
        self.state = state 
        self.homeStatus = homeStatus 
        self.address = address 
        self.bedrooms = bedrooms 
        self.bathrooms = bathrooms 
        self.price = price 
        self.yearBuilt = yearBuilt 
        self.streetAddress = streetAddress 
        self.zipcode = zipcode 
        self.homeType = homeType 
        self.monthlyHoaFee = monthlyHoaFee
        self.livingArea = livingArea
        self.taxHistory = taxHistory 
        self.priceHistory = priceHistory 
        self.timeOnZillow = timeOnZillow 
        self.pageViewCount = pageViewCount 
        self.favoriteCount = favoriteCount
        self.daysOnZillow = daysOnZillow 
        self.latitude = latitude 
        self.longitude = longitude
        self.propertyTaxRate = propertyTaxRate
        self.lotSize = lotSize
        self.annualHomeownersInsurance = annualHomeownersInsurance


    @classmethod
    def from_dict(cls, listing_dict: Dict[str, any]) -> 'PropertyListing':

        valid_keys = cls.__init__.__code__.co_varnames[1:]

        # Extract only the allowed keys from listing_dict
        filtered_dict = {k: v for k, v in listing_dict.items() if k in valid_keys}

        return cls(**filtered_dict)