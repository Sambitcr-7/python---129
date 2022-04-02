class Library:


    def __init__(self,ListOfBooks):
        self.books = ListOfBooks
    def display(self):
        pass
    def displayAvailableBook(self):
        print("Books present in the library are:")
        for book in self.book:
            print(" *" + book)
    
    def borrowBook(self, bookName):
        if bookName in self.book:
            print(f"You have been issued {bookName}.Please keep it safe and return it within 30 days ")
            self.book.remove(bookName)


        else:
            print("sorry, This book is either not avilable or  has already been issued to someone elsa, Please wait until the book is returned")  
            return True  

    def returnBook(self, bookName):
        self.book.append(bookName)
        print("Thanks for returing this book! Hope you enjoyed reading it. Have a great day ahead!")        



class student:
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return")    
        return self.book

if __name__=="__main__":
    centralLibrary = Library(["Algorithms","Django","Clrs","Python Notes"])
    centralLibrary.displayAvailableBook()
    while(True):
        welcomeMsg = '''======Welcome to e=central Library==========
        Plese choose an option :
        1.Listing all the books
        2.Request a book
        3.Return a book
        4.Exit the Library
        '''
        
        a = int(input("Enter a choice:"))
        if a == 1:
            centralLibrary.displayAvailableBook()
        elif a == 2:
            centralLibrary.displayAvailableBook()
        elif a== 3:
            centralLibrary.displayAvailableBook()
        elif a == 4:
            print("Thanks for choosing Central Library.Have a great day ahead!")
            exit()
        else:
            print("Invalid Choice!")       


        print(welcomeMsg)
