class MutableString:
    def __init__(self, text=""):
        if isinstance(text, MutableString):
            self._chars = list(text._chars)
        else:
            self._chars = list(str(text))
    
    def __str__(self):
        return ''.join(self._chars)
    
    def __repr__(self):
        return f"MutableString('{self.__str__()}')"
    
    def __len__(self):
        return len(self._chars)
    
    def __getitem__(self, index):
        if isinstance(index, slice):
            return MutableString(''.join(self._chars[index]))
        return self._chars[index]
    
    def __setitem__(self, index, value):
        if isinstance(index, slice):
            if isinstance(value, MutableString):
                self._chars[index] = value._chars
            else:
                self._chars[index] = list(str(value))
        else:
            if isinstance(value, str) and len(value) == 1:
                self._chars[index] = value
            else:
                raise ValueError("Можна присвоїти лише один символ")
    
    def __add__(self, other):
        result = MutableString(self)
        
        if isinstance(other, MutableString):
            result._chars.extend(other._chars)
        else:
            result._chars.extend(list(str(other)))
        
        return result
    
    def __mul__(self, times):
        if not isinstance(times, int):
            raise TypeError("Множник має бути цілим числом")
        
        result = MutableString()
        for _ in range(times):
            result._chars.extend(self._chars)
        
        return result
    
    def __contains__(self, item):
        if isinstance(item, MutableString):
            item = str(item)
        
        if len(item) == 1:
            return item in self._chars
        
        return item in str(self)
    
    def replace(self, old, new):
        if isinstance(old, MutableString):
            old = str(old)
        if isinstance(new, MutableString):
            new = str(new)
            
        text = str(self).replace(old, new)
        return MutableString(text)
    
    def lower(self):
        return MutableString(str(self).lower())
    
    def upper(self):
        return MutableString(str(self).upper())
    
    def strip(self):
        return MutableString(str(self).strip())
    
    def index(self, sub, start=0, end=None):
        if end is None:
            end = len(self._chars)
            
        return str(self)[start:end].index(str(sub))
    
    def find(self, sub, start=0, end=None):
        if end is None:
            end = len(self._chars)
            
        return str(self)[start:end].find(str(sub)) 