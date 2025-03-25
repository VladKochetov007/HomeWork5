class CustomList:
    def __init__(self, items=None):
        if items is None:
            self._items = []
        elif isinstance(items, CustomList):
            self._items = items._items.copy()
        else:
            self._items = []
            for item in items:
                if not isinstance(item, int):
                    raise TypeError("CustomList can only contain integers")
                self._items.append(item)
    
    def __str__(self):
        return str(self._items)
    
    def __repr__(self):
        return f"CustomList({self._items})"
    
    def __getitem__(self, index):
        return self._items[index]
    
    def __setitem__(self, index, value):
        if not isinstance(value, int):
            raise TypeError("CustomList can only contain integers")
        self._items[index] = value
    
    def __len__(self):
        return len(self._items)
    
    def __contains__(self, item):
        return item in self._items
    
    def __iadd__(self, other):
        if isinstance(other, CustomList):
            self._items.extend(other._items)
        elif isinstance(other, int):
            self._items.append(other)
        else:
            raise TypeError("Right operand must be CustomList or integer")
        return self
    
    def __isub__(self, other):
        if isinstance(other, CustomList):
            self._items = [item for item in self._items if item not in other._items]
        elif isinstance(other, int):
            while other in self._items:
                self._items.remove(other)
        else:
            raise TypeError("Right operand must be CustomList or integer")
        return self
    
    def __imul__(self, other):
        if not isinstance(other, int):
            raise TypeError("Right operand must be integer")
        if other <= 0:
            self._items = []
        else:
            original = self._items.copy()
            self._items = []
            for _ in range(other):
                self._items.extend(original)
        return self
    
    def count_non_zero(self):
        return sum(1 for item in self._items if item != 0)
    
    def sum(self):
        return sum(self._items) 