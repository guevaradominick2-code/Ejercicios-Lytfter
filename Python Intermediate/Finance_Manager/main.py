from logic import FinanceManager
from persistence import load_categories, load_movements
from interfaces import main_window

manager = FinanceManager()

manager.categories = load_categories("data/categories.json")
manager.movements = load_movements(
    "data/movements.json",
    manager.categories
)

main_window(manager)