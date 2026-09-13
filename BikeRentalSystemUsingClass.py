class BikeShop:
    def __init__(self,stock):
        self._stock=stock
    def BikeDisplay(self):
        print("Total Bikes available in the stock are ",self._stock)
    def RentBike(self,q):
        if q<=0:
            print("Please enter a valid quantity ...")
        elif q>self._stock:
            print("Sorry ! We don't have enough bikes in stock...😢")
        else:
            total_rent=q*100
            print("Total rent for ",q," bikes is ",total_rent)


while True:
    bike=BikeShop(100)
    uchoice=int(input('''
    1. Display Bikes
    2. Rented Bikes requirement 
    3. Exit  
    '''))
    if uchoice==1:
        bike.BikeDisplay()
    elif uchoice==2:
        q=int(input("Enter the number of bikes you want to rent: "))
        bike.RentBike(q)
    else :
        print("Thank you for visiting our Bike Shop...😊")
        break   
        
