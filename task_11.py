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
            return float(self._calories) <= 200
        except:
            return True
    
    def is_delicious(self) -> bool:
        return True
    
    def __str__(self):
        return f"Desert has name: {self._name}\tcalories: {self._calories}"
    


desert_1 = Dessert()
print(desert_1.is_healthy())
print(desert_1.is_delicious())
print(desert_1.__str__())
print("------------")

desert_2 = Dessert("ugug", 400)
print(desert_2.is_healthy())
print(desert_2.is_delicious())
print(desert_2._calories)
desert_2.calories = 300
print(desert_2.__str__())
desert_2.calories = "test_calories"
print(desert_2.is_healthy())
print(desert_2.__str__())
print("------------")
