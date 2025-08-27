import json
import os

# storing data in JSON so it doesn’t reset when we close the program
DATA_FILE = "library_data.json"

# load from file if exists, otherwise start fresh
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

# save changes back to file
def save_data(books):
    with open(DATA_FILE, "w") as f:
        json.dump(books, f, indent=4)

# add a book with total copies and available copies
def add_book(books):
    title = input("Enter book title: ").strip()
    author = input("Enter book author: ").strip()
    quantity = int(input("Enter quantity: "))
    books.append({
        "title": title,
        "author": author,
        "total_quantity": quantity,      # how many library owns
        "available_quantity": quantity   # how many are not borrowed
    })
    save_data(books)
    print(f"✅ Book '{title}' added successfully!")

# show all books
def display_books(books):
    if not books:
        print("📚 No books in the library.")
        return
    print("\n--- Library Books ---")
    for i, book in enumerate(books, 1):
        print(f"{i}. {book['title']} by {book['author']} "
              f"(Available: {book['available_quantity']} / {book['total_quantity']})")

# search by title or author
def search_book(books):
    keyword = input("Enter title or author to search: ").strip().lower()
    found_books = [book for book in books if keyword in book['title'].lower() or keyword in book['author'].lower()]
    if not found_books:
        print("❌ No matching books found.")
    else:
        print("\n--- Search Results ---")
        for book in found_books:
            print(f"{book['title']} by {book['author']} "
                  f"(Available: {book['available_quantity']} / {book['total_quantity']})")

# borrow decreases available (but not below zero)
def borrow_book(books):
    title = input("Enter book title to borrow: ").strip().lower()
    for book in books:
        if book['title'].lower() == title:
            if book['available_quantity'] > 0:
                book['available_quantity'] -= 1
                save_data(books)
                print(f"📖 You borrowed '{book['title']}'. Enjoy reading!")
            else:
                print("❌ Sorry, no copies available right now.")
            return
    print("❌ Book not found.")

# return increases available (but not beyond total)
def return_book(books):
    title = input("Enter book title to return: ").strip().lower()
    for book in books:
        if book['title'].lower() == title:
            if book['available_quantity'] < book['total_quantity']:
                book['available_quantity'] += 1
                save_data(books)
                print(f"✅ You returned '{book['title']}'. Thank you!")
            else:
                print("⚠ All copies are already in the library.")
            return
    print("❌ Book not found in our records.")

# main loop
def main():
    books = load_data()
    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Display All Books")
        print("3. Search Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_book(books)
        elif choice == "2":
            display_books(books)
        elif choice == "3":
            search_book(books)
        elif choice == "4":
            borrow_book(books)
        elif choice == "5":
            return_book(books)
        elif choice == "6":
            save_data(books)
            print("💾 Data saved. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()