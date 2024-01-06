from typing import List
from pydantic import BaseModel, HttpUrl

from app.listings.examples import ex_property_listing

class PropertyListing(BaseModel):

    url:HttpUrl
    zpid:int
    city:str
    state:str
    homeStatus:str
    address:dict
    bedrooms:int
    bathrooms:int
    price:int
    yearBuilt:int
    streetAddress:str
    zipcode:str
    homeType:str
    monthlyHoaFee:int
    livingArea:int
    taxHistory:list
    priceHistory:list
    timeOnZillow:str
    pageViewCount:int
    favoriteCount:int
    daysOnZillow:int
    latitude:float
    longitude:float
    propertyTaxRate:float
    lotSize:int
    annualHomeownersInsurance:float

    class Config:
        schema_extra = {"example": ex_property_listing}