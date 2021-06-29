from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import sys
import os
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurant'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)


class MenuItem(Base):
    __tablename__ = 'menu_item'
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    course = Column(String(255))
    description = Column(String(255))
    price = Column(String(255))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)


engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)



Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession() 



#add
MyFirstRestaurant = Restaurant(name = "Pizza Place")
session.add(MyFirstRestaurant)
session.commit()
session.query(Restaurant).all()
session.commit()
cheesepizza = MenuItem(name = "Cheese Pizza", description = "Pizza with cheese", course = "Entree", price = "$9.99", restaurant = MyFirstRestaurant)
session.add(cheesepizza)
session.commit()
veggieBurger = MenuItem(name = "Veggie Burger", description = "Veggie Burger", course = "Starter", price = "$19.99", restaurant = MyFirstRestaurant)
veggieBurger1 = MenuItem(name = "Veggie Burger1", description = "Veggie Burger", course = "Starter", price = "$119.99", restaurant = MyFirstRestaurant)
session.add(veggieBurger)
session.add(veggieBurger1)
session.commit()

#read
items = session.query(MenuItem).all()
for item in items:
    print(item.name)

#update
veggieBurgers = session.query(MenuItem).filter_by(name = 'Veggie Burger')
for burger in veggieBurgers:
    print(burger.name)
    burger.price = "$2.99"
    session.add(burger)
    session.commit()
session.commit()
pizza = session.query(MenuItem).filter_by(name = "Cheese Pizza", id = 1).one()
pizza.price = "$1"
session.add(pizza)
session.commit()

#delete
veggieBurgers = session.query(MenuItem).filter_by(name = 'Veggie Burger1')

for burger in veggieBurgers:
    print(burger.name)
    session.delete(burger)
session.commit()
