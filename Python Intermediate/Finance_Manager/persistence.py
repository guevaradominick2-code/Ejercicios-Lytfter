from logic import Category, Movement
import json
import csv

def category_to_dict(category):
    if not isinstance(category, Category):
        raise ValueError ("Expected a Category object")

    category_dict = {
        "category": category.name,
        "color": category.color
    }
    return category_dict


def dict_to_category(category_data):
    if not isinstance(category_data, dict):
        raise ValueError ("Expecting to receive dictionary information")

    category = category_data["category"]
    color = category_data["color"]

    category_new= Category(category, color)

    return category_new


def save_categories(categories, file_path):

    categories_history = []

    for data in categories:
            categories_history.append(category_to_dict(data))

    with open(file_path, "w", encoding= "UTF-8") as file:
        json.dump(categories_history, file, indent= 4)

def load_categories(file_path):

    categories = []

    try:
        with open(file_path, "r", encoding="UTF-8") as file:
            data = json.load(file)

            for dicts in data:
                categories.append(dict_to_category(dicts))

    except FileNotFoundError:
        pass
        
    
    return categories

def movement_to_dict(movement):
    if not isinstance(movement, Movement):
        raise ValueError ("Invalid movement")

    movement_dict ={
        "title" : movement.title,
        "amount" : movement.amount,
        "category" : movement.category.name,
        "movement_type" : movement.movement_type,
        "date" : movement.date.strftime("%d/%m/%Y")
        }

    return movement_dict

def dict_to_movement(movement_dict, categories):

    if not isinstance(movement_dict, dict):
        raise ValueError("Expected a dictionary")

    title = movement_dict["title"]
    amount = movement_dict["amount"]
    category = movement_dict["category"]
    movement_type = movement_dict["movement_type"]
    date = movement_dict["date"]

    for category_object in categories:
        if category_object.name == category:

            movements_history = Movement(
                title,
                amount,
                category_object,
                movement_type,
                date
            )

            return movements_history

    raise ValueError("Movement category not found")

def save_movements(movements, file_path):

    movements_history = []

    for movement in movements:
        movements_history.append(movement_to_dict(movement))

    with open(file_path, "w", encoding= "UTF-8") as file:
            json.dump(movements_history, file, indent= 4)

def load_movements(file_path, categories):

    movements = []

    try:
        with open(file_path, "r", encoding="UTF-8") as file:
            data = json.load(file)

            for dicts in data:
                movements.append(dict_to_movement(dicts,categories))

    except FileNotFoundError:
        pass
        
    
    return movements

def export_movements_to_csv(
    movements,
    file_path,
    total_income,
    total_expense,
    balance
):

    with open(
        file_path,
        "w",
        newline="",
        encoding="utf-8-sig"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "Date",
            "Title",
            "Amount",
            "Category",
            "Type"
        ])

        for movement in movements:
            writer.writerow([
                movement.date.strftime("%d/%m/%Y"),
                movement.title,
                movement.amount,
                movement.category.name,
                movement.movement_type
            ])

        writer.writerow([])

        writer.writerow([
            "Total Income",
            total_income
        ])

        writer.writerow([
            "Total Expenses",
            total_expense
        ])

        writer.writerow([
            "Balance",
            balance
        ])