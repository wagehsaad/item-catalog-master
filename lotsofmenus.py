from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Categories, Base, Courses

engine = create_engine('postgresql://catalog:grader@localhost/catalog')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Menu for UrbanBurger
category1 = Categories(name="Urban Burger")

session.add(category1)
session.commit()

Courses2 = Courses(
    name="Veggie Burger", description="Juicy grilluce",
    link="$7.50", photo_url="Entree", category=category1)
session.add(Courses2)
session.commit()


Courses1 = Courses(
        name="French Fries", description="with garrmesan",
        link="$2.99", photo_url="Appetizer", category=category1)

session.add(Courses1)
session.commit()

Courses2 = Courses(
        name="Chicken Burger", description="Juicy glettuce",
        link="$5.50", photo_url="Entree", category=category1)

session.add(Courses2)
session.commit()

Courses3 = Courses(
    name="Chocolate Cake", description="fresam",
    link="$3.99", photo_url="Dessert", category=category1)

session.add(Courses3)
session.commit()

Courses4 = Courses(
    name="Sirloin Burger", description="Mad ade A beef",
    link="$7.99", photo_url="Entree", category=category1)

session.add(Courses4)
session.commit()

Courses5 = Courses(
    name="Root Beer", description="16oz of goodness",
    link="$1.99", photo_url="Beverage", category=category1)

session.add(Courses5)
session.commit()

Courses6 = Courses(
    name="Iced Tea", description="with Lemon",
    link="$.99", photo_url="Beverage", category=category1)

session.add(Courses6)
session.commit()

Courses7 = Courses(
    name="Grilled Cheese Sandwich", description="On ",
    link="$3.49", photo_url="Entree", category=category1)

session.add(Courses7)
session.commit()

Courses8 = Courses(
    name="Veggie Burger", description="Ms grown spices",
    link="$5.99", photo_url="Entree", category=category1)

session.add(Courses8)
session.commit()


# Menu for Super Stir Fry
category2 = Categories(name="Super Stir Fry")

session.add(category2)
session.commit()


Courses1 = Courses(
    name="Chicken Stir Fry", description="Witauces",
    link="$7.99", photo_url="Entree", category=category2)

session.add(Courses1)
session.commit()

Courses2 = Courses(
    name="Peking Duck", description=" s prcook",
    link="$25", photo_url="Entree", category=category2)

session.add(Courses2)
session.commit()

Courses3 = Courses(
    name="Spicy Tuna Roll", description="Seoy sauce ",
    link="15", photo_url="Entree", category=category2)

session.add(Courses3)
session.commit()

Courses4 = Courses(
    name="Nepali Momo ", description="Steamedmeat. ",
    link="12", photo_url="Entree", category=category2)

session.add(Courses4)
session.commit()

Courses5 = Courses(
    name="Beef Noodle Soup", description="A Chioodles.",
    link="14", photo_url="Entree", category=category2)

session.add(Courses5)
session.commit()

Courses6 = Courses(
    name="Ramen", description="a Japa uses.",
    link="12", photo_url="Entree", category=category2)

session.add(Courses6)
session.commit()


# Menu for Panda Garden
category1 = Categories(name="Panda Garden")

session.add(category1)
session.commit()


Courses1 = Courses(
    name="Pho", description="a Vie] meat.",
    link="$8.99", photo_url="Entree", category=category1)

session.add(Courses1)
session.commit()

Courses2 = Courses(
    name="Chinese Dumplings", description="a ccker.",
    link="$6.99", photo_url="Appetizer", category=category1)

session.add(Courses2)
session.commit()

Courses3 = Courses(
    name="Gyoza", description="The most prominner",
    link="$9.95", photo_url="Entree", category=category1)

session.add(Courses3)
session.commit()

Courses4 = Courses(
    name="Stinky Tofu", description="Taiwanesd cabbage.",
    link="$6.99", photo_url="Entree", category=category1)

session.add(Courses4)
session.commit()

Courses2 = Courses(
    name="Veggie Burger", description="Juicy glettuce",
    link="$9.50", photo_url="Entree", category=category1)

session.add(Courses2)
session.commit()

print "added menu items!"
