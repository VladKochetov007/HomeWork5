class ProtectedDictInt:
    def __init__(self, dictionary=None):
        self._data = {}
        if dictionary is not None:
            for key, value in dictionary.items():
                if not isinstance(key, int):
                    raise TypeError("Keys must be integers")
                self._data[key] = value

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError("Keys must be integers")
        return self._data[key]

    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise TypeError("Keys must be integers")
        if key in self._data:
            raise ValueError(f"Cannot modify existing key: {key}")
        self._data[key] = value

    def __contains__(self, key):
        return key in self._data

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return str(self._data)

    def __add__(self, other):
        result = ProtectedDictInt(self._data)
        if isinstance(other, ProtectedDictInt):
            for key in other._data:
                if key in self._data:
                    raise ValueError(f"Dictionary already contains key: {key}")
                result[key] = other._data[key]
        elif isinstance(other, tuple) and len(other) == 2:
            key, value = other
            if not isinstance(key, int):
                raise TypeError("Key must be an integer")
            if key in self._data:
                raise ValueError(f"Dictionary already contains key: {key}")
            result[key] = value
        else:
            raise TypeError("Right operand must be ProtectedDictInt or a tuple (key, value)")
        return result

    def __sub__(self, key):
        if not isinstance(key, int):
            raise TypeError("Key must be an integer")
        result = ProtectedDictInt(self._data)
        if key in result._data:
            del result._data[key]
        return result 