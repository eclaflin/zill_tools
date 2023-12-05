from listing import scrape_page, PropertyListing 
from quote import PropertyQuote

url = input("Enter a Zillow Listing URL: ")

data_dict = scrape_page(url)

listing = PropertyListing.from_dict(data_dict)

print("The list price is %d\n" % listing.price)
down = input("Enter a down payment amount: ")
int_rate = input("Enter an interest rate for a 30-year loan: ")

quote = PropertyQuote(property_listing=listing, interest_rate=float(int_rate), down_payment=int(down), mortgage_term_years=30)

quote.calc_mortgage_pmt()