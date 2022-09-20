from utils.json_handler import read_json, write_json
from management.tab_handler import calculate_tab

DATABASE_PATH = "menu.json"

if __name__ == "__main__":
    content = {"name": "CHURROS DO M5", "price": 5.0}
    
    print(write_json(DATABASE_PATH, content))
    print(read_json(DATABASE_PATH))

if __name__ == "__main__":
    table_1 = [{'id': 1, 'amount': 5}, {'id': 19, 'amount': 5}]
    table_2 = [
      {"id": 10, "amount": 3},
      {"id": 20, "amount": 2},
      {"id": 21, "amount": 5},
    ]

    print(calculate_tab(table_1))
    print(calculate_tab(table_2))