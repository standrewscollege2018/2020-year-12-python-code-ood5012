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
    3.Stop running''')
    menuChoice = int(input("What do you want to do?"))
    #Adding a book
    if menuChoice == 1:
#Asking for new book details where user can input
        newBookTitle = input("What is the title of the new book?")
        newBookAuthor = input("Who is the author of the new book?")
        newBookPrice = int(input("What is the price of the new book?"))
#Appends all information to a new list
        newBook =[]
        newBook.append(newBookTitle)
        newBook.append(newBookAuthor)
        newBook.append(newBookPrice)
#Adds list to master book list
        books.append(newBook)
#Deletes a book
    elif menuChoice == 2:
        delBook = int(input("What book would you like to delete(use book index number)?"))
        del books [delBook-1]
    else:
        running = False

        



    
    
    
