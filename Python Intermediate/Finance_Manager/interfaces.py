import FreeSimpleGUI as sg

from logic import Category, Movement, validate_date

from persistence import (
    save_categories,
    save_movements,
    export_movements_to_csv
)



def main_window(manager):

    table_data, row_colors = movements_table_data(
        manager.movements
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
                f"Income: ${manager.calculate_income()}",
                key="INCOME_TOTAL"
            ),

            sg.Text(
                f"Expenses: ${manager.calculate_expense()}",
                key="EXPENSE_TOTAL"
            ),

            sg.Text(
                f"Balance: ${manager.calculate_balance()}",
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

            sg.Button("Clear Filter")
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
            sg.Button("Add Category"),
            sg.Button("Add Expense"),
            sg.Button("Add Income")
        ],

        [
            sg.Button("Export CSV"),
            sg.Button("Clear History"),
            sg.Button("Exit")
        ]
    ]

    window = sg.Window(
        "Finance Manager",
        layout
    )

    while True:

        event, values = window.read()

        if event in (
            sg.WIN_CLOSED,
            "Exit"
        ):

            save_categories(
                manager.categories,
                "data/categories.json"
            )

            save_movements(
                manager.movements,
                "data/movements.json"
            )

            break


        if event == "Add Category":

            add_category_window(manager)


        if event == "Add Expense":

            add_expense_window(manager)

            refresh_main_window(
                window,
                manager
            )

        if event == "Add Income":

            add_income_window(manager)

            refresh_main_window(
                window,
                manager
            )

        if event == "Filter":

            try:

                filtered_movements = filter_movements(
                    manager,
                    values["FILTER_FROM"],
                    values["FILTER_TO"]
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

            window["FILTER_FROM"].update("")
            window["FILTER_TO"].update("")

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


def movements_table_data(movements):

    table_data = []
    row_colors = []

    for index, movement in enumerate(movements):

        table_data.append([
            movement.date.strftime("%d/%m/%Y"),
            movement.title,
            movement.amount,
            movement.category.name,
            movement.movement_type
        ])

        text_color = text_color_for_background(
            movement.category.color
        )

        row_colors.append(
            (
                index,
                text_color,
                movement.category.color
            )
        )

    return table_data, row_colors


def text_color_for_background(color):

    color = color.replace("#", "")

    red = int(color[0:2], 16)
    green = int(color[2:4], 16)
    blue = int(color[4:6], 16)

    brightness = (
        red * 299 +
        green * 587 +
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
        movements = manager.movements

    table_data, row_colors = movements_table_data(
        movements
    )

    window["__MOVEMENTS__"].update(
        values=table_data,
        row_colors=row_colors
    )

    income = 0
    expenses = 0

    for movement in movements:

        if movement.movement_type == "Income":
            income += movement.amount

        elif movement.movement_type == "Expense":
            expenses += movement.amount

    balance = income - expenses

    window["INCOME_TOTAL"].update(
        f"Income: ${income}"
    )

    window["EXPENSE_TOTAL"].update(
        f"Expenses: ${expenses}"
    )

    window["BALANCE_TOTAL"].update(
        f"Balance: ${balance}"
    )

def add_category_window(manager):

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

        event, values = window.read()

        if event in (
            sg.WIN_CLOSED,
            "Cancel"
        ):
            break

        if event == "Save":

            name = (
                values["CATEGORY_NAME"]
                .strip()
            )

            color = (
                values["CATEGORY_COLOR"]
                .strip()
            )

            try:

                category = Category(
                    name,
                    color
                )

                manager.add_category(
                    category
                )

                save_categories(
                    manager.categories,
                    "data/categories.json"
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


def add_expense_window(manager):

    if not manager.categories:

        sg.popup_error(
            "No categories available"
        )

        return

    category_names = []

    for category in manager.categories:

        category_names.append(
            category.name
        )

    layout = [

        [
            sg.Text("Title")
        ],

        [
            sg.Input(
                key="EXPENSE_TITLE"
            )
        ],

        [
            sg.Text("Amount")
        ],

        [
            sg.Input(
                key="EXPENSE_AMOUNT"
            )
        ],

        [
            sg.Text("Category")
        ],

        [
            sg.Combo(
                category_names,
                key="EXPENSE_CATEGORY",
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
                key="EXPENSE_DATE"
            )
        ],

        [
            sg.Button("Save"),
            sg.Button("Cancel")
        ]
    ]

    window = sg.Window(
        "Add Expense",
        layout
    )

    while True:

        event, values = window.read()

        if event in (
            sg.WIN_CLOSED,
            "Cancel"
        ):
            break

        if event == "Save":

            title = (
                values["EXPENSE_TITLE"]
                .strip()
            )

            amount = (
                values["EXPENSE_AMOUNT"]
                .strip()
            )

            category_name = (
                values["EXPENSE_CATEGORY"]
            )

            expense_date = (
                values["EXPENSE_DATE"]
                .strip()
            )

            try:

                amount = float(amount)

                selected_category = None

                for category in manager.categories:

                    if (
                        category.name
                        == category_name
                    ):

                        selected_category = (
                            category
                        )

                        break

                if selected_category is None:

                    raise ValueError(
                        "Please select a category"
                    )

                movement = Movement(
                    title,
                    amount,
                    selected_category,
                    "Expense",
                    expense_date
                )

                manager.add_movement(
                    movement
                )

                save_movements(
                    manager.movements,
                    "data/movements.json"
                )

                sg.popup(
                    "Expense added successfully"
                )

                break

            except ValueError as error:

                sg.popup_error(
                    str(error)
                )

    window.close()


def add_income_window(manager):

    if not manager.categories:

        sg.popup_error(
            "No categories available"
        )

        return

    category_names = []

    for category in manager.categories:

        category_names.append(
            category.name
        )

    layout = [

        [
            sg.Text("Title")
        ],

        [
            sg.Input(
                key="INCOME_TITLE"
            )
        ],

        [
            sg.Text("Amount")
        ],

        [
            sg.Input(
                key="INCOME_AMOUNT"
            )
        ],

        [
            sg.Text("Category")
        ],

        [
            sg.Combo(
                category_names,
                key="INCOME_CATEGORY",
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
                key="INCOME_DATE"
            )
        ],

        [
            sg.Button("Save"),
            sg.Button("Cancel")
        ]
    ]

    window = sg.Window(
        "Add Income",
        layout
    )

    while True:

        event, values = window.read()

        if event in (
            sg.WIN_CLOSED,
            "Cancel"
        ):
            break

        if event == "Save":

            title = (
                values["INCOME_TITLE"]
                .strip()
            )

            amount = (
                values["INCOME_AMOUNT"]
                .strip()
            )

            category_name = (
                values["INCOME_CATEGORY"]
            )

            income_date = (
                values["INCOME_DATE"]
                .strip()
            )

            try:

                amount = float(amount)

                selected_category = None

                for category in manager.categories:

                    if (
                        category.name
                        == category_name
                    ):

                        selected_category = (
                            category
                        )

                        break

                if selected_category is None:

                    raise ValueError(
                        "Please select a category"
                    )

                movement = Movement(
                    title,
                    amount,
                    selected_category,
                    "Income",
                    income_date
                )

                manager.add_movement(
                    movement
                )

                save_movements(
                    manager.movements,
                    "data/movements.json"
                )

                sg.popup(
                    "Income added successfully"
                )

                break

            except ValueError as error:

                sg.popup_error(
                    str(error)
                )

    window.close()

def filter_movements(
    manager,
    start_date_text,
    end_date_text
):

    start_date_text = (
        start_date_text.strip()
    )

    end_date_text = (
        end_date_text.strip()
    )

    if not start_date_text:
        raise ValueError(
            "Please enter the start date"
        )

    if not end_date_text:
        raise ValueError(
            "Please enter the end date"
        )

    start_date = validate_date(
        start_date_text
    )

    end_date = validate_date(
        end_date_text
    )

    if start_date > end_date:

        raise ValueError(
            "Start date cannot be after end date"
        )

    filtered_movements = []

    for movement in manager.movements:

        if (
            start_date
            <= movement.date
            <= end_date
        ):

            filtered_movements.append(
                movement
            )

    return filtered_movements

def export_csv_window(manager):

    if not manager.movements:

        sg.popup_error(
            "There are no movements to export"
        )

        return

    file_path = sg.popup_get_file(
        "Save CSV",
        save_as=True,
        default_extension=".csv",
        file_types=(
            ("CSV Files", "*.csv"),
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

    except Exception as error:

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

    confirmation = sg.popup_yes_no(
        "Are you sure you want to delete "
        "all movement history?\n\n"
        "This will delete all incomes and "
        "expenses.\n"
        "Categories will NOT be deleted."
    )

    if confirmation != "Yes":
        return

    manager.movements.clear()

    save_movements(
        manager.movements,
        "data/movements.json"
    )

    refresh_main_window(
        window,
        manager
    )

    sg.popup(
        "Movement history deleted successfully"
    )