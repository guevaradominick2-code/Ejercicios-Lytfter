import csv
import json

from pathlib import Path

from logic import (
    Category,
    Movement
)


def category_to_dict(category):

    if not isinstance(
        category,
        Category
    ):
        raise ValueError(
            "Expected a Category object"
        )

    return {
        "category": category.name,
        "color": category.color
    }


def dict_to_category(
    category_data
):

    if not isinstance(
        category_data,
        dict
    ):
        raise ValueError(
            "Expecting to receive dictionary information"
        )

    return Category(
        category_data["category"],
        category_data["color"]
    )


def save_categories(
    categories,
    file_path
):

    file_path = Path(
        file_path
    )

    file_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    data = [
        category_to_dict(
            category
        )
        for category in categories
    ]

    with file_path.open(
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )


def load_categories(
    file_path
):

    file_path = Path(
        file_path
    )

    try:

        with file_path.open(
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(
                file
            )

    except (
        FileNotFoundError,
        json.JSONDecodeError
    ):

        return []

    if not isinstance(
        data,
        list
    ):
        return []

    categories = []

    for item in data:

        try:

            categories.append(
                dict_to_category(
                    item
                )
            )

        except (
            ValueError,
            KeyError,
            TypeError
        ):

            continue

    return categories


def movement_to_dict(
    movement
):

    if not isinstance(
        movement,
        Movement
    ):
        raise ValueError(
            "Invalid movement"
        )

    return {
        "title": movement.title,
        "amount": movement.amount,
        "category": movement.category.name,
        "movement_type": movement.movement_type,
        "date": movement.date.strftime(
            "%d/%m/%Y"
        )
    }


def dict_to_movement(
    movement_data,
    categories
):

    if not isinstance(
        movement_data,
        dict
    ):
        raise ValueError(
            "Expected a dictionary"
        )

    category_name = (
        movement_data[
            "category"
        ]
    )

    selected_category = None

    for category in categories:

        if (
            category.name.casefold()
            ==
            str(category_name)
            .strip()
            .casefold()
        ):

            selected_category = (
                category
            )

            break

    if selected_category is None:

        raise ValueError(
            "Movement category not found"
        )

    return Movement(
        movement_data["title"],
        movement_data["amount"],
        selected_category,
        movement_data[
            "movement_type"
        ],
        movement_data["date"]
    )


def save_movements(
    movements,
    file_path
):

    file_path = Path(
        file_path
    )

    file_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    data = [
        movement_to_dict(
            movement
        )
        for movement in movements
    ]

    with file_path.open(
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )


def load_movements(
    file_path,
    categories
):

    file_path = Path(
        file_path
    )

    try:

        with file_path.open(
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(
                file
            )

    except (
        FileNotFoundError,
        json.JSONDecodeError
    ):

        return []

    if not isinstance(
        data,
        list
    ):
        return []

    movements = []

    for item in data:

        try:

            movements.append(
                dict_to_movement(
                    item,
                    categories
                )
            )

        except (
            ValueError,
            KeyError,
            TypeError
        ):

            continue

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

        writer = csv.writer(
            file
        )

        writer.writerow([
            "Date",
            "Title",
            "Amount",
            "Category",
            "Type"
        ])

        for movement in movements:

            writer.writerow([
                movement.date.strftime(
                    "%d/%m/%Y"
                ),
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