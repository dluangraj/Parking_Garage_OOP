class Garage():


#All of us
    def __init__(self):
        self.tickets = ["1","2","3","4","5","6","7","8","9","10"]
        self.parkingSpaces = ["1","2","3","4","5","6","7","8","9","10"]
        self.currentTicket = {}    #{1:"paid"} 
#All End
    

#Faiber Take Ticket
    def takeTicket(self):

        if self.tickets != []:
            takenTicket = self.tickets.pop(0)
            self.currentTicket[takenTicket] = "unpaid"
            del self.parkingSpaces[0]
            print(f"You have picked up a ticket for spot: {takenTicket}")
        else:
            print('The parking lot is full.')
            return
#Faiber End
        

#Cookie Pay For Parking
    def payForParking(self):
        self.parkingMenu()
        parkingSpot = input("What spot are you paying for? ")
        if parkingSpot in self.currentTicket:
            if parkingSpot != " ":
                self.currentTicket.update({parkingSpot : "paid"})
                print("15 minutes have been added before you need to leave.")
        else:
            print("Parking spot currently available, no need to pay.")
        self.parkingMenu()
#Cookie End

# Dennis Leave Garage
    def leaveGarage(self):
            self.parkingMenu()
            parkingTicket = input("Which parking spot is leaving?: ")
            try:  
                if self.currentTicket[parkingTicket] == "paid":
                    print("Thank you, have a nice day")
                    del self.currentTicket[parkingTicket]
                    self.tickets.append(parkingTicket)
                    self.parkingSpaces.append(parkingTicket)
                elif self.currentTicket[parkingTicket] == "unpaid":
                    print("Please pay your ticket!")
                    self.payForParking()
            except:
                print("This is invalid input")
            self.parkingMenu()         
# Dennis End

    def parkingMenu(self):
            print("\n            Spots Available:\n")
            print("|  ",*self.tickets,"   |", sep='  |_|  ')
            print("\n            Spots Taken:\n")
            people = " ".join(f" |_{key}_:_{value}_| " for key, value in self.currentTicket.items())
            print(people)


#All of us
    def run(self):
        
        self.parkingMenu()
        while True:
            response = input("""\n
                    Welcome to the Rangers Parking Garage! 
            What would you like to do(use the letter assigned letter)?

                             [T]ake Ticket 
                             [P]ay for Parking 
                             [L]eave Garage
                             [Q]uit 
                        """)


            if response.lower() == "t":
                self.takeTicket()
            elif response.lower() == "p":
                self.payForParking()
            elif response.lower() == "l":
                self.leaveGarage()    
            elif response.lower() == "q":
                print("Thank you for your business!")
                break
            else:
                print("Incorrect Input... Try Again")
            # print(f"Available Parking Spots: {self.tickets}")
            # print(f"Current Parking Spots: {self.currentTicket}")
#All End
        

rangersParking = Garage()
rangersParking.run()