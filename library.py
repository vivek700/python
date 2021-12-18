class Library:
    
    def __init__(self,list_of_books):
        self.books = list_of_books
        
        
    
    def DisplayAvailableBooks(self):
        for index,book in enumerate(self.books):
            print(f"\t{index+1} {book}")

    def BorrowBook(self,bookName):
        if bookName in self.books:
            print(f"\nYou have been issued {bookName}. Please keep it safe and return it within 30 days")       
            self.books.remove(bookName)
            s = "\n".join(self.books)
            with open("books.txt",'w') as f:
                f.write(s)

                
        else:
            print("Sorry! This book is alredy issued to someone else or unavailabe.")    

    def AddBook(self,bookname):
        if bookname !="":
            self.books.append(bookname)
            print("\nThis book is Successfully added!")
            v = "\n".join(self.books)
            with open("books.txt",'w') as f:
                f.write(v)        
        else:
            print("Invalid book name.")    

class Student:

    def __init__(self):
        self.reqlist = []

    def DisplayIssuedBook(self):
        for i,book in enumerate(self.reqlist):
            print(f"{i+1} {book}")    
    

    def reqBook(self):
        self.book = input("Enter the name of the which you want to borrow: ")
        self.reqlist.append(self.book)
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the which you want to return/add: ")
        if self.book in self.reqlist:
            self.reqlist.remove(self.book)      
        else:    
            return self.book

        
if __name__ == "__main__":
    with open("books.txt",'r') as f:
        l = []
        for i in f:
            l.append(i.rstrip())
    
      
    Y = Library(l)
    s = Student()

    while(True):
        wlcmMessage = '''\n************* Welcome To Y Library *************
        Please choose an option:
        1. List all available books
        2. Request a book
        3. Return/Add a book
        4. Exit the library
        '''
        print(wlcmMessage)
        a = int(input("Enter your choice: "))
        if a == 1:
            Y.DisplayAvailableBooks()
        elif a == 2:
            Y.BorrowBook(s.reqBook())    
        elif a == 3:
            Y.AddBook(s.returnBook())
        elif a == 4:
            print("Thanks for using Y library. Have a nice day!")
            exit()  
        else:
            print("Invailid option!")      
