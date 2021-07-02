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


class RestaurantsDatabase():
    _engine = ""
    _session = ""

    def __init__(self):
        self._engine = create_engine('sqlite:///restaurantmenu.db')
        Base.metadata.create_all(self._engine)
        Base.metadata.bind = self._engine
        DBSession = sessionmaker(bind=self._engine)
        self._session = DBSession()

    def list_restaurants(self):
        return self._session.query(Restaurant).all()

    def add_restaurant(self, new_restaurant):
        MyFirstRestaurant = Restaurant(name=new_restaurant)
        self._session.add(MyFirstRestaurant)
        self._session.commit()
        return

    def get_restaurant_by_id(self, restaurantIDPath):
        print(restaurantIDPath)
        restaurant = self._session.query(
            Restaurant).filter_by(id=restaurantIDPath).one()
        print(restaurant.name)
        return restaurant

    def update_by_id(self, restaurantID, restaurant_name_new):
        print(restaurantID, restaurant_name_new)
        print("calling update of {} with {}".format(
            restaurantID, restaurant_name_new))
        restaurant = self.get_restaurant_by_id(restaurantID)
        print("updating of {} with {}".format(
            restaurantID, restaurant_name_new))
        restaurant.name = str(restaurant_name_new)
        self._session.add(restaurant)
        self._session.commit()
        print("updated of {} with {}".format(
            restaurantID, restaurant_name_new))
        return

    def delete_by_id(self, restaurantID):
        print("calling remove of {} with {}".format(restaurantID))
        restaurant = self.get_restaurant_by_id(restaurantID)
        self._session.delete(restaurant)
        self._session.commit()
        return


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


# engine = create_engine('sqlite:///restaurantmenu.db')
# Base.metadata.create_all(engine)


# Base.metadata.bind = engine
# DBSession = sessionmaker(bind=engine)
# session = DBSession()


# #add
# MyFirstRestaurant = Restaurant(name = "Pizza Place")
# session.add(MyFirstRestaurant)
# session.commit()
# session.query(Restaurant).all()
# session.commit()
# cheesepizza = MenuItem(name = "Cheese Pizza", description = "Pizza with cheese", course = "Entree", price = "$9.99", restaurant = MyFirstRestaurant)
# session.add(cheesepizza)
# session.commit()
# veggieBurger = MenuItem(name = "Veggie Burger", description = "Veggie Burger", course = "Starter", price = "$19.99", restaurant = MyFirstRestaurant)
# veggieBurger1 = MenuItem(name = "Veggie Burger1", description = "Veggie Burger", course = "Starter", price = "$119.99", restaurant = MyFirstRestaurant)
# session.add(veggieBurger)
# session.add(veggieBurger1)
# session.commit()

# #read
# items = session.query(MenuItem).all()
# for item in items:
#     print(item.name)

# #update
# veggieBurgers = session.query(MenuItem).filter_by(name = 'Veggie Burger')
# for burger in veggieBurgers:
#     print(burger.name)
#     burger.price = "$2.99"
#     session.add(burger)
#     session.commit()
# session.commit()
# pizza = session.query(MenuItem).filter_by(name = "Cheese Pizza", id = 1).one()
# pizza.price = "$1"
# session.add(pizza)
# session.commit()

# #delete
# veggieBurgers = session.query(MenuItem).filter_by(name = 'Veggie Burger1')

# for burger in veggieBurgers:
#     print(burger.name)
#     session.delete(burger)
# session.commit()
