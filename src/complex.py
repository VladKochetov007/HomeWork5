import math

class Complex:
    def __init__(self, real=0, imag=0):
        if isinstance(real, Complex):
            self.real = real.real
            self.imag = real.imag
        else:
            self.real = float(real)
            self.imag = float(imag)
    
    def __str__(self):
        if self.imag == 0:
            return f"{self.real}"
        elif self.real == 0:
            return f"{self.imag}i"
        elif self.imag < 0:
            return f"{self.real} - {abs(self.imag)}i"
        else:
            return f"{self.real} + {self.imag}i"
    
    def __repr__(self):
        return f"Complex({self.real}, {self.imag})"
    
    def __eq__(self, other):
        if isinstance(other, (int, float)):
            return self.real == other and self.imag == 0
        
        if not isinstance(other, Complex):
            return False
        
        return self.real == other.real and self.imag == other.imag
    
    def __add__(self, other):
        if isinstance(other, (int, float)):
            return Complex(self.real + other, self.imag)
        
        if not isinstance(other, Complex):
            other = Complex(other)
        
        return Complex(self.real + other.real, self.imag + other.imag)
    
    def __radd__(self, other):
        return self + other
    
    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return Complex(self.real - other, self.imag)
        
        if not isinstance(other, Complex):
            other = Complex(other)
        
        return Complex(self.real - other.real, self.imag - other.imag)
    
    def __rsub__(self, other):
        return -self + other
    
    def __neg__(self):
        return Complex(-self.real, -self.imag)
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Complex(self.real * other, self.imag * other)
        
        if not isinstance(other, Complex):
            other = Complex(other)
        
        return Complex(
            self.real * other.real - self.imag * other.imag,
            self.real * other.imag + self.imag * other.real
        )
    
    def __rmul__(self, other):
        return self * other
    
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Division by zero")
            return Complex(self.real / other, self.imag / other)
        
        if not isinstance(other, Complex):
            other = Complex(other)
        
        if other.real == 0 and other.imag == 0:
            raise ZeroDivisionError("Division by zero")
        
        denominator = other.real ** 2 + other.imag ** 2
        return Complex(
            (self.real * other.real + self.imag * other.imag) / denominator,
            (self.imag * other.real - self.real * other.imag) / denominator
        )
    
    def __rtruediv__(self, other):
        return Complex(other) / self
    
    def __pow__(self, other):
        if isinstance(other, int):
            result = Complex(1)
            for _ in range(abs(other)):
                result *= self
            
            if other < 0:
                result = 1 / result
            
            return result
        
        if isinstance(other, float):
            return self._power_float(other)
        
        if isinstance(other, Complex):
            return self._power_complex(other)
        
        raise TypeError("Unknown type")
    
    def _power_float(self, power):
        r, theta = self.polar()
        new_r = r ** power
        new_theta = theta * power
        return Complex.from_polar(new_r, new_theta)
    
    def _power_complex(self, power):
        if power.imag == 0:
            return self ** power.real
        
        r, theta = self.polar()
        if r == 0:
            return Complex(0)
        
        ln_r = math.log(r)
        return Complex.from_polar(
            math.exp(power.real * ln_r - power.imag * theta),
            power.real * theta + power.imag * ln_r
        )
    
    def conjugate(self):
        return Complex(self.real, -self.imag)
    
    def abs(self):
        return math.sqrt(self.real ** 2 + self.imag ** 2)
    
    def polar(self):
        r = self.abs()
        theta = math.atan2(self.imag, self.real)
        return r, theta
    
    @staticmethod
    def from_polar(r, theta):
        return Complex(r * math.cos(theta), r * math.sin(theta)) 