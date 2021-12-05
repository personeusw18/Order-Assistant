from typing import List
from sqlalchemy.orm import Session

import models

def get_restaurant(db: Session, id: int):
    return db.query(models.Restaurant).filter(models.Restaurant.id == id).first()

def get_restaurants(db: Session):
    return db.query(models.Restaurant).all()

def get_identifiers(db: Session, restaurant_id: int):
    return db.query(models.Identifier).filter(models.Identifier.restaurant_id == restaurant_id).all()

def get_menu_items(db: Session, menu_item_ids: List[int]):
    return db.query(models.MenuItem).filter(models.MenuItem.id.in_(menu_item_ids)).all()

def reset_db(db: Session):

    # clear db (everything cascade deletes on restaurants)
    restaurants = get_restaurants(db)
    for restaurant in restaurants:
        db.delete(restaurant)
    db.commit()

    dunkin = models.Restaurant(
        id = 1,
        name="Dunkin Donuts",
        img=r"https://upload.wikimedia.org/wikipedia/en/thumb/b/b8/Dunkin%27_Donuts_logo.svg/1200px-Dunkin%27_Donuts_logo.svg.png",
        menu_items=[
            models.MenuItem(
                name="Coffee",
                desc="Our famous Hot Coffee is made from high-quality 100% Arabica beans and is freshly ground and brewed continually throughout the day.",
                price=1.99,
                img=r"https://www.dunkindonuts.com/content/dam/dd/img/menu-redesign/espresso-coffee/pdpespressocoffee/Coffee_570x570.png",
                identifiers=[
                    models.Identifier(
                        restaurant_id=1,
                        identifier="coffee"
                    ),
                    models.Identifier(
                        restaurant_id=1,
                        identifier="cup of joe"
                    )
                ]
            ),
            models.MenuItem(
                name="Americano",
                desc="Our Hot Americano puts the oh! in Americano by combining two shots of Dunkin’s 100% Rainforest Alliance Certified™ espresso with hot water creating a rich, robust drink.",
                price=3.99,
                img=r"https://www.dunkindonuts.com/content/dam/dd/img/menu-redesign/espresso-coffee/pdpespressocoffee/Americano_570x570.png",
                identifiers=[
                    models.Identifier(
                        restaurant_id=1,
                        identifier="americano"
                    ),
                ]
            ),
            models.MenuItem(
                name="Latte",
                desc="Made with steamed, frothy milk, blended with our rich, freshly ground and brewed espresso. Our Latte has a layer of foam and is the perfect balance of creamy and smooth to get you goin'.",
                img=r"https://www.dunkindonuts.com/content/dam/dd/img/menu-redesign/espresso-coffee/pdpespressocoffee/Latte_570x570.png",
                price=3.99,
                identifiers=[
                    models.Identifier(
                        restaurant_id=1,
                        identifier="latte"
                    ),
                ]
            )
        ]
    )
    mcdonalds = models.Restaurant(
        id=2,
        name="McDonalds",
        img=r"https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/McDonald%27s_Golden_Arches.svg/2339px-McDonald%27s_Golden_Arches.svg.png",
        menu_items=[
            models.MenuItem(
                name="Big Mac",
                desc=r"Mouthwatering perfection starts with two 100% pure beef patties and Big Mac® sauce sandwiched between a sesame seed bun. It’s topped off with pickles, crisp shredded lettuce, finely chopped onion and American cheese for a 100% beef burger with a taste like no other.",
                price=7.89,
                img=r"https://www.mcdonalds.com/is/image/content/dam/usa/nfl/nutrition/items/hero/desktop/t-mcdonalds-Big-Mac.jpg?$Product_Desktop$",
                identifiers=[
                    models.Identifier(
                        restaurant_id=2,
                        identifier="big mac"
                    ),
                    models.Identifier(
                        restaurant_id=2,
                        identifier="number one"
                    )
                ]
            ),
            models.MenuItem(
                name="Quarter Pounder",
                desc=r"Each Quarter Pounder® with Cheese burger features a ¼ lb.* of 100% fresh beef that’s hot, deliciously juicy and cooked when you order. It’s seasoned with just a pinch of salt and pepper, sizzled on a flat iron grill, then topped with slivered onions, tangy pickles and two slices of melty American cheese on a sesame seed bun.",
                price=6.29,
                img=r"https://www.mcdonalds.com/is/image/content/dam/usa/nfl/nutrition/items/hero/desktop/t-mcdonalds-Quarter-Pounder-with-Cheese.jpg?$Product_Desktop$",
                identifiers=[
                    models.Identifier(
                        restaurant_id=2,
                        identifier="quarter pounder"
                    ),
                    models.Identifier(
                        restaurant_id=2,
                        identifier="qp"
                    ),
                    models.Identifier(
                        restaurant_id=2,
                        identifier="number two"
                    )
                ]
            ),
        ],
    )
    db.add(dunkin)
    db.add(mcdonalds)
    db.commit()