
class PropertyQuote:
    def __init__(self, property_listing, interest_rate, down_payment):
        self.property_listing = property_listing
        self.interest_rate = interest_rate
        self.down_payment = down_payment

    def calculate_quote(self):
        purchase_price = self.property_listing.price