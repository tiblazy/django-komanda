import re
from utils.json_handler import read_json
from datetime import datetime

DATABASE_PATH = "menu.json"

def calculate_tab(table: dict):    
    database = read_json(DATABASE_PATH)

    subtotal = 0
    for product in table:
        for item in database:
            if product["id"] == item["id"]:
                subtotal += item["price"] * product["amount"]
                
    local_format = "%d/%m/%y %H:%M:%S"
    date_now = datetime.now()
    created_at = date_now.strftime(local_format)        
        
    return {"subtotal": subtotal, "created_at": created_at}