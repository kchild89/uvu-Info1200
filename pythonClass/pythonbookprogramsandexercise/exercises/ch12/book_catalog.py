#!/usr/bin/env python3

# helper functions
def get_title():
    title = input("Title: ")
    return title

def update_catalog(book_catalog, title):
    author = input("Author name: ")
    pubyear = input("Publication year: ")
    
    book = {title: {"author": author, "pubyear": pubyear}}  # create dictionary
    book_catalog |= book                  # add to catalog with update operator

# functions called in main
def show_book(book_catalog):
    title = get_title()
    if title in book_catalog:
        book = book_catalog[title]
        print(f"Title:    {title}")
        print(f"Author:   {book['author']}")
        print(f"Pub year: {book['pubyear']}")
    else:
        print(f"Sorry, {title} doesn't exist in the catalog.")

def add_book(book_catalog):
    title = get_title()
    if title in book_catalog:
        print(f"{title} already exists in the catalog.")
        response = input("Would you like to edit it? (y/n): ").lower()
        if response != "y":
            return

    update_catalog(book_catalog, title)
    
def edit_book(book_catalog):
    title = get_title()
    if title not in book_catalog:
        print(f"{title} doesn't exist in the catalog.")
        response = input("Would you like to add it? (y/n): ").lower()
        if response != "y":
            return

    update_catalog(book_catalog, title)

def delete_book(book_catalog):
    title = get_title()
    if title in book_catalog:
        del book_catalog[title]
        print(f"{title} removed from catalog.")
    else:
        print(f"{title} doesn't exist in the catalog.")

def display_menu():
    print("The Book Catalog program")
    print()
    print("COMMAND MENU")
    print("show - Show book info")
    print("add -  Add book")
    print("edit - Edit book")
    print("del -  Delete book")
    print("exit - Exit program")

def main():
    book_catalog = {
        "Moby Dick": {"author": "Herman Melville", "pubyear": "1851"},
        "The Hobbit": {"author": "J. R. R. Tolkien", "pubyear": "1937"},
        "Kindred": {"author": "Octavia Butler", "pubyear": "1979"}
    }
    
    display_menu()
    
    while True:
        print()
        command = input("Command: ").lower().strip()
        match command:
            case "show":
                show_book(book_catalog)
            case "add":
                add_book(book_catalog)
            case "edit":
                edit_book(book_catalog)
            case "del":
                delete_book(book_catalog)
            case "exit":
                print("Bye!")
                break
            case _:
                print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()
