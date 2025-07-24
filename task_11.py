class Dessert:

    def __init__(self, name = "Undefined", calories = 0.0):
        self._name = name
        self._calories = calories

    def set_name(self, value):
        try:
            self._name = str(value)
        except Exception as e:
            print(str(e))

    def set_calories(self, value):
        try:
            typed_value = float(value)

            if typed_value > 0:
                self._calories = typed_value

        except Exception as e:
            print(str(e))

    @property
    def get_name(self):
        return self._name
    
    @property
    def get_calories(self):
        return self._calories

    def is_healthy(self) -> bool:
        return self._calories < 200
    
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
desert_2.set_calories(300)
print(desert_2.__str__())
print("------------")
