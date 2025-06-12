import re

def extract_sessionid(session_str:str):
    #Extract using regex
    match =re.search(r'/sessions/(.*?)/contexts',session_str)
    if match:
        return match.group(0)
    return ""

def get_str_from_food_dict(food_dict: dict):
    result = ", ".join([f"{int(value)} {key}" for key, value in food_dict.items()])
    return result


def save_to_db(order:dict):
    import backend.db_helper as db_helper
    order_id=db_helper.get_next_order_id()
    for food_item,quantity in order.items():
        db_helper.insert_order_item(food_item,quantity,order_id)
    db_helper.insert_order_tracking(order_id,"in-progress")
    
    return order_id
