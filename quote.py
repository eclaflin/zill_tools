from prettytable import PrettyTable
from listing import scrape_page, PropertyListing 
from rates import get_latest_rate
from tax import rate_pull

class PropertyQuote:
    def __init__(self, property_listing, interest_rate, down_payment, mortgage_term_years):
        self.property_listing = property_listing
        self.interest_rate = interest_rate
        self.down_payment = down_payment
        #self.financed_amt = (self.property_listing.price - self.down_payment)
        self.mortgage_term_years = mortgage_term_years

    def closing_cost_adj(self):
        """
        Factoring for 2% of the total loan amount in closing fees due up front, 
        this means that the financed amount is actually not the list minus the down pmt
        rather, the down payment needs to be treated as an available amount
        """
        # calculated relationship between available cash amount and closing cost pct of list price, assume 4.1% closing
        self.down_pct_list = self.down_payment/self.property_listing.price
        self.closing_pct_list = (-0.01904*self.down_pct_list) + 0.0202912
        self.closing_cost_est = self.closing_pct_list * self.property_listing.price

        self.net_down_payment = self.down_payment - self.closing_cost_est
        
        return self.property_listing.price - self.net_down_payment
        
        pass

    def calc_tax_pmt(self):
        try:
            if len(self.property_listing.taxHistory) == 0:
                self.muni_tax_rate = rate_pull(self.property_listing.zipcode, self.property_listing.city)
                self.estimated_tax_ass = (self.property_listing.price/1000)*self.muni_tax_rate
                self.monthly_tax_pmt = self.estimated_tax_ass/12

            else:
                self.curr_tax_ass = self.property_listing.taxHistory[0]['taxPaid']
                self.monthly_tax_pmt = self.curr_tax_ass/12

        except:
            raise ValueError('Error calculating tax assessment') 

        pass

    def calc_mortgage_pmt(self):
        self.calc_tax_pmt()

        self.financed_amt = self.closing_cost_adj()

        self.monthly_interest_rate = self.interest_rate/12
        self.lifetime_pmts = self.mortgage_term_years * 12
        self.monthly_loan_pmt = (
            self.financed_amt*(
                (self.monthly_interest_rate*(1+self.monthly_interest_rate)**self.lifetime_pmts)
                /
                (((1+self.monthly_interest_rate)**self.lifetime_pmts)-1)
                )
        )

        self.mothly_principal_pmt = self.financed_amt/(self.lifetime_pmts)

        self.monthly_interest_pmt = self.monthly_loan_pmt - self.mothly_principal_pmt 

        self.total_monthly_pmt = self.monthly_loan_pmt + self.monthly_tax_pmt

    def write_quote(self):
        table = PrettyTable(['Line Item','Amount'])
        table.align['Amount'] = 'r'
        table.add_row(['Monthly Principal',"${:,.2f}".format(self.mothly_principal_pmt)])
        table.add_row(['Monthly Interest',"${:,.2f}".format(self.monthly_interest_pmt)])
        table.add_row(['Monthly Tax', "${:,.2f}".format(self.monthly_tax_pmt)])
        table.add_row(['Total Monthly Payment', "${:,.2f}".format(self.total_monthly_pmt)])
        table.add_row(['',''])
        table.add_row(['Estimated Closing Cost', "${:,.2f}".format(self.closing_cost_est)])
        table.add_row(['Estimated Total Financed Amount', "${:,.2f}".format(self.financed_amt)])

        print(table)
        #fmt_output = "total monthly payment = %d\n monthly principal = %d\n monthly interest = %d\n monthly_tax = %d" % (
        #    self.total_monthly_pmt, self.mothly_principal_pmt, self.monthly_interest_pmt, self.monthly_tax_pmt)
        
        #print(fmt_output)

def quote_a_property():

    exit_scr = False

    while not exit_scr:

        url = input("Enter a Zillow Listing URL: ")
        data_dict = scrape_page(url)
        listing = PropertyListing.from_dict(data_dict)

        print("The list price is %d\n" % listing.price)
        down = input("Enter a down payment amount: ")
        int_rate = float(get_latest_rate())/100

        quote = PropertyQuote(property_listing=listing, interest_rate=float(int_rate), down_payment=int(down), mortgage_term_years=30)

        quote.calc_mortgage_pmt()
        quote.write_quote()

        proceed = input("Quote Another? [Y/n]\n")

        if proceed.lower() == 'n':
            exit_scr = True
            return exit_scr

    
