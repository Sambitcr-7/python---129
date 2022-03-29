'''
1 2 3 4 5 6 7 8 9 10
'''
class Train:
    def __init__(self,name,fare,seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getstatus(self):
        print("************")
        print(f"The same of the train is {self.name}")
        print(f"The seats available in the train are {self.seats}")    
        print("**************")

    def getattribute(self):
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the train are {self.seats}" )


    def fareInfo(self):
        print(f"The price of the ticket is : {self.fare}")  

    def bookTicket(self):
        if(self.seats>0):
            print(f"Your ticket has been booked! Your seat number is {self.seats}") 
            self.seats = self.seats -1
        else:
            print("Sorry this train is full! Kindly try in tatkal")         

intercity = Train("Intercity Express: 14015",90,300)   
# intercity.getattribute()
# intercity.fareInfo() 
intercity.getstatus() 
intercity.bookTicket()
intercity.getstatus()