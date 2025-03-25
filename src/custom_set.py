class CustomSet:
    def __init__(self, elements=None):
        self._elements = set()
        if elements is not None:
            if isinstance(elements, CustomSet):
                self._elements = elements._elements.copy()
            else:
                for item in elements:
                    self._elements.add(item)
    
    def __str__(self):
        if not self._elements:
            return "∅"
        return "{" + ", ".join(str(element) for element in self._elements) + "}"
    
    def __repr__(self):
        return self.__str__()
    
    def __len__(self):
        return len(self._elements)
    
    def __contains__(self, item):
        return item in self._elements
    
    def __iter__(self):
        return iter(self._elements)
    
    def __add__(self, other):
        result = CustomSet(self._elements)
        
        if isinstance(other, CustomSet):
            result._elements.update(other._elements)
        else:
            result._elements.add(other)
        
        return result
    
    def __mul__(self, other):
        result = CustomSet()
        
        if isinstance(other, CustomSet):
            result._elements = self._elements.intersection(other._elements)
        else:
            if other in self._elements:
                result._elements.add(other)
        
        return result
    
    def __sub__(self, other):
        result = CustomSet(self._elements)
        
        if isinstance(other, CustomSet):
            result._elements.difference_update(other._elements)
        else:
            result._elements.discard(other)
        
        return result
    
    def __truediv__(self, other):
        if isinstance(other, CustomSet):
            result = CustomSet()
            result._elements = self._elements.symmetric_difference(other._elements)
            return result
        else:
            result = CustomSet(self._elements)
            if other in result._elements:
                result._elements.remove(other)
            else:
                result._elements.add(other)
            return result
    
    def add(self, item):
        self._elements.add(item)
    
    def remove(self, item):
        self._elements.remove(item)
    
    def discard(self, item):
        self._elements.discard(item)
    
    def clear(self):
        self._elements.clear()
    
    def union(self, other):
        return self + other
    
    def intersection(self, other):
        return self * other
    
    def difference(self, other):
        return self - other
    
    def symmetric_difference(self, other):
        return self / other 