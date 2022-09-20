from datetime import datetime

def calculate_tab(table: dict):    
    total = {}
    for item in table:
        for amount in item.keys():
            total[amount] = total.get(amount, 0) + item[amount]
    subtotal = total["amount"]
    
    local_format = "%d/%m/%y %H:%M:%S"
    date_now = datetime.now()
    created_at = date_now.strftime(local_format)        
        
    return {"subtotal": subtotal, "created_at": created_at}