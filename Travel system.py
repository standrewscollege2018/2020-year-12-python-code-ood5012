#This is a programme to book flights and accomodation for a holiday
#Oliver Odlin
#27/2/2020

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
        print(departure+1,departures[departure][0])
#This for loop is to display the destinations
    print("Destinations")
    for location in range(0,len(locations)):
        print(location+1,locations[location][0])
#Asks for the departure location for the passanger
    departure_choice = int(input("Where do you want to leave from(use index number)?"))
#Input for choosing what place you would like to travel to
    location_choice = int(input("Where would you like to travel(use index number)?"))
    nights_stay = int(input("How many nights would you like to stay?"))
#Calculates price based on place and nights and then prints it
    price_flights = locations[location_choice-1][1]+departures[departure_choice-1][1]
    price_accommodation = locations[location_choice-1][2]*nights_stay
    price_accommodtaion_after = price_accommodation
#Constants for both discount and discount threshhold
    DISCOUNT_THRESHHOLD = 3
    DISCOUNT = 0.8
#Calculate the discount if the nights staying is over 3
    if nights_stay >= DISCOUNT_THRESHHOLD:
        price_accommodation_after = price_accommodation*DISCOUNT
    price = price_flights + price_accommodation
    print ("Flights cost $",price_flights)
    print ("Accommodation orignally costs $",price_accommodation)
    print ("After 3 night or over discount $",price_accommodation_after)
    print ("Total $",price)
#Input for confirmation
    confirmation = int(input("If you would like to confirm the trip enter 1, if you want to change enter 2."))
    if confirmation == 1:
        running = False
    
