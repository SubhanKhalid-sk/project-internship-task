Library Management System

Author: Subhan Khalid

Overview

The Library Management System is a console-based Python program designed to manage books in a library. It provides a simple menu interface where users can add books, display the full collection, search for specific titles or authors, borrow books, and return them. To ensure data persistence, the system stores all records in a JSON file so that information is not lost after closing the program.

Features

Add books with details like title, author, and total quantity

Display all available books with their availability status

Search for books by entering part of the title or author’s name

Borrow and return books with checks to avoid invalid actions

Save and load data automatically using library_data.json


Requirements

Python 3.x

Built-in modules: json, os


How to Run

1. Download or clone this repository


2. Open a terminal or command prompt inside the project folder


3. Run the program using the command: python LibraryManagementSystem.py


4. Follow the menu instructions to perform operations



Notes

The file library_data.json will be created automatically if it does not exist

Enter valid inputs (for example, numbers for quantity) to avoid errors


Conclusion

This project demonstrates file handling, JSON data storage, and menu-driven programming in Python. It was developed as part of an internship task.
