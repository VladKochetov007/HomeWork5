from math import gcd

class Rational:
    def __init__(self, numerator=0, denominator=1):
        if isinstance(numerator, Rational):
            self.n = numerator.n
            self.d = numerator.d
            return
        
        if isinstance(numerator, str):
            if '/' in numerator:
                parts = numerator.split('/')
                numerator = int(parts[0])
                denominator = int(parts[1])
            else:
                numerator = int(numerator)
        
        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero")
        
        g = abs(gcd(numerator, denominator))
        
        if denominator < 0:
            numerator, denominator = -numerator, -denominator
            
        self.n = numerator // g
        self.d = denominator // g
    
    def __str__(self):
        if self.d == 1:
            return f"{self.n}"
        return f"{self.n}/{self.d}"
    
    def __add__(self, other):
        if isinstance(other, int):
            other = Rational(other)
        if not isinstance(other, Rational):
            raise TypeError("Unsupported operand type")
        
        return Rational(self.n * other.d + other.n * self.d, self.d * other.d)
    
    def __sub__(self, other):
        if isinstance(other, int):
            other = Rational(other)
        if not isinstance(other, Rational):
            raise TypeError("Unsupported operand type")
        
        return Rational(self.n * other.d - other.n * self.d, self.d * other.d)
    
    def __mul__(self, other):
        if isinstance(other, int):
            other = Rational(other)
        if not isinstance(other, Rational):
            raise TypeError("Unsupported operand type")
        
        return Rational(self.n * other.n, self.d * other.d)
    
    def __truediv__(self, other):
        if isinstance(other, int):
            other = Rational(other)
        if not isinstance(other, Rational):
            raise TypeError("Unsupported operand type")
        if other.n == 0:
            raise ZeroDivisionError("Division by zero")
        
        return Rational(self.n * other.d, self.d * other.n)
    
    def __call__(self):
        return self.n / self.d
    
    def __getitem__(self, key):
        if key == "n":
            return self.n
        elif key == "d":
            return self.d
        else:
            raise KeyError("Invalid key. Use 'n' for numerator or 'd' for denominator")
    
    def __setitem__(self, key, value):
        if not isinstance(value, int):
            raise TypeError("Value must be an integer")
        
        if key == "n":
            self.n = value
            g = abs(gcd(self.n, self.d))
            self.n //= g
            self.d //= g
        elif key == "d":
            if value == 0:
                raise ZeroDivisionError("Denominator cannot be zero")
            self.d = value
            g = abs(gcd(self.n, self.d))
            self.n //= g
            self.d //= g
        else:
            raise KeyError("Invalid key. Use 'n' for numerator or 'd' for denominator") 
    
    def __repr__(self) -> str:
        return f"({self.n} / {self.d})"
    
    def __eq__(self, other):
        if isinstance(other, int):
            other = Rational(other)
        if not isinstance(other, Rational):
            return False
        return self.n * other.d == other.n * self.d