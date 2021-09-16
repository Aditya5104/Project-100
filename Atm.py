class Atm:
    def __init__(self,cardNumber,pinNumber):
        self.cardNumber=cardNumber
        self.pinNumber=pinNumber

    def cashWithDrawl(self,cash):
        cashLeft=50000-cash
        print("You have withdrawn amount "+cash) 
        print("Your remaining balace left is "+cashLeft)     

    def BalanceEnquiry(self):
        print("Your balance is 50000")      

def main():
    cardNumber=input("Enter Your Card Number")
    pinNumber=input("Enter Your Pin Number")
    user1=Atm(cardNumber,pinNumber)
    print("Choose From The Following Options")
    print("1.Balance Enquiry  2.Cash Withdrawl")    

    option=int(input("Enter Your Option"))

    if option==1:
        user1.BalanceEnquiry()
    elif option==2:
        clash=input("Enter Your Amount")
        user1.cashWithDrawl(clash)
    else:
        print("Enter A Valid Number")

main()               
        