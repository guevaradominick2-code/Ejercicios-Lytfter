from pathlib import Path


BASE_DIR = (
    Path(__file__)
    .resolve()
    .parent
)

DATA_DIR = (
    BASE_DIR
    / "data"
)

CATEGORIES_FILE = (
    DATA_DIR
    / "categories.json"
)

MOVEMENTS_FILE = (
    DATA_DIR
    / "movements.json"
)