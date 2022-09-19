import json

def read_json(database_path: str) -> dict:    
    with open(database_path, "r", encoding="utf8") as database_file:
        database = json.load(database_file)    
        
        if not database or len(database) == 0:
            return []
        
        return database
    
def write_json(database_path: str, content: dict):
    database = read_json(database_path)
    database["content"].append({"id": next_id(database_path), **content})
    
    with open(database_path, "w", encoding="utf8") as database_file:
        json.dump(database, database_file, ensure_ascii=True)
    
def next_id(database_path: str) -> dict:
    database = read_json(database_path)
    return len(database["content"]) + 1