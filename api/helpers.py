import crud

def get_menu_items_in_order(identifiers, entities):
    menu_item_ids = []
    for identifier in identifiers:
        if identifier.identifier in entities:
            menu_item_ids.append(identifier.menu_item_id)
    return menu_item_ids

def get_cost(menu_items):
    subtotal = 0.0
    for item in menu_items:
        subtotal += item.price
    taxes = subtotal * 0.0875
    taxes = round(taxes, 2)
    total = subtotal + taxes
    return subtotal, taxes, total

            
    