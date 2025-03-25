import re

class CustomDict:
    def __init__(self, dictionary=None):
        self._data = {}
        
        if dictionary is not None:
            if isinstance(dictionary, CustomDict):
                self._data = dictionary._data.copy()
            else:
                for key, value in dictionary.items():
                    self[key] = value
    
    def __str__(self):
        return str(self._data)
    
    def __repr__(self):
        return f"CustomDict({self._data})"
    
    def __getitem__(self, key):
        self._validate_key(key)
        return self._data.get(key, 0)
    
    def __setitem__(self, key, value):
        self._validate_key(key)
        self._validate_value(value)
        self._data[key] = value
    
    def __delitem__(self, key):
        self._validate_key(key)
        if key in self._data:
            del self._data[key]
    
    def __len__(self):
        return len(self._data)
    
    def __contains__(self, key):
        self._validate_key(key)
        return key in self._data
    
    def __iadd__(self, other):
        if not isinstance(other, CustomDict):
            raise TypeError("Правий операнд має бути екземпляром класу CustomDict")
        
        for key, value in other._data.items():
            if key in self._data:
                self._data[key] += value
            else:
                self._data[key] = value
        
        return self
    
    def _validate_key(self, key):
        if not isinstance(key, str):
            raise TypeError("Ключ має бути рядком")
        
        if not re.match(r'^[а-яіїєґА-ЯІЇЄҐa-zA-Z]+$', key):
            raise ValueError("Ключ має містити лише літери українського або англійського алфавіту")
    
    def _validate_value(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Значення має бути числовим типом (int, float)")
    
    def keys(self):
        return self._data.keys()
    
    def values(self):
        return self._data.values()
    
    def items(self):
        return self._data.items()
    
    def get(self, key, default=0):
        self._validate_key(key)
        return self._data.get(key, default)
    
    def pop(self, key, default=None):
        self._validate_key(key)
        return self._data.pop(key, default)
    
    def clear(self):
        self._data.clear()
    
    def copy(self):
        return CustomDict(self)
    
    def update(self, other):
        if isinstance(other, CustomDict):
            for key, value in other._data.items():
                self[key] = value
        else:
            for key, value in other.items():
                self[key] = value
        
        return self
    
    def word_count(self, text):
        result = CustomDict()
        words = re.findall(r'[а-яіїєґА-ЯІЇЄҐa-zA-Z]+', text)
        
        for word in words:
            if word in result:
                result[word] += 1
            else:
                result[word] = 1
        
        return result
    
    def most_common(self, n=1):
        sorted_items = sorted(self._data.items(), key=lambda x: x[1], reverse=True)
        return sorted_items[:n]
    
    def words_with_count(self, count):
        return [key for key, value in self._data.items() if value == count]
    
    def longest_word(self):
        if not self._data:
            return None
        return max(self._data.keys(), key=len)
    
    def shortest_word(self):
        if not self._data:
            return None
        return min(self._data.keys(), key=len) 