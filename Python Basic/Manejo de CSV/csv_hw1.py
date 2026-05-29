import csv


def games_data():
    
    counter = 0
    name = []
    genre = []
    developer = []
    esrb_class = []

    try:
        game_quantity = int(input("Inserte la cantidad de juegos que desea registrar: "))
    except ValueError as ex:
        print(f"Error: Inserte el valor en formato de numero: {ex}")
        return

    while counter < game_quantity:
        name.append(input("Ingrese el nombre del videojuego: "))
        genre.append(input("Ingrese el genero del videojuego: "))
        developer.append(input("Ingrese el desarrollador del videojuego: "))
        esrb_class.append(input("Ingrese la clasificacion del videojuego: "))
        print("La informacion de tu videojuego se ha registrado con exito")
        counter += 1

    top_games = [
        {
            "Name": n,
            "Genre": g,
            "Developer": d,
            "ESRB Classification": e,
        }
        for n, g, d, e in zip(name, genre, developer, esrb_class)
    ]

    return top_games


def csv_games_file(games_csv, games_data):
    with open(games_csv, 'w', encoding="UTF-8", newline='') as file:
        headers = games_data[0].keys()
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(games_data)


def tsv_games_dialect(filename, games_data):
    with open(filename, 'w', encoding="UTF-8", newline='') as file:
        headers = games_data[0].keys()
        writer = csv.DictWriter(file, fieldnames=headers, dialect='excel-tab')
        writer.writeheader()
        writer.writerows(games_data)


if __name__ == "__main__":
    game_list = games_data()
    csv_games_file("Top_5_Games.csv", game_list)
    tsv_games_dialect("Top_5_Games_dialect.tsv", game_list)