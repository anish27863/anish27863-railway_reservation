import random
import pandas as pd
import payment as upi
tickets={}
pnr=random.randint(100,999)
def display_menu():
  """Prints the menu options for the railway reservation system."""
  print("\nRailway Reservation System")
  print("-" * 30)
  print("1. Search available trains")
  print("2. Check seat availability")
  print("3. Book ticket")
  print("4. Cancel ticket")
  print("5. Check PNR status")
  print("6. View tickets")
  print("7. Exit")
  print("\nPlease enter your choice (1-7): ")


def exitf():
  print("Exiting the system...")
  exit()


def trains_available():
  global trains
  trains = {
    "12345": {
        "Train_name ": "Bhagirathi Express",
        "Train_Number " :"12345" ,
        "Departure_station ": "Lalgola",
        "Departure_time ": "06:00 AM",
        "Arrival_station ": "Sealdah",
        "Arrival_time" : "11:00 AM"
    },
    "56786": {
        "Train_name ": "Teesta Torsa Express",
        "Train_Number " :"56786" ,
        "Departure_station ": "New Alipurduar",
        "Departure_time ": "10:30 AM",
        "Arrival_station ": "Azimganj",
        "Arrival_time" : "06:00 PM"
    },
    "90120": {
        "Train_name ": "Malda Town Express",
        "Train_Number " :"90120" ,
        "Departure_station ": "Nabadwip Dham",
        "Departure_time ": "11:59 PM",
        "Arrival_station ": "Malda Town",
        "Arrival_time" : "07:00 AM"
    },
    "34756": {
        "Train_name ": "Dhano Dhanye Express",
        "Train_Number " :"34756" ,
        "Departure_station ": "Lalgola",
        "Departure_time ": "06:00 AM",
        "Arrival_station ": "Kolkata",
        "Arrival_time" : "03:00 PM"
    },
    "78690": {
        "Train_name ": "Howrah Intercity Express",
        "Train_Number " :"78690" ,
        "Departure_station ": "Azimganj",
        "Departure_time ": "02:00 PM",
        "Arrival_station ": "Howrah",
        "Arrival_time" : "09:00 PM"
    }
}
  print(pd.DataFrame.from_dict(trains, orient='index').reset_index(drop=True))


def seat_availability():
  tno=input("Enter train number")
  global boardingstaion,unboardingstation,date,ac1,ac2,ac3,sl,st
  if(tno in trains):
    boardingstaion=input("Enter boarding station: ")
    unboardingstation=input("Enter unboarding station: ")
    date=input("Enter date of travel in the format dd.mm.yyyy: ")
    # Define a dictionary to represent the available seats in each class
    ac1=random.randint(0,20)
    ac2=random.randint(0,50)
    ac3=random.randint(0,80)
    sl=random.randint(0,150)
    st=random.randint(0,300)
    seats = {
    "First AC": {
        "Available": ac1
        
    },
    "Second AC": {
        "Available": ac2
        
    },
    "Third AC": {
        "Available": ac3
        
    },
    "Sleeper": {
        "Available": sl
        
    },
    "Sitting": {
        "Available": st
       
    }
  }

# Print the available seats for each class
  print("Available Seats:")
  for class_name, seat_info in seats.items():
    available_seats = seat_info["Available"]
    print(f"{class_name}: {available_seats}")


def ticketbooking():
  fare=0
  berth=["upper",'middle',"lower","Side upper","side lower"]
  n=int(input("Enter number of tickets you wish to book: "))
  for i in range(1,n+1):
   nm=input(f"Enter name of passenger {i} ")
   ag=int(input(f"Enter age of passenger {i} "))
   cl=int(input("choose preffered seating class:\n 1.First Ac \n 2.Second Ac \n 3.Third Ac \n 4.Sleeper \n 5.Seating \n "))
   if(cl==1):
    cla='First Ac'
    fare+=2000
    
   elif(cl==2):
    fare+=1500
    cla="Second Ac"
    
   elif(cl==3):
    fare+=1000
    cla="Third Ac"
     
   elif(cl==4):
    fare+=700
    cla="Sleeper"
    
   elif(cl==5):
    fare+=300
    cla="Sitting"
    
   else:
    print("Error, select a number between 1,5")      

   if(ag>55):
    berth=["Side lower","Lower"]

    

   tickets.update({pnr:{"          Name : ":nm,"         Age : ":ag," Class: ":cla," Berth : ":random.choice(berth),"PNR: ":pnr,"       Boarding Station: ":boardingstaion,"Unboarding Station: ":unboardingstation,"Date: ":date}})
  print(pd.DataFrame.from_dict(tickets, orient='index').reset_index(drop=True))
  print(f"Payment Due= {fare}")
  num=int(input("Enter UPI id: "))
  upi_ps=int(input("Enter UPI password: "))
  if(num==upi.upi_id and upi_ps==upi.upi_pin):
    print("Ticket Booked succesfully")
  else:
    print("Wrong id or password, ticket not booked")   
  

def cancel_ticket():
    a=int(input("Enter pnr number of the ticket to cancel"))
    if a in tickets:
        del tickets[a]
        print("Your ticket has been deleted")

    else:
        print("PNR not found")


def pnr_status():
    a=int(input("Enter pnr number of the ticket "))
    if a in tickets:
        print("Booking is confirmed")
    else:
        print("PNR not found") 


def display_booked_tickets():
    print(print(pd.DataFrame.from_dict(tickets, orient='index').reset_index(drop=True)) )           


def main():
  while True:
    display_menu()
    choice = int(input())
    if choice == 1:
      # Implement train search functionality
      trains_available()
      pass
    elif choice == 2:
      seat_availability()
      # Implement seat availability check functionality
      pass
    elif choice == 3:
        ticketbooking() # Implement ticket booking functionality
    elif choice == 4:
      cancel_ticket()# Implement ticket cancellation functionality
      pass
    elif choice == 5:
      pnr_status()# Implement PNR status check functionality
      pass
    elif choice == 6:
      display_booked_tickets()# Implement view Fare= tickets functionality
      pass
    elif choice == 7:
      exitf()
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()
