from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

session.query(Restaurant).all()
print(session.query(Restaurant).all())

items = session.query(MenuItem).all()
for item in items:
    print(item.name)
