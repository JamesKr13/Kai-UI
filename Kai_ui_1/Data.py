
from dataclasses import dataclass

@dataclass
class Item:
    _name: str
    _price: float
    _is_vegan: bool
    _is_vegeterain: bool
    _contains_sugar: bool
    _days_avaliable: list

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, _new_name):
        self._name = _new_name

    @property
    def price(self) -> int:
        return self._price

    @price.setter
    def price(self, new_price):
        self._price = new_price

    @property
    def is_vegan(self) -> bool:
        return self._is_vegan
    
    @is_vegan.setter
    def is_vegan(self, change_is_vegan):
        if type(change_is_vegan) == bool:
            self._is_vegan = False
        else:
            raise TypeError
    @property
    def is_vegeterain(self) -> bool:
        return self._is_vegeterain
    
    @is_vegeterain.setter
    def is_vegeterain(self, change_is_vegeterain):
        if type(change_is_vegeterain) == bool:
            self._is_vegeterain = False
        else:
            raise TypeError
    
    @property
    def contains_sugar(self) -> bool:
        return self._contains_sugar
    
    @contains_sugar.setter
    def contains_sugar(self, change_contains_sugar):
        if type(change_contains_sugar) == bool:
            self._contains_sugar = change_contains_sugar
        else:
            raise TypeError
    
    @property
    def days_avaliable(self):
        return self._days_avaliable
    
    @days_avaliable.setter
    def days_avaliable(self,week_change):
        if not week_change:
            self.days_avaliable = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
        elif type(week_change ) is list:
            self._days_avaliable = week_change
        elif week_change not in self._days_avaliable:
            self._days_avaliable.append(week_change)
        else:
            self._days_avaliable.pop(self._days_avaliable.index(week_change))

class Sandwiches(Item):
    def __init__(self, name, price, contains_sugar, is_vegan, is_vegeterain, days):
        super().__init__(name,price, contains_sugar, is_vegan, is_vegeterain, days)
class Sushi(Item):
    def __init__(self, name, price, contains_sugar, is_vegan, is_vegeterain, days):
        super().__init__(name,price, contains_sugar, is_vegan, is_vegeterain, days)
class Drinks(Item):
    def __init__(self, name, price, contains_sugar, is_vegan, is_vegeterain, days):
        super().__init__(name,price, contains_sugar, is_vegan, is_vegeterain, days)
class Specials(Item):
    def __init__(self, name, price, contains_sugar, is_vegan, is_vegeterain, days):
        super().__init__(name,price, contains_sugar, is_vegan, is_vegeterain, days)

def set_catergories(catergories,name,item_price,sugar,v_option=False,vg_option=False,*days):
    obj = catergories(name,item_price,sugar,v_option,v_option,days)
    return obj
_load = {
    Sandwiches:[["Ham & egg sandwich",False,False,False,3.5],
                ["Chicken mayo sandwich",False,False,False,3.5],
                ["Egg sandwich",False,True,False,3.0],
                ["Beef sandwich",False,False,False,3.8],
                ["Salad sandwich",False,True,True,3.2]],
    Sushi:[["Chicken (3pc)",False,True,True,4.5],
        ["Tuna (3pc)",False,True,True,4.5],
        ["Avocado sushi (3pc)",False,True,False,4.8],
        ["Chicken rice bowl",False,True,True,5.5],
        ["Vegetarian rice bowl",False,True,True,5.5]],
    Drinks:[["Soda Can",True,True,True,2.0],
            ["Aloe Vera Drink",True,False,True,3.5],
            ["Chocolate Milk",True,False,False,3.5],
            ["Water Bottle",False,True,True,2.5],
            ["Instant Hot Chocoloate",True,True,False,1.5]],
    Specials:[["Kale Moa",True,False,False,6.0,"Monday"],
                ["Potjiekos",False,False,False,6.0,"Tuesday"],
                ["Hangi",False,True,True,6.0,"Wednesday"],
                ["Paneer tikka masala",True,True,False,6.0,"Thursday"],
                ["Chow Mein",False,True,True,6.0,"Friday"]]
}

def days_of_the_week(index):
    return ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][index]

counter = 0
all_class = []
for _class, item in _load.items():
    for item_values in item:
        counter += 1
        var_name = f"obj{counter}"
        vars()[var_name] = set_catergories(_class,item_values[0],item_values[4],item_values[1],item_values[2],item_values[3],list(item_values[5:]))
        all_class.append(vars()[var_name])