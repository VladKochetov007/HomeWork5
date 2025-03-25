class Sentence:
    def __init__(self, text=""):
        self.words = []
        
        if isinstance(text, Sentence):
            self.words = text.words.copy()
        elif isinstance(text, str):
            self.words = text.split()
        elif hasattr(text, '__iter__'):
            self.words = list(text)
    
    def __str__(self):
        return " ".join(self.words)
    
    def __repr__(self):
        return f"Sentence('{self.__str__()}')"
    
    def __len__(self):
        return len(self.words)
    
    def __getitem__(self, index):
        return self.words[index]
    
    def __setitem__(self, index, value):
        self.words[index] = value
    
    def __add__(self, other):
        result = Sentence(self.words)
        
        if isinstance(other, Sentence):
            result.words.extend(other.words)
        elif isinstance(other, str):
            result.words.append(other)
        else:
            raise TypeError("Можна додавати лише екземпляри класу Sentence або рядкові літерали")
        
        return result
    
    def __sub__(self, other):
        result = Sentence(self.words)
        
        if isinstance(other, Sentence):
            result.words = [word for word in result.words if word not in other.words]
        elif isinstance(other, str):
            while other in result.words:
                result.words.remove(other)
        else:
            raise TypeError("Можна віднімати лише екземпляри класу Sentence або рядкові літерали")
        
        return result
    
    def __contains__(self, item):
        return item in self.words
    
    def replace(self, old, new):
        result = Sentence(self.words)
        
        for i in range(len(result.words)):
            if result.words[i] == old:
                result.words[i] = new
        
        return result
    
    def count(self, word):
        return self.words.count(word)
    
    def add(self, word):
        self.words.append(word)
        return self
    
    def remove(self, word):
        while word in self.words:
            self.words.remove(word)
        return self
    
    def clear(self):
        self.words.clear()
        return self 