class atm (object):
    def __init__(self, card_number,pin_number,CashWithdrawl,BalanceEnquiry):
        self.card_number=card_number
        self.pin_number=pin_number
        self.CashWithdrawl=CashWithdrawl
        self.BalanceEnquiry=BalanceEnquiry

    def card_number(self):
        print("123456")

    def pin_number(self):
        print("654321")    

    def CashWithdrawl(self):
        print("$100")    

    def BalanceEnquiry(self):
        print("180923")    

Bank=atm("123456","654321","$100",180923)
Bank.company