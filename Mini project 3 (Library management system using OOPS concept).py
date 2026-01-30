"""Create a Library Management System where different library items calculate borrowing charges differently.
Library item (parent class)
Book and magazie (child class)
LibraryApp(main class)

Book IS-A libraryitem
Magazine IS-A libraryitem
LibraryApp HAS-A libraryitem

Output format
Item Type: Book
Borrow Days: 5
Borrowing Charge: 50
Or 
Item Type: Magazine
Borrow Days: 3
Borrowing Charge: 30
"""
#------Library Management System using OOPS concepts-----
#Abstraction
class Libraryitem:                                                 # Parent class
    def __init__(self,item_type,borrow_days):
        self.item_type = item_type
        self.borrow_days = borrow_days                             # Encapsulation
# Abstract Method
    def calculate_borrowing_charge(self):                          
        pass
# Inheritance
class Book(Libraryitem):                                           
    def __init__(self,item_type,borrow_days):
        super().__init__(item_type,borrow_days)
        self.borrow_days = borrow_days
#Polymorphism
    def calculate_borrowing_charge(self):
        return self.borrow_days  * 10
 # Inheritance
class Magzine(Libraryitem):                                       
    def __init__(self,item_type,borrow_days):
        super().__init__(item_type,borrow_days)
        self.borrow_days = borrow_days
#Polymorphism
    def calculate_borrowing_charge(self):
        return self.borrow_days  * 10
# HAS - A relationship
class LibraryApp:
    def __init__(self):
        self.item = None
    def  create_item(self, item_type, borrow_days):
        if item_type == "Book":
            self.item = Book(item_type,borrow_days)
        elif item_type == "Magazine":
            self.item = Magzine(item_type,borrow_days)

    def show_details(self):
        print("Item Type:", self.item.item_type)
        print("Borrow Days:", self.item.borrow_days)
        print("Borrowing Charge:", self.item.calculate_borrowing_charge())
app = LibraryApp()
app.create_item("Book", 5)
app.show_details()
app2 = LibraryApp()
app2.create_item("Magazine", 3)
app2.show_details()


