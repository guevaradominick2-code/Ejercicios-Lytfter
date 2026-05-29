import json

def pokedex_reader(file_name):

    with open(file_name, 'r', encoding = "UTF-8") as file:
        return json.load(file)
    
def add_pokemon(pokemon_list):
    print("\n--- Agregar nuevo Pokémon ---")

    name = input("Nombre: ")
    pokemon_type = input("Tipo (ej: Fire, Water, Electric): ")
    
    try:
        level = int(input("Nivel: "))
        weight_kg = float(input("Peso (kg): "))
    except ValueError:
        print("Error: Nivel debe ser entero y peso debe ser número.")
        return pokemon_list

    is_shiny_input = input("¿Es shiny? (s/n): ").strip().lower()
    is_shiny = is_shiny_input == 's'

    held_item_input = input("Held item (dejar vacío si no tiene): ").strip()
    held_item = held_item_input if held_item_input else None

    print("Ingrese los skills (presione Enter sin texto para terminar):")
    skills = []
    while True:
        skill = input(f"  Skill {len(skills) + 1}: ").strip()
        if skill == "":
            break
        skills.append(skill)

    print("Ingrese las estadísticas:")
    try:
        stats = {
            "hp":         int(input("  HP: ")),
            "attack":     int(input("  Attack: ")),
            "defense":    int(input("  Defense: ")),
            "sp_attack":  int(input("  Sp. Attack: ")),
            "sp_defense": int(input("  Sp. Defense: ")),
            "speed":      int(input("  Speed: "))
        }
    except ValueError:
        print("Error: Las estadísticas deben ser números enteros.")
        return pokemon_list

    new_pokemon = {
        "name": name,
        "type": pokemon_type,
        "level": level,
        "weight_kg": weight_kg,
        "is_shiny": is_shiny,
        "held_item": held_item,
        "skills": skills,
        "stats": stats
    }

    pokemon_list.append(new_pokemon)
    print(f"\n¡{name} agregado con éxito!")
    return pokemon_list

def save_pokemon_file(filename, pokemon_list):
    with open(filename, 'w', encoding='UTF-8') as file:
        json.dump(pokemon_list, file, indent=3, ensure_ascii=False)
    print(f"Archivo '{filename}' guardado con éxito.")

if __name__ == "__main__":
    filename = "pokedex.json"

    pokemon_list = pokedex_reader(filename)  # nombre correcto
    print(f"Se cargaron {len(pokemon_list)} Pokémones existentes.")

    pokemon_list = add_pokemon(pokemon_list)

    save_pokemon_file(filename, pokemon_list)