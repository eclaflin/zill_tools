from listing import scrape_page, PropertyListing 
from quote import PropertyQuote
from rates import get_latest_rate
from simple_term_menu import TerminalMenu

def quote_a_property():

    url = input("Enter a Zillow Listing URL: ")
    data_dict = scrape_page(url)
    listing = PropertyListing.from_dict(data_dict)

    print("The list price is %d\n" % listing.price)
    down = input("Enter a down payment amount: ")
    int_rate = float(get_latest_rate())/100

    quote = PropertyQuote(property_listing=listing, interest_rate=float(int_rate), down_payment=int(down), mortgage_term_years=30)

    quote.calc_mortgage_pmt()
    quote.write_quote()

def closing_cost_estimator():
    print('this is the closing cost estimatory')

def interest_rate_spread():
    print('this is the interest rate spread')

def main():
    options = [
        '1. Quote a property',
        '2. Closing Cost Estimator',
        '3. Interest Rate Spread'
    ]

    menu = TerminalMenu(options)
    menu_index = menu.show()

    if menu_index == 0:
        return quote_a_property()
    
    elif menu_index == 1:
        return closing_cost_estimator()
    
    elif menu_index == 2:
        return interest_rate_spread()

    #print(f"You have selected {options[menu_index]}")

if __name__ == "__main__":
    main()