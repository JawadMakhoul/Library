library = [
    {"Title": "1984", "Authors": "George Orwell", "Genre": "Dystopian", "Publication Year": 1949},
    {"Title": "To Kill a Mockingbird", "Authors": "Harper Lee", "Genre": "Fiction", "Publication Year": 1960}
]

# Search books by title
def find_by_title(title):
    results = []

    for book in library:
        if book["Title"].lower() == title.lower():
            results.append(book)
    return results

# Search books by author
def find_by_author(author):
    results = []

    for book in library:
        if book["Authors"].lower() == author.lower():
            results.append(book)
    return results

# Add a new book
def add_book(title, authors, genre, publication_year, bookID, copies):
    new_book = { "Title": title, "Authors": authors, "Genre": genre, "Publication Year": publication_year}

    if bookID:
        new_book["BKID"] = bookID
    if copies:
        new_book["Number of Copies"] = copies

    library.append(new_book)

# Menu for user interaction
def menu():
    while True:
        print("\nLibrary Management System")
        print("1. Find a book by Title")
        print("2. Find a book by Author")
        print("3. Add a new book")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter the book title: ")
            books = find_by_title(title)
            if books:
                print("Books found:", books)
            else:
                print("No books found with that title.")

        elif choice == "2":
            author = input("Enter the author's name: ")
            books = find_by_author(author)
            if books:
                print("Books found:", books)
            else:
                print("No books found by that author.")

        elif choice == "3":
            title = input("Enter the book title: ")
            authors = input("Enter the author name: ")
            genre = input("Enter the genre: ")
            year = input("Enter the publication year: ")
            bookID = input("Enter the Book ID (optional): ") or None
            copies = input("Enter the number of copies (optional): ") or None
            add_book(title, authors, genre, year, bookID, copies)
            print("Book added successfully!")

        elif choice == "4":
            print("Exut!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()