class Dessert:

    def __init__(self, name = "Undefined", calories: any = None):
        self._name = name
        self._calories = calories

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        try:
            self._name = str(value)
        except Exception as e:
            print(str(e))

    @property
    def calories(self):
        return self._calories

    @calories.setter
    def calories(self, value):
        try:
            typed_value = str(value)
            self._calories = typed_value
        except Exception as e:
            print(str(e))


    def is_healthy(self) -> bool:
        try:
            return float(self._calories) < 200
        except:
            return False
    
    def is_delicious(self) -> bool:
        return True
    
    def __str__(self):
        return f"Desert has name: {self._name}\tcalories: {self._calories}"
    


dessert = Dessert()
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
print(dessert.is_healthy())

dessert.calories = 300
print(dessert.calories)

print(dessert.is_healthy())

if dessert.is_healthy(): raise Exception("Logical error. Method must return False")
print(dessert.is_delicious())

if not dessert.is_delicious(): raise Exception("Invalid method result")
dessert.calories = 200
print(dessert.calories)

print(dessert.is_healthy())

if dessert.is_healthy(): raise Exception("Logical error. Method must return False")

