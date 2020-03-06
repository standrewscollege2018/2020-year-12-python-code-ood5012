"""This program is used to book flights and accommodation for vacations"""
"""Oliver Odlin"""
"""03/03/20"""
def error_catching (message,input_range_low,input_range_high):
    """This function is for error catching integer inputs"""
    running = True
    while running == True:
        try:
            user_input = int(input(message))
            if user_input in range(input_range_low,input_range_high):
                running = False
            else:
                print("Enter a valid number")
        except:
            print("Enter a valid number")
    return user_input
#This is a list for the location and the costs
locations = [["Sydney",326,120],["Tonga",378,40],["Shanghai",1436,60],["London",2376,80]]
#This list is for the departure locations of the passangers and cost to flight return from each
departures = [["Auckland",0],["Wellington",100],["Christchurch",150]]
#Variable for while loop
running = True
#While loop so customer can repeat until they confirm the trip
while running == True:
#This loop shows the departure locations
    print("Departure locations")
    for departure in range(0,len(departures)):
        print(departure+1,departures[departure][0],"Cost $",departures[departure][1],"one-way")
#Asks for the departure location for the passanger
    departure_choice = error_catching("Where do you want to leave from(use index number)?",0,len(departures)+1)
#This for loop is to display the destinations
    print("Destinations")
    for location in range(0,len(locations)):
        print(location+1,locations[location][0],"Cost $",locations[location][1],"return flights")
#Asks for the departure location for the passanger
#Input for choosing what place you would like to travel to
    location_choice = error_catching("Where would you like to travel(use index number)?",0,len(locations)+1)
    nights_stay = error_catching("How many nights would you like to stay?",1,122)
#Calculates price based on place and nights and then prints it
    price_flights = locations[location_choice-1][1]+departures[departure_choice-1][1]
    price_accommodation = locations[location_choice-1][2]*nights_stay
    price_accommodtaion_after = price_accommodation
#Constants for both discount and discount threshhold
    DISCOUNT_THRESHHOLD = 3
    DISCOUNT = 0.8
    customer_discount = 0
#Calculate the discount if the nights staying is over 3
    if nights_stay >= DISCOUNT_THRESHHOLD:
        price_accommodation_after = price_accommodation*DISCOUNT
        customer_discount = (1-DISCOUNT)*nights_stay*locations[location_choice-1][2]
    price = price_flights + price_accommodation
    print ("Flights $",price_flights)
    print ("Accommodation $",price_accommodation)
    print ("Accomodation discount -$",customer_discount)
    print ("Total $",price)
#Input for confirmation
    confirmation = error_catching("If you would like to confirm the trip enter 1, if you want to change enter 2.",1,3)
    if confirmation == 1:
        running = False
        print("Your trip has been booked")
    else:
        print("Rebooking...")
    
