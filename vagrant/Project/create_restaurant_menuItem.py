from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

myFirstRestaurant = Restaurant(name = "Pizza Palace")
session.add(myFirstRestaurant)
session.commit()
session.query(Restaurant).all()

print(session.query(Restaurant).all())

chessepizza = MenuItem(name = "Chesse Pizza",
    description = "Made with all natural ingredients and freesh mozzarella",
    course = "Entree", price = "$8.99", restaurant = myFirstRestaurant)
session.add(chessepizza)
session.commit()
session.query(MenuItem).all()
print(session.query(MenuItem).all())

firstResult = session.query(Restaurant).first()
firstResult.name
print(firstResult)
