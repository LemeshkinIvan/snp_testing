class EvenNumbers:

    def __init__(self, n = 1):
        self._n = n
        self._current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._current < self._n:
            value = self._current
            self._current += 1
            return 2*(self._current - 1)    
        else:
            raise StopIteration

    

for el in EvenNumbers(5):
    print(el)