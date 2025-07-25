from task_11 import Dessert

class JellyBean(Dessert):
    def __init__(self, name = "Undefined", calories: any = None, flavor = 'Undefined flavor'):
        super().__init__(name, calories)
        self._flavor = flavor

    @property
    def flavor(self):
        return self._flavor    

    @flavor.setter
    def flavor(self, value):
        try:
            typed_value = str(value)
            self._flavor = typed_value if typed_value != '' else "Undefined flavor"
        except Exception as e:
            print(str(e))
    
    def is_delicious(self):       
        return not(self._flavor == "black licorise")
    
    def __str__(self):
        return f"Desert has name: {self._name}\tcalories: {self._calories}\tflavor: {self._flavor}"
    

# test
desert_1 = JellyBean(name= "Cake", calories= "", flavor= "bitter")
print(desert_1.is_delicious())
print(desert_1.__str__())

desert_2 = JellyBean(name= "Cake 2", flavor= "black licorice")
print(desert_2.is_delicious())
print(desert_2.__str__())