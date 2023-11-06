# Define a class called "Library" to represent a library with various book-related operations.
class Library:
    # Initialize the library with a list of books, a name, and an empty dictionary to track book loans.
    def __init__(self, book_list, name):
        self.booklist = book_list
        self.name = name
        self.lentdict = {}  # A dictionary to map books to the person who has borrowed them.

    # Display the list of books available in the library.
    def displayBooks(self):
        print(f"We have the following books in the {self.name} library:")
        for book in self.booklist:
            print(book)

    # Allow a user to lend a book, updating the book-owner dictionary.
    def lendBook(self, user, book):
        if book not in self.lentdict.keys():
            self.lentdict.update({book: user})
            print("Lender-Book database has been updated. You can take the book now.")
        else:
            print(f"The book is already being used by {self.lentdict[book]}")

    # Add a book to the library's collection.
    def addBook(self, book):
        self.booklist.append(book)
        print("The book has been added to the book list.")

    # Return a book to the library, removing it from the book-owner dictionary.
    def returnBook(self, book):
        self.lentdict.pop(book)

# Check if this script is the main program entry point.
if __name__ == '__main__':
    # Create an instance of the Library class with an initial list of books and a library name.
    owes = Library(['python', 'Harry Potter and the Sorcerer’s Stone', ' 7 Habits of Highly Effective People', 'THINK AGAIN', 'ATOMIC HABITS'], "Public Library")

    # Start an infinite loop to interact with library operations.
    while True:
        print(f"Welcome to the {owes.name}. Enter your choice to continue:")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")

        user_choice = input()

        # Validate user input to ensure it's one of the available options (1, 2, 3, or 4).
        if user_choice not in ['1', '2', '3', '4']:
            print("Please enter a valid option.")
            continue
        else:
            user_choice = int(user_choice)

        # Perform the selected operation based on user input.
        if user_choice == 1:
            owes.displayBooks()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend: ")
            user = input("Enter your name: ")
            owes.lendBook(user, book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to add: ")
            owes.addBook(book)

        elif user_choice == 4:
            book = input("Enter the name of the book you want to return: ")
            owes.returnBook(book)

        else:
            print("Not a valid option")

        user_choice2 = ""
        print("Press 'q' to quit and 'c' to continue")
        
        # Allow the user to quit or continue the interaction loop.
        while user_choice2 != "c" and user_choice2 != "q":
            user_choice2 = input()
            if user_choice2 == "q":
                exit()  # Exit the program if 'q' is entered.

            elif user_choice2 == "c":
                continue  # Continue the loop if 'c' is entered.
