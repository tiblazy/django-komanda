from utils.json_handler import read_json, write_json

DATABASE_PATH = "menu.json"


if __name__ == "__main__":
    content = {
        "name": "BATATA FRITA", 
        "price": 35.3
    }
    
    print(write_json(DATABASE_PATH, content))
    print(read_json(DATABASE_PATH))
