from typing import List, Union
from urllib.parse import urljoin

import json

from aiohttp import ClientSession
from bs4 import BeautifulSoup
from fastapi import HTTPException
from fastapi import status as http_status

from app.core.config import QUOTES_SITE_ENTRYPOINT
from app.listings.schemas import PropertyListing

async def get_text(url: str) -> BeautifulSoup:
    async with ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()

            if response.status == 200:
                text = BeautifulSoup(text,'html.parser')

                return text

    raise HTTPException(status_code=http_status.HTTP_501_NOT_IMPLEMENTED,
                        detail=f"Scraper didn't succeed in getting data:\n"
                               f"\turl: {url}\n"
                               f"\tstatus code: {response.status}\n"
                               f"\tresponse text: {text}")

def parse_listing(text: BeautifulSoup) -> PropertyListing:
    script_tag = text.find(attrs={"id":"__NEXT_DATA__","type":"application/json"})

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