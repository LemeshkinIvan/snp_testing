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
    

dessert = JellyBean()
if not issubclass(dessert.__class__, JellyBean): raise Exception("Invalid inheritance")
dessert.name = "test_name"
print(dessert.name)

dessert.name = "test_name2"
print(dessert.name)

if dessert.name != "test_name2": raise Exception("Setter for name is not working")
dessert.calories = "test_calories"
print(dessert.calories)

dessert.calories = "test_calories2"
print(dessert.calories)

if dessert.calories != "test_calories2": raise Exception("Setter for calories is not working")
print(dessert.is_delicious())

if not dessert.is_delicious(): raise Exception("Invalid method result")
dessert.flavor = "test_flavor"
print(dessert.flavor)

print(dessert.is_healthy())

dessert.calories = 300
print(dessert.calories)
300
print(dessert.is_healthy())

if dessert.is_healthy(): raise Exception("Logical error. Method must return False")
print(dessert.is_delicious())

if not dessert.is_delicious(): raise Exception("Invalid method result")
dessert.calories = 200
print(dessert.calories)
200
print(dessert.is_healthy())

if dessert.is_healthy(): raise Exception("Logical error. Method must return False")