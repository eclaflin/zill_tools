from prettytable import PrettyTable
from tax import rate_pull

class PropertyQuote:
    def __init__(self, property_listing, interest_rate, down_payment, mortgage_term_years):
        self.property_listing = property_listing
        self.interest_rate = interest_rate
        self.down_payment = down_payment
        self.financed_amt = (self.property_listing.price - self.down_payment)
        self.mortgage_term_years = mortgage_term_years

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

        print(table)
        #fmt_output = "total monthly payment = %d\n monthly principal = %d\n monthly interest = %d\n monthly_tax = %d" % (
        #    self.total_monthly_pmt, self.mothly_principal_pmt, self.monthly_interest_pmt, self.monthly_tax_pmt)
        
        #print(fmt_output)