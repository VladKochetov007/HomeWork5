class Monom:
    def __init__(self, coefficient: int, degree: int):
        self.coefficient = coefficient
        self.degree = degree

    def __str__(self):
        if self.degree == 0:
            return f"{self.coefficient}"
        return f"{self.coefficient}x^{self.degree}"
    
    @classmethod
    def from_string(cls, monom_str: str) -> 'Monom':
        try:
            m = float(monom_str)
            return cls(m, 0)
        except ValueError:
            pass
        
        parts = monom_str.split('x^')
        if len(parts) == 1:
            if 'x' in parts[0]:
                parts[0] = parts[0].replace('x', '1')
            else:
                parts[0] = parts[0].replace(' ', '')
            coefficient = int(parts[0])
            degree = 1
        else:
            coefficient = int(parts[0])
            degree = int(parts[1])
        return cls(coefficient, degree)
    

class Polynom:
    def __init__(self, monomials: list[Monom]):
        self.monomials = monomials
    
    @classmethod
    def from_string(cls, polynom_str: str) -> 'Polynom':
        monomials = []
        for monom_str in polynom_str.split(' + '):
            monomials.append(Monom.from_string(monom_str))
        return cls(monomials)
        
    def __str__(self):
        return " + ".join(str(m) for m in self.monomials)

    def sort_degree(self):
        self.monomials.sort(key=lambda x: x.degree, reverse=True)

    def print_monomials(self):
        for monom in self.monomials:
            print(monom)

if __name__ == '__main__':
    polynom_str = "3x^5 + 2x^2 + 1"
    polynom = Polynom.from_string(polynom_str)
    polynom.sort_degree()
    polynom.print_monomials()
