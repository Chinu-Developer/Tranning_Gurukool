import colorama
from colorama import  Fore ,Back , Style ,init 

def menu():
    init(autoreset=True)
    print(Fore.MAGENTA + '''╔══════════════════════════════════════════════╗
║                                              ║
║        📚  LIBRARY MANAGEMENT SYSTEM  📚     ║
║                                              ║
╚══════════════════════════════════════════════╝''')

    print(Fore.BLUE +''' 1.Add Book
2. View Book 
3.Search BOOK 
4.Register User
5.Issue Book 
6.Exit ''')   



def readbook():
    """This is a function which gives you the data of the book"""
    with open("book.txt", "r") as f:
        book_ele = f.readlines()
        return book_ele

def add_book():
    """This is a add book Function . It takes Book Id, Book Name, Author,Quantity as input """
    book_ele  = readbook()
    print(Fore.GREEN + "--- ADD BOOK ---" )
    book_name = input("Enter the Book name  :")
    for i in book_ele:
        if book_name in i:
            print(Fore.GREEN + "The Book Already Exists")
            print(Fore.RED + " Please use Update Function")
            return 10
    book_id = len(book_ele) + 1
    book_author = input("Enter author Name Please : ")
    print(Fore.GREEN + "Book Id is :: ", book_id)
        


    book_author = input("Enter author Name Please : ")
    print(Fore.GREEN + "Book Id is :: ", book_id)
    error_message = Fore.RED + "Invalid quantity entered \n Please Enter a valid Value"
    while True:
        book_quantity = input("Enter Quantity :").strip()
        if book_quantity.isdigit() :
            if int(book_quantity) > 0:
                book_quantity = int(book_quantity)
                break
            else:
                print(error_message)    
        else:
            print(error_message)
    print(Fore.GREEN + f'{"Book added successfully.":^100}')

    with  open("book.txt", "a") as f:
        f.write(f"{book_id}, {book_name}, {book_author}, {book_quantity} \n")

def Viewbook ():
    """ Thia a view book function this hepls you to view a exact Book """
    book_ele = readbook ()
    if len(book_ele)== 0 :
        print(Fore.RED + "There is no  Book to view ")
    else:
        for i in book_ele:
            i = i.replace("\n","")
            i = i.split()
            print(Fore.WHITE + f"Book id : {i[0]} Book Name :{i[1]} Book Author  : {i[2]} Book Quantity {i[3]}")      


def SearchBook(Praam):
    """ This is a Function which can be use to search a particular Book & which can be useful """
    book_ele = readbook()
    if len(book_ele) == 0:
        print(Fore.RED +" There is no Book Avalibal in Data base ")
    else:
        for i in book_ele:
            i = i.replace("\n","")
            i = i.split()
        if Praam.isdidgit():
            #  print(f"{i[0]} --> {type(i[0])}")
            # print(param, type(param))
            if i[0] == Praam + ",":
                 print("\n\n")
                 print(Fore.CYAN + f"Book Id : {i[0]} Book Name : {i[1]}  Book Author : {i[2]} Book_Quantity : {i[-1]} ")
                 return i 

                
             


















if __name__ == "__main__":
    while True:
        menu()
        choice = input("Enter Your Choice From 1 to 6 :: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            Viewbook() 
        elif choice == "3":
            print("Search Book")
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "6":
            print(Fore.GREEN +" Thankyou For Visiting, Please Visti Aagin ")
            break
        else:
            print(Fore.RED + "Invalid Choice") 

   

          

             
       
     
