from task_11 import Dessert

class JellyBean(Dessert):
    def __init__(self, name = "Undefined", calories = 0.0, flavor = 'Undefined flavor'):
        super().__init__(name, calories)
        self._flavor = flavor

    def set_flavor(self, value):
        try:
            typed_value = str(value)
            self._flavor = typed_value if typed_value != '' else "Undefined flavor"
        except Exception as e:
            print(str(e))

    @property
    def get_flavor(self):
        return self._flavor
    
    def is_delicious(self):       
        # !(bool value) 
        return not(self._flavor == "black licorise")
    
    def __str__(self):
        return f"Desert has name: {self._name}\tcalories: {self._calories}\tflavor: {self._flavor}"
    

# test
desert_1 = JellyBean(name= "Cake", calories= 100, flavor= "bitter")
print(desert_1.is_delicious())
print(desert_1.__str__())

desert_2 = JellyBean(name= "Cake 2", flavor= "black licorice")
print(desert_2.is_delicious())
print(desert_2.__str__())