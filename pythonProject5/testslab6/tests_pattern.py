from decorator import Bicycle, Car, Colors
from singleton import Singleton
from factory import *
from observer import *


def test_bicycle_d():
    bicycle1 = Bicycle(10)
    des_string = 'Maximum bicycle speed: 10'
    assert str(bicycle1) == des_string


def test_car_d():
    car1 = Car(200, 2.5)
    des_string = 'The car has 200 h.p. and engine volume 2.5 l.'
    assert str(car1) == des_string
    car1.upgrade(50)
    des_string = 'The car has 250 h.p. and engine volume 2.5 l.'
    assert str(car1) == des_string


def test_colors_d():
    car2 = Colors('Car', 'black')
    bicycle2 = Colors('Bicycle', 'red')
    des_string1 = 'Car is black'
    des_string2 = 'Bicycle is red'
    assert str(car2) == des_string1
    assert str(bicycle2) == des_string2


def test_singleton():
    s1 = Singleton()
    s2 = Singleton()
    assert s1 == s2


def test_factory():
    new_food1 = create_food(FoodType.Burger)
    new_food2 = create_food(FoodType.Ice_Cream)
    assert new_food1.get_price() == 'Price is 150'
    assert new_food2.get_price() == 'Price is 100'


def test_observer():
    sub = Subject('Subject1')
    obs1 = Observer('Observer1', sub)
    obs2 = Observer('Observer2', sub)
    assert sub._observers == [obs1, obs2]
    sub.unsubscribe(obs2)
    assert sub._observers == [obs1]
