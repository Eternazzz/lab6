from enum import Enum


class FoodType(Enum):
    Burger = 1
    French_fries = 2
    Ice_Cream = 3


class Food:
    def __init__(self, price):
        self.price = price

    def get_price(self):
        return f'Price is {self.price}'


class Burger(Food):
    def __init__(self):
        super().__init__(150)


class FrenchFries(Food):
    def __init__(self):
        super().__init__(75)


class IceCream(Food):
    def __init__(self):
        super().__init__(100)


def create_food(food_type: FoodType) -> Food:
    dict1 = {FoodType.Ice_Cream: IceCream,
             FoodType.Burger: Burger,
             FoodType.French_fries: FrenchFries}
    return dict1[food_type]()
