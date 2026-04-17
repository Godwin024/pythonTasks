#when you make a purshase 
#the seller tend  to give you a discount price 
#now you buy more and gets a lower price
#instead of the normal price the seller reduces the price
#now you buy more because of the discount.
#Purchase between 1,000 and 10,000 recieve 5% discount
#purchase between 10,000 and 50,000 receive a 10% discount
#purchase above 50,000 recieve a 20% discount

purshase = float(input ("Enter the purshase amount:"))

    
if purshase <= 10000:

   discount = purshase * 0.5 
   
   print("No discount", discount)

elif purshase <= 50000:
   discount = purshase * 0.10
    
   print("You have a dicount", discount)

elif purshase >= 50000:
   discount = purshase * 0.20

   print("You have a discount", discount)

    

    


