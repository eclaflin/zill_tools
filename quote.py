
class PropertyQuote:
    def __init__(self, property_listing, interest_rate, down_payment, mortgage_term_years):
        self.property_listing = property_listing
        self.interest_rate = interest_rate
        self.down_payment = down_payment
        self.financed_amt = (self.property_listing.price - self.down_payment)
        self.mortgage_term_years = mortgage_term_years

    def calc_tax_pmt(self):
        try:
            self.curr_tax_ass = self.property_listing.taxHistory[0]['taxPaid']
            self.monthly_tax_pmt = self.curr_tax_ass/12

        except:
            raise valueError('No tax history available on zillow') 
        
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

        fmt_output = "total monthly payment = %d\n monthly principal = %d\n monthly interest = %d\n monthly_tax %d" % (
            self.total_monthly_pmt, self.mothly_principal_pmt, self.monthly_interest_pmt, self.monthly_tax_pmt)
        
        print(fmt_output)