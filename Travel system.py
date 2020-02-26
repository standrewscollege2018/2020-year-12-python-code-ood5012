#This is a programme to book flights and accomodation for a holiday
#Oliver Odlin
#27/2/2020

#This is a list for the location and the costs
locations = [["Sydney",326,120],["Tonga",378,40],["Shanghai",1436,60],["London",2376,80]]

#This for loop is to display the destinations

for location in range(0,len(locations)):
    print(location+1,locations[location][0])
