import json

def read_json(database_path: str) -> dict:
    try:
        with open(database_path, "r", encoding="utf8") as database_file:
            database = json.load(database_file)    
            return database
        
    except FileNotFoundError:
        return []
    
    except:
        return []
    
def write_json(database_path: str, content: dict):
    database = read_json(database_path)    
    
    product_already_exists = [
        product["name"]
        for product in database
        if product["name"] == content["name"]  
    ]
    
    if product_already_exists:
        return "Produto já inserido, insira um novo produto"
    
    database.append({"id": next_id(database_path), **content})
    with open(database_path, "w", encoding="utf8") as database_file:
        json.dump(database, database_file, ensure_ascii=True)
    
def next_id(database_path: str) -> dict:
    database = read_json(database_path)
    return len(database) + 1