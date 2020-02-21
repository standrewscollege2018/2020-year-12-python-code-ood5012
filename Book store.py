#This programme is to store, display and edit books in a list
#Ollie Odlin
#18/2/20
#This version stores books in a list including title author and price
#This is a list with each book including title, author and price
books = [["Fight Club","Chuck Palahniuk",20],["Inferno","Dan Brown",25],["Shawshank Redemption","Stephen King",15],["Shoe Dog","Phil Knight",30]]
#This is a variable that controls the while loop
running = True
#This while loop is to continue to the code until a user wants it to stop
while running == True:
#This for loop prints the book titles, authors and price
    for book in range (0, len(books)):
        print(book+1,books[book][0],"by",books[book][1],"$",books[book][2])
    print ('''Menu
    1. Add book
    2. Delete book
    3.Change book details
    4.Stop running''')
#Error catching for choosing a valid menu option using try and except
    validOption = True
    while validOption == True:
        try:
            menuChoice = int(input("What do you want to do?"))
            if menuChoice in range (1,5):
                validOption = False
            else:
                print("Choose a valid number")
        except:
            print("Choose a number")
    #Adding a book
    if menuChoice == 1:
#Asking for new book details where user can input
        newBookTitle = input("What is the title of the new book?")
        newBookAuthor = input("Who is the author of the new book?")
        validOption = True
        while validOption == True:
            try:
                newBookPrice = int(input("What is the price of the new book?"))
                validOption = False
            except:
                print("Choose a number")
#Appends all information to a new list
        newBook =[]
        newBook.append(newBookTitle)
        newBook.append(newBookAuthor)
        newBook.append(newBookPrice)
#Adds list to master book list
        books.append(newBook)
#Deletes a book
    elif menuChoice == 2:
        validOption = True
        while validOption == True:
            try:
                delBook = int(input("What book would you like to delete(use book index number)?"))
                if delBook in range (1,(len(books)+1)):
                    validOption = False
                else:
                    print("Choose a valid number")
            except:
                print("Choose a number")
        del books [delBook-1]
#Code to change book details
    elif menuChoice == 3:
#Find what book to change
        validOption = True
        while validOption == True:
             try:
                bookChange = int(input("What book do you want to change(use book index number)?"))
                if bookChange in range (1,(len(books)+1)):
                    validOption = False
                else:
                    print("Choose a valid number")
             except:
                print("Choose a number")
#Find the information to change about the book
        validOption = True
        while validOption == True:
             try:
                changeFrom = int(input('''What part of the book do you want to change(Use number)
1:Title
2:Author
3:Price'''))
                if changeFrom in range (1,4):
                    validOption = False
                else:
                    print("Choose a number")
             except:
                print("Choose a number")
        
#User input for the new information for the book
#If the price is being changed it must be an integer
        if changeFrom == 3:
            validOption = True
#THis is to get a correct input
            while validOption == True:
                try:
                    changeTo = int(input("What is the new price?"))
                    validOption = False
                except:
                  print("Choose a number")
        if changeTo == 2:
            changeTo = input("What is the new author?")
        if changeTo == 1:
            changeTo = input("What is the new title?")
        books[bookChange-1][changeFrom-1] = changeTo
    elif menuChoice == 4:
        running = False

        



    
    
    
