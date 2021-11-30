import crud

def get_menu_items_in_order(identifiers, entities):
    menu_item_ids = []
    for identifier in identifiers:
        if identifier.identifier in entities:
            menu_item_ids.append(identifier.menu_item_id)
    return menu_item_ids
            
    