from task_11 import Dessert

class JellyBean(Dessert):
    def init(self, name="Undefined", calories=None, flavor='Undefined flavor'):
        super().init(name, calories)
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
        return self._flavor.lower() != "black licorice"
    
    def str(self):
        return f"Desert has name: {self._name}\tcalories: {self._calories}\tflavor: {self._flavor}"
