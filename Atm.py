
class Atm(object):
 def __init__(self,cardNumber,pinNumber,balance):
  self.cardNumber=cardNumber
  self.pinNumber=pinNumber
  self.balance=balance 

 def Validation(self,cardnumber,pinnumber):
  if((int(self.cardNumber)== int(cardnumber))& (int(self.pinNumber)==int(pinnumber))):
   print("Select 1:-Withdrawl, 2:-Deposition, 3:-viewBalance :")
   return 1

  return 0   

 def WithDrawlMoney(self,WithDrawl):
  
  if(self.balance < WithDrawl):
   print("insuffecient account balance") 
   return 0   
  self.balance = int(self.balance)- int(WithDrawl)
  print("withdrawl successfull. Your balance is:-"+self.balance)
  

 def Deposition(self,Deposit):
  
  self.balance=int(self.balance)+int(Deposit)
  print("successfully deposited. Total balance is:-"+self.balance)
  

 def viewBalance(self):

  self.balance=balance  

Srujan=Atm("1111222233334444","4321","500")  
ret = Srujan.Validation("1111222233334444","4321")

if (ret == 1):
 userChoice=input("Enter 1 or 2 or 3:-") 

 if(userChoice == "1"):
  Srujan.WithDrawlMoney("50")
 if(userChoice == "2"):
  Srujan.Deposition("100")
 if(userChoice == "3"):
  Srujan.viewBalance()

 


    





