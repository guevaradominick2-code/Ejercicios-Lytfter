from datetime import date

import FreeSimpleGUI as sg

from paths import (
    CATEGORIES_FILE,
    MOVEMENTS_FILE
)

from persistence import (
    save_categories,
    save_movements,
    export_movements_to_csv
)

def main_window(manager):

    table_data, row_colors = (
        movements_table_data(
            manager.movements
        )
    )

    headings = [
        "Date",
        "Title",
        "Amount",
        "Category",
        "Type"
    ]

    layout = [

        [
            sg.Text(
                "Lyfter Finance Manager",
                font=("Arial", 18)
            )
        ],

        [
            sg.Text(
                f"Income: ₡{manager.calculate_income():,.2f}",
                key="INCOME_TOTAL"
            ),

            sg.Text(
                f"Expenses: ₡{manager.calculate_expense():,.2f}",
                key="EXPENSE_TOTAL"
            ),

            sg.Text(
                f"Balance: ₡{manager.calculate_balance():,.2f}",
                key="BALANCE_TOTAL"
            )
        ],

        [
            sg.Text("From:"),

            sg.Input(
                key="FILTER_FROM",
                size=(12, 1)
            ),

            sg.Text("To:"),

            sg.Input(
                key="FILTER_TO",
                size=(12, 1)
            ),

            sg.Button("Filter"),

            sg.Button(
                "Clear Filter"
            )
        ],

        [
            sg.Table(
                values=table_data,
                headings=headings,
                key="__MOVEMENTS__",
                auto_size_columns=True,
                justification="center",
                num_rows=10,
                row_colors=row_colors
            )
        ],

        [
            sg.Button(
                "Add Category"
            ),

            sg.Button(
                "Add Expense"
            ),

            sg.Button(
                "Add Income"
            )
        ],

        [
            sg.Button(
                "Export CSV"
            ),

            sg.Button(
                "Clear History"
            ),

            sg.Button(
                "Exit"
            )
        ]
    ]

    window = sg.Window(
        "Finance Manager",
        layout
    )

    while True:

        event, values = (
            window.read()
        )

        if event in (
            sg.WIN_CLOSED,
            "Exit"
        ):

            save_categories(
                manager.categories,
                CATEGORIES_FILE
            )

            save_movements(
                manager.movements,
                MOVEMENTS_FILE
            )

            break

        if event == "Add Category":

            add_category_window(
                manager
            )

        if event == "Add Expense":

            add_movement_window(
                manager,
                "Expense"
            )

            refresh_main_window(
                window,
                manager
            )

        if event == "Add Income":

            add_movement_window(
                manager,
                "Income"
            )

            refresh_main_window(
                window,
                manager
            )

        if event == "Filter":

            try:

                filtered_movements = (
                    manager.filter_movements(
                        values[
                            "FILTER_FROM"
                        ],
                        values[
                            "FILTER_TO"
                        ]
                    )
                )

                refresh_main_window(
                    window,
                    manager,
                    filtered_movements
                )

            except ValueError as error:

                sg.popup_error(
                    str(error)
                )

        if event == "Clear Filter":

            window[
                "FILTER_FROM"
            ].update("")

            window[
                "FILTER_TO"
            ].update("")

            refresh_main_window(
                window,
                manager
            )

        if event == "Export CSV":

            export_csv_window(
                manager
            )

        if event == "Clear History":

            clear_history(
                manager,
                window
            )

    window.close()


def movements_table_data(
    movements
):

    table_data = []
    row_colors = []

    for index, movement in enumerate(
        movements
    ):

        table_data.append([
            movement.date.strftime(
                "%d/%m/%Y"
            ),

            movement.title,

            f"₡{movement.amount:,.2f}",

            movement.category.name,

            movement.movement_type
        ])

        row_colors.append((
            index,

            text_color_for_background(
                movement.category.color
            ),

            movement.category.color
        ))

    return (
        table_data,
        row_colors
    )


def text_color_for_background(
    color
):

    color = color.replace(
        "#",
        ""
    )

    red = int(
        color[0:2],
        16
    )

    green = int(
        color[2:4],
        16
    )

    blue = int(
        color[4:6],
        16
    )

    brightness = (
        red * 299
        +
        green * 587
        +
        blue * 114
    ) / 1000

    if brightness > 150:
        return "black"

    return "white"


def refresh_main_window(
    window,
    manager,
    movements=None
):

    if movements is None:
        movements = (
            manager.movements
        )

    table_data, row_colors = (
        movements_table_data(
            movements
        )
    )

    window[
        "__MOVEMENTS__"
    ].update(
        values=table_data,
        row_colors=row_colors
    )

    window[
        "INCOME_TOTAL"
    ].update(
        f"Income: ₡{manager.calculate_income(movements):,.2f}"
    )

    window[
        "EXPENSE_TOTAL"
    ].update(
        f"Expenses: ₡{manager.calculate_expense(movements):,.2f}"
    )

    window[
        "BALANCE_TOTAL"
    ].update(
        f"Balance: ₡{manager.calculate_balance(movements):,.2f}"
    )


def add_category_window(
    manager
):

    layout = [

        [
            sg.Text(
                "Category Name"
            )
        ],

        [
            sg.Input(
                key="CATEGORY_NAME"
            )
        ],

        [
            sg.Text(
                "Color"
            )
        ],

        [
            sg.Input(
                key="CATEGORY_COLOR",
                size=(12, 1)
            ),

            sg.ColorChooserButton(
                "Choose Color",
                target="CATEGORY_COLOR"
            )
        ],

        [
            sg.Button("Save"),
            sg.Button("Cancel")
        ]
    ]

    window = sg.Window(
        "Add Category",
        layout
    )

    while True:

        event, values = (
            window.read()
        )

        if event in (
            sg.WIN_CLOSED,
            "Cancel"
        ):
            break

        if event == "Save":

            try:

                manager.create_category(
                    values[
                        "CATEGORY_NAME"
                    ],
                    values[
                        "CATEGORY_COLOR"
                    ]
                )

                save_categories(
                    manager.categories,
                    CATEGORIES_FILE
                )

                sg.popup(
                    "Category added successfully"
                )

                break

            except ValueError as error:

                sg.popup_error(
                    str(error)
                )

    window.close()


def add_movement_window(
    manager,
    movement_type
):

    if not manager.categories:

        sg.popup_error(
            "No categories available"
        )

        return

    if movement_type not in (
        "Income",
        "Expense"
    ):

        sg.popup_error(
            "Invalid movement type"
        )

        return

    category_names = [
        category.name
        for category
        in manager.categories
    ]

    today = (
        date.today()
        .strftime("%d/%m/%Y")
    )

    layout = [

        [
            sg.Text("Title")
        ],

        [
            sg.Input(
                key="MOVEMENT_TITLE"
            )
        ],

        [
            sg.Text("Amount")
        ],

        [
            sg.Input(
                key="MOVEMENT_AMOUNT"
            )
        ],

        [
            sg.Text("Category")
        ],

        [
            sg.Combo(
                category_names,
                key="MOVEMENT_CATEGORY",
                readonly=True
            )
        ],

        [
            sg.Text(
                "Date (dd/mm/yyyy)"
            )
        ],

        [
            sg.Input(
                default_text=today,
                key="MOVEMENT_DATE"
            )
        ],

        [
            sg.Button("Save"),
            sg.Button("Cancel")
        ]
    ]

    window = sg.Window(
        f"Add {movement_type}",
        layout
    )

    while True:

        event, values = (
            window.read()
        )

        if event in (
            sg.WIN_CLOSED,
            "Cancel"
        ):
            break

        if event == "Save":

            try:

                manager.create_movement(
                    values[
                        "MOVEMENT_TITLE"
                    ],

                    values[
                        "MOVEMENT_AMOUNT"
                    ],

                    values[
                        "MOVEMENT_CATEGORY"
                    ],

                    movement_type,

                    values[
                        "MOVEMENT_DATE"
                    ]
                )

                save_movements(
                    manager.movements,
                    MOVEMENTS_FILE
                )

                sg.popup(
                    f"{movement_type} added successfully"
                )

                break

            except ValueError as error:

                sg.popup_error(
                    str(error)
                )

    window.close()


def export_csv_window(
    manager
):

    if not manager.movements:

        sg.popup_error(
            "There are no movements to export"
        )

        return

    file_path = (
        sg.popup_get_file(
            "Save CSV",
            save_as=True,
            default_extension=".csv",
            file_types=(
                (
                    "CSV Files",
                    "*.csv"
                ),
            )
        )
    )

    if not file_path:
        return

    try:

        export_movements_to_csv(

            manager.movements,

            file_path,

            manager.calculate_income(),

            manager.calculate_expense(),

            manager.calculate_balance()
        )

        sg.popup(
            "CSV exported successfully"
        )

    except OSError as error:

        sg.popup_error(
            f"Could not export CSV:\n{error}"
        )


def clear_history(
    manager,
    window
):

    if not manager.movements:

        sg.popup(
            "There is no history to delete"
        )

        return

    confirmation = (
        sg.popup_yes_no(
            "Are you sure you want to delete all movement history?\n\n"
            "This will delete all incomes and expenses.\n"
            "Categories will NOT be deleted."
        )
    )

    if confirmation != "Yes":
        return

    manager.clear_history()

    save_movements(
        manager.movements,
        MOVEMENTS_FILE
    )

    refresh_main_window(
        window,
        manager
    )

    sg.popup(
        "Movement history deleted successfully"
    )