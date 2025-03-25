from src.rational import Rational

class RationalList:
    def __init__(self, items=None):
        self._items = []
        if items is not None:
            if isinstance(items, RationalList):
                self._items = [item for item in items._items]
            else:
                for item in items:
                    if isinstance(item, Rational):
                        self._items.append(item)
                    elif isinstance(item, int):
                        self._items.append(Rational(item))
                    elif isinstance(item, str) and '/' in item:
                        self._items.append(Rational(item))
                    else:
                        raise TypeError("Items must be Rational, int, or string representation of a fraction")
    
    def __len__(self):
        return len(self._items)
    
    def __getitem__(self, index):
        return self._items[index]
    
    def __setitem__(self, index, value):
        if isinstance(value, Rational):
            self._items[index] = value
        elif isinstance(value, int):
            self._items[index] = Rational(value)
        elif isinstance(value, str) and '/' in value:
            self._items[index] = Rational(value)
        else:
            raise TypeError("Value must be Rational, int, or string representation of a fraction")
    
    def __add__(self, other):
        result = RationalList(self._items)
        
        if isinstance(other, RationalList):
            for item in other._items:
                result._items.append(item)
        elif isinstance(other, (Rational, int)):
            if isinstance(other, int):
                other = Rational(other)
            result._items.append(other)
        else:
            raise TypeError("Unsupported operand type")
        
        return result
    
    def __iadd__(self, other):
        if isinstance(other, RationalList):
            for item in other._items:
                self._items.append(item)
        elif isinstance(other, (Rational, int)):
            if isinstance(other, int):
                other = Rational(other)
            self._items.append(other)
        else:
            raise TypeError("Unsupported operand type")
        
        return self
    
    def __eq__(self, other):
        if not isinstance(other, RationalList):
            return False
        if len(self) != len(other):
            return False
        return all(self[i] == other[i] for i in range(len(self)))
    
    def __repr__(self):  # It is usually better to use __repr__ in development
        return '[' + ', '.join(str(item) for item in self._items) + ']'
    
    def sum(self):
        if not self._items:
            return Rational(0)
        result = Rational(self._items[0])
        for item in self._items[1:]:
            result += item
        return result 