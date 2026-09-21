import pickle

FILENAME = "movies.bin"

def write_movies(movies):
    with open(FILENAME, "wb") as file:
        pickle.dump(movies, file)

def read_movies():
    with open(FILENAME, "rb") as file:
        movies = pickle.load(file)
    return movies

def list_movies(movies):
    movies = read_movies()
    for i, movie in enumerate(movies, start=1):
        print(f"{i}. {movie[0]} ({movie[1]})")
    print()

def add_movie(movies):
    name = input("Name: ")
    year = input("Year: ")
    movie = [name, year]
    movies.append(movie)
    write_movies(movies)
    print(f"{name} was added.\n")

def delete_movie(movies):
    index = int(input("Number: "))
    if index < 1 or index > len(movies):
        print("Invalid movie number.\n")
    else:
        movie = movies.pop(index - 1)
        write_movies(movies)
        print(f"{movie[0]} was deleted.\n")
        
def display_menu():
    print("The Movie List program")
    print()
    print("COMMAND MENU")
    print("list - List all movies")
    print("add -  Add a movie")
    print("del -  Delete a movie")
    print("exit - Exit program")
    print()

def main():
    display_menu()
    movies = read_movies()
    while True:        
        command = input("Command: ")
        match command.lower():
            case "list":
                list_movies(movies)
            case "add":
                add_movie(movies)
            case "del":
                delete_movie(movies)
            case "exit":
                print("Bye!")
                break
            case _:
                print("Not a valid command. Please try again.")

if __name__ == "__main__":
    main()
