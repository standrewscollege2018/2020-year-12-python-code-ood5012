#This is a programme to book flights and accomodation for a holiday
#Oliver Odlin
#27/2/2020

#This is a list for the location and the costs
locations = [["Sydney",326,120],["Tonga",378,40],["Shanghai",1436,60],["London",2376,80]]
#This list is for the departure locations of the passangers and cost to flight return from each
departures = [["Auckland",0],["Wellington",100],["Christchurch",150]]
#This for loop is to display the destinations
print("Destinations")
for location in range(0,len(locations)):
    print(location+1,locations[location][0])
#This loop shows the departure locations
print("Departure locations")
for departure in range(0,len(departures)):
    print(departure+1,departures[departure][0])
#Asks for the departure location for the passanger
departure_choice = int(input("Where do you want to leave from(use index number)?"))
#Input for choosing what place you would like to travel to
location_choice = int(input("Where would you like to travel(use index number)?"))
nights_stay = int(input("How many nights would you like to stay?"))
#Calculates price based on place and nights and then prints it
price_flights = locations[location_choice-1][1]+departures[departure_choice-1][1]
price_accommodation = locations[location_choice-1][2]*nights_stay
#Constants for both discount and discount threshhold
DISCOUNT_THRESHHOLD = 3
DISCOUNT = 0.8
#Calculate the discount if the nights staying is over 3
if nights_stay >= DISCOUNT_THRESHHOLD:
    price_accommodation = price_accommodation*DISCOUNT
price = price_flights + price_accommodation
print (price)
