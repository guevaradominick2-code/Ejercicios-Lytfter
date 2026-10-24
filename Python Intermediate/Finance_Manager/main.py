from interfaces import main_window

from logic import FinanceManager

from paths import (
    CATEGORIES_FILE,
    MOVEMENTS_FILE
)

from persistence import (
    load_categories,
    load_movements
)


def main():

    manager = FinanceManager()

    manager.categories = (
        load_categories(
            CATEGORIES_FILE
        )
    )

    manager.movements = (
        load_movements(
            MOVEMENTS_FILE,
            manager.categories
        )
    )

    main_window(
        manager
    )


if __name__ == "__main__":
    main()