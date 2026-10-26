from logic import Category, Movement, FinanceManager
from datetime import date
import pytest

def test_category_creation():
    category = Category("Food", "#FFA500")

    assert category.name == "Food"
    assert category.color == "#FFA500"

def test_category_invalid_name():

    with pytest.raises(ValueError):
            Category(" ", "#FFA542")

def test_category_invalid_color():

    with pytest.raises(ValueError):
            Category("Gas", "#WRONG")

def test_movement_creation():

    category = Category("Food", "#CC3421")

    transaction_test = Movement("Walmart", 35000, category, "Expense", "08/10/2026")

    assert transaction_test.title == "Walmart"
    assert transaction_test.amount == 35000
    assert (transaction_test.category.name, transaction_test.category.color) == ("Food", "#CC3421")
    assert transaction_test.movement_type == "Expense"
    assert transaction_test.date == date(2026, 10, 8)

def test_duplicate_category():

    manager = FinanceManager()
    gas =  Category("Gas", "#DD1233")
    gas2 = Category(" GAS ", "#DC1234")

    manager.add_category(gas)
     
    with pytest.raises(ValueError):
        manager.add_category(gas2)

    assert len(manager.categories) == 1
    assert manager.categories[0].name == "Gas"

def test_add_movement():

     manager_menu = FinanceManager()
     food = Category("Food", "#BB1234")

     manager_menu.add_category(food)

     movement_record = Movement(
          "Walmart",
          45000,
          food,
          "Expense",
          "08/10/2026"
     )

     manager_menu.add_movement(movement_record)

     assert len(manager_menu.movements) == 1
     assert manager_menu.movements[0] is movement_record

def test_movement_added_without_category():

    manager = FinanceManager()

    gas = Category ("GAS", "#AA1256")
    movement_record = Movement("Gas Station",
                       25000,
                       gas,
                       "Expense",
                       "08/10/2026")

    with pytest.raises(ValueError, match="No categories available"):
        manager.add_movement(movement_record)
    assert len(manager.movements) == 0

def test_financial_calculation():

    manager = FinanceManager()

    work = Category("Work", "#AA1233")
    food = Category("Food","#DE0984")

    manager.add_category(work)
    manager.add_category(food)

    movement_record = Movement(
          "Work Salary",
          950000,
          work,
          "Income",
          "08/10/2026"
     )
    movement_record2 = Movement(
         "Walmart",
        450000,
        food,
        "Expense",
        "08/10/2026")

    movement_record3 = Movement(
         "Walmart",
        100000,
        food,
        "Expense",
        "08/10/2026")

    manager.add_movement(movement_record)
    manager.add_movement(movement_record2)
    manager.add_movement(movement_record3)

    assert manager.calculate_income() == 950000
    assert manager.calculate_expense() == 550000
    assert manager.calculate_balance() == 400000