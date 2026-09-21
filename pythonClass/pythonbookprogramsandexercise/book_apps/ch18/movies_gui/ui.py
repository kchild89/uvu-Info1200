#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk, messagebox

import db
from objects import Movie

class MoviesFrame(ttk.Frame):
    def __init__(self, parent):
        # Initialize the frame and keep a reference to the parent window.
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.parent = parent
        self.initComponents()

    def initComponents(self):
        self.pack()

        # Filter frame (top)
        filterFrame = ttk.LabelFrame(self, text="View Movies")
        filterFrame.grid(column=0, row=0, columnspan=2, 
                         sticky=tk.EW, pady=(0, 5))

        # Read category objects from db and get list of names
        self.categories = db.get_categories()
        categoryNames = []
        for c in self.categories:
            categoryNames.append(c.name)

        # Category filter
        ttk.Label(filterFrame, text="Category:").grid(
            column=0, row=0, sticky=tk.E, padx=5, pady=3)
        self.categoryCombo = ttk.Combobox(filterFrame, width=22,
            values=categoryNames, state="readonly")
        self.categoryCombo.grid(column=1, row=0, padx=5, pady=3)
        self.categoryCombo.bind("<<ComboboxSelected>>", self.viewByCategory)

        # Treeview frame (middle)
        treeFrame = ttk.Frame(self)
        treeFrame.grid(column=0, row=1, columnspan=2, 
                       sticky=tk.NSEW, pady=5)

        columns = ("id", "name", "year", "minutes", "category")
        self.tree = ttk.Treeview(treeFrame, columns=columns,
                                 show="headings", height=6)
        self.tree.heading("id",       text="ID",       anchor=tk.W)
        self.tree.heading("name",     text="Name",     anchor=tk.W)
        self.tree.heading("year",     text="Year",     anchor=tk.W)
        self.tree.heading("minutes",  text="Mins",     anchor=tk.W)
        self.tree.heading("category", text="Category", anchor=tk.W)
        self.tree.column("id",       width=40,  anchor=tk.W)
        self.tree.column("name",     width=280, anchor=tk.W)
        self.tree.column("year",     width=55,  anchor=tk.W)
        self.tree.column("minutes",  width=50,  anchor=tk.W)
        self.tree.column("category", width=100, anchor=tk.W)

        scrollbar = ttk.Scrollbar(treeFrame, orient=tk.VERTICAL,
                                  command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.grid(column=0, row=0, sticky=tk.NSEW)
        scrollbar.grid(column=1, row=0, sticky=tk.NS)

        # Frame for adding a new movie (bottom left)
        addFrame = ttk.LabelFrame(self, text="Add Movie")
        addFrame.grid(column=0, row=2, sticky=tk.NSEW, padx=(0, 5), pady=5)

        ttk.Label(addFrame, text="Name:").grid(
            column=0, row=0, sticky=tk.E, padx=5, pady=3)
        self.nameVar = tk.StringVar()
        ttk.Entry(addFrame, width=40, textvariable=self.nameVar).grid(
            column=1, row=0, padx=5, pady=3)

        ttk.Label(addFrame, text="Year:").grid(
            column=0, row=1, sticky=tk.E, padx=5, pady=3)
        self.yearVar = tk.StringVar()
        ttk.Entry(addFrame, width=40, textvariable=self.yearVar).grid(
            column=1, row=1, padx=5, pady=3)

        ttk.Label(addFrame, text="Minutes:").grid(
            column=0, row=2, sticky=tk.E, padx=5, pady=3)
        self.minutesVar = tk.StringVar()
        ttk.Entry(addFrame, width=40, textvariable=self.minutesVar).grid(
            column=1, row=2, padx=5, pady=3)

        ttk.Label(addFrame, text="Category:").grid(
            column=0, row=3, sticky=tk.E, padx=5, pady=3)
        self.addCategoryCombo = ttk.Combobox(addFrame, width=37,
            values=categoryNames, state="readonly")
        self.addCategoryCombo.grid(column=1, row=3, padx=5, pady=3)

        # Preselect the first category if categories are available
        if categoryNames:
            self.addCategoryCombo.current(0)

        addButton = ttk.Button(addFrame, text="Add Movie",
                               command=self.addMovie)
        addButton.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)
        addButton.bind("<Return>", self.addMovie)

        # Frame for deleting a movie (bottom right)
        deleteFrame = ttk.LabelFrame(self, text="Delete Movie")
        deleteFrame.grid(column=1, row=2, sticky=tk.NSEW, pady=5)

        deleteButton = ttk.Button(deleteFrame, text="Delete Movie",
                                   command=self.deleteMovie)
        deleteButton.grid(column=0, row=0, sticky=tk.E, padx=5, pady=5)
        deleteButton.bind("<Return>", self.deleteMovie)

        # Exit button
        exitButton = ttk.Button(self, text="Exit", command=self.exit)
        exitButton.grid(column=1, row=3, sticky=tk.E, pady=5)
        exitButton.bind("<Return>", self.exit)
              
    def viewByCategory(self, event=None):
        # Show movies in the selected category
        index = self.categoryCombo.current()
        category = self.categories[index]                # get Category obj
        movies = db.get_movies_by_category(category.id)  # get Movie objects
        self.populateTree(movies)

    def populateTree(self, movies):
        # Delete current rows, then insert one row for each movie
        for row in self.tree.get_children():
            self.tree.delete(row)
        for m in movies:
            self.tree.insert("", tk.END, values=(
                m.id, m.name, m.year, m.minutes, m.category.name))

    def addMovie(self, event=None):
        # Validate the new movie data before adding it to the database.
        add_message = ""
        name = self.nameVar.get().strip()
        if not name:
            add_message += "Name is required.\n"
        try:
            year = int(self.yearVar.get())
        except ValueError:
            add_message += "Year must be a valid integer.\n"
        try:
            minutes = int(self.minutesVar.get())
        except ValueError:
            add_message += "Minutes must be a valid integer.\n"

        if add_message:
            messagebox.showerror("Error", add_message)
            return

        # Create a Movie object and save it to the database
        index = self.addCategoryCombo.current()   # get selected index
        category = self.categories[index]         # get category object
        movie = Movie(name=name, year=year, minutes=minutes, 
                      category=category)
        db.add_movie(movie)

        # Clear the input fields and refresh the displayed list
        self.nameVar.set("")
        self.yearVar.set("")
        self.minutesVar.set("")
        self.categoryCombo.set(category.name)
        self.viewByCategory()

    def deleteMovie(self, event=None):
        selected = self.tree.selection()
        if not selected:
            messagebox.showerror("Error", "Please select a movie.")
            return
        row = selected[0]
        movie = self.tree.item(row)["values"]
        movie_id = movie[0]
        movie_name = movie[1]
        confirm = messagebox.askyesno(
            "Confirm Delete",
            f"Delete {movie_name}?")
        if confirm:
            db.delete_movie(movie_id)
            self.viewByCategory()

    def exit(self, event=None):
        self.parent.destroy();

if __name__ == "__main__":
    db.connect()
    root = tk.Tk()
    root.title("Movie List")
    MoviesFrame(root)
    root.mainloop()
    db.close()