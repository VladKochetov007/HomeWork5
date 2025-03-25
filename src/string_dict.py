import re

class StringDict:
    def __init__(self, dictionary=None):
        self._data = {}
        
        if dictionary is not None:
            if isinstance(dictionary, StringDict):
                for key, value in dictionary._data.items():
                    self._data[key] = value.copy()
            else:
                for key, value in dictionary.items():
                    self[key] = value
    
    def __str__(self):
        return str(self._data)
    
    def __repr__(self):
        return f"StringDict({self._data})"
    
    def __getitem__(self, key):
        self._validate_key(key)
        return self._data.get(key, [])
    
    def __setitem__(self, key, value):
        self._validate_key(key)
        self._validate_value(value)
        self._data[key] = value if isinstance(value, list) else [value]
    
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
        if not isinstance(other, StringDict):
            raise TypeError("Правий операнд має бути екземпляром класу StringDict")
        
        for key, value in other._data.items():
            if key in self._data:
                for item in value:
                    if item not in self._data[key]:
                        self._data[key].append(item)
            else:
                self._data[key] = value.copy()
        
        return self
    
    def _validate_key(self, key):
        if not isinstance(key, str):
            raise TypeError("Ключ має бути рядком")
        
        if not re.match(r'^[а-яіїєґА-ЯІЇЄҐa-zA-Z]+$', key):
            raise ValueError("Ключ має містити лише літери українського або англійського алфавіту")
    
    def _validate_value(self, value):
        if isinstance(value, list):
            for item in value:
                if not isinstance(item, str):
                    raise TypeError("Елементи списку значень мають бути рядками")
                
                if not re.match(r'^[а-яіїєґА-ЯІЇЄҐa-zA-Z]+$', item):
                    raise ValueError("Елементи списку значень мають містити лише літери українського або англійського алфавіту")
        elif isinstance(value, str):
            if not re.match(r'^[а-яіїєґА-ЯІЇЄҐa-zA-Z]+$', value):
                raise ValueError("Значення має містити лише літери українського або англійського алфавіту")
        else:
            raise TypeError("Значення має бути рядком або списком рядків")
    
    def keys(self):
        return self._data.keys()
    
    def values(self):
        return self._data.values()
    
    def items(self):
        return self._data.items()
    
    def get(self, key, default=None):
        self._validate_key(key)
        return self._data.get(key, default or [])
    
    def pop(self, key, default=None):
        self._validate_key(key)
        return self._data.pop(key, default or [])
    
    def clear(self):
        self._data.clear()
    
    def copy(self):
        return StringDict(self)
    
    def update(self, other):
        if isinstance(other, StringDict):
            for key, value in other._data.items():
                if key in self._data:
                    for item in value:
                        if item not in self._data[key]:
                            self._data[key].append(item)
                else:
                    self._data[key] = value.copy()
        else:
            for key, value in other.items():
                if key in self._data:
                    value_list = value if isinstance(value, list) else [value]
                    for item in value_list:
                        if item not in self._data[key]:
                            self._data[key].append(item)
                else:
                    self._data[key] = value if isinstance(value, list) else [value]
        
        return self
    
    def add_translation(self, eng, ukr):
        self._validate_key(eng)
        self._validate_value(ukr)
        
        ukr_list = ukr if isinstance(ukr, list) else [ukr]
        
        if eng in self._data:
            for word in ukr_list:
                if word not in self._data[eng]:
                    self._data[eng].append(word)
        else:
            self._data[eng] = ukr_list
    
    def create_reverse_dict(self):
        result = StringDict()
        
        for eng, ukr_list in self._data.items():
            for ukr in ukr_list:
                if ukr in result._data:
                    if eng not in result._data[ukr]:
                        result._data[ukr].append(eng)
                else:
                    result._data[ukr] = [eng]
        
        return result
    
    def get_translations(self, word):
        self._validate_key(word)
        return self._data.get(word, [])
    
    def word_with_most_translations(self):
        if not self._data:
            return None
        
        return max(self._data.items(), key=lambda x: len(x[1]))[0]
    
    def words_with_single_translation(self):
        return [key for key, value in self._data.items() if len(value) == 1]
    
    def count_unique_words(self):
        return len(self._data)
    
    def count_unique_translations(self):
        unique_translations = set()
        for values in self._data.values():
            for value in values:
                unique_translations.add(value)
        
        return len(unique_translations) 