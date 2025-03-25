class Polynom:
    def __init__(self, coefficients=None):
        if coefficients is None:
            self.coefficients = [0]
        elif isinstance(coefficients, Polynom):
            self.coefficients = coefficients.coefficients.copy()
        elif isinstance(coefficients, (int, float)):
            self.coefficients = [coefficients]
        else:
            self.coefficients = list(coefficients)
            
        self._remove_leading_zeros()
    
    def _remove_leading_zeros(self):
        while len(self.coefficients) > 1 and self.coefficients[-1] == 0:
            self.coefficients.pop()
    
    def __str__(self):
        if all(c == 0 for c in self.coefficients):
            return "0"
        
        terms = []
        for i, coef in enumerate(self.coefficients):
            if coef == 0:
                continue
                
            if i == 0:
                terms.append(str(coef))
            elif i == 1:
                if coef == 1:
                    terms.append("x")
                elif coef == -1:
                    terms.append("-x")
                else:
                    terms.append(f"{coef}x")
            else:
                if coef == 1:
                    terms.append(f"x^{i}")
                elif coef == -1:
                    terms.append(f"-x^{i}")
                else:
                    terms.append(f"{coef}x^{i}")
        
        return " + ".join(terms).replace("+ -", "- ")
    
    def __repr__(self):
        return f"Polynom({self.coefficients})"
    
    def __getitem__(self, index):
        if 0 <= index < len(self.coefficients):
            return self.coefficients[index]
        return 0
    
    def __setitem__(self, index, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Coefficients must be numbers")
        
        if index < 0:
            raise IndexError("Index cannot be negative")
        
        if index >= len(self.coefficients):
            self.coefficients.extend([0] * (index - len(self.coefficients) + 1))
        
        self.coefficients[index] = value
        self._remove_leading_zeros()
    
    def __call__(self, x):
        result = 0
        for i, coef in enumerate(self.coefficients):
            result += coef * (x ** i)
        return result
    
    def __add__(self, other):
        if isinstance(other, (int, float)):
            result = Polynom(self.coefficients)
            result.coefficients[0] += other
            return result
        
        if not isinstance(other, Polynom):
            other = Polynom(other)
        
        result_coeffs = []
        max_len = max(len(self.coefficients), len(other.coefficients))
        
        for i in range(max_len):
            a = self[i]
            b = other[i]
            result_coeffs.append(a + b)
        
        return Polynom(result_coeffs)
    
    def __radd__(self, other):
        return self + other
    
    def __sub__(self, other):
        if isinstance(other, (int, float)):
            result = Polynom(self.coefficients)
            result.coefficients[0] -= other
            return result
        
        if not isinstance(other, Polynom):
            other = Polynom(other)
        
        result_coeffs = []
        max_len = max(len(self.coefficients), len(other.coefficients))
        
        for i in range(max_len):
            a = self[i]
            b = other[i]
            result_coeffs.append(a - b)
        
        return Polynom(result_coeffs)
    
    def __rsub__(self, other):
        return -self + other
    
    def __neg__(self):
        return Polynom([-c for c in self.coefficients])
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Polynom([c * other for c in self.coefficients])
        
        if not isinstance(other, Polynom):
            other = Polynom(other)
        
        result_degree = len(self.coefficients) + len(other.coefficients) - 1
        result_coeffs = [0] * result_degree
        
        for i, a in enumerate(self.coefficients):
            for j, b in enumerate(other.coefficients):
                result_coeffs[i + j] += a * b
        
        return Polynom(result_coeffs)
    
    def __rmul__(self, other):
        return self * other
    
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Division by zero")
            return Polynom([c / other for c in self.coefficients])
        
        raise NotImplementedError("Polynomial division is not supported")
    
    def derivative(self):
        if len(self.coefficients) <= 1:
            return Polynom([0])
        
        result_coeffs = [self.coefficients[i] * i for i in range(1, len(self.coefficients))]
        return Polynom(result_coeffs)
    
    def integral(self, constant=0):
        result_coeffs = [constant]
        for i, coef in enumerate(self.coefficients):
            result_coeffs.append(coef / (i + 1))
        return Polynom(result_coeffs)
    
    def degree(self):
        return len(self.coefficients) - 1 