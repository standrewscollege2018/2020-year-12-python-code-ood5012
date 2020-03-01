#This is a programme to book flights and accomodation for a holiday
#Oliver Odlin
#27/2/2020

#This is a list for the location and the costs
locations = [["Sydney",326,120],["Tonga",378,40],["Shanghai",1436,60],["London",2376,80]]

#This for loop is to display the destinations

for location in range(0,len(locations)):
    print(location+1,locations[location][0])
#Input for choosing what place you would like to travel to
location_choice = int(input("Where would you like to travel(use index number)?"))
nights_stay = int(input("How many nights would you like to stay?"))
#Calculates price based on place and nights and then prints it
price_flights = locations[location_choice-1][1]
price_accommodation = locations[location_choice-1][2]*nights_stay
price = price_flights + price_accommodation
print (price)
