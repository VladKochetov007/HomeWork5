import math

class Vector:
    def __init__(self, components=None):
        self.components = []
        if components is not None:
            self.components = list(components)
    
    def __str__(self):
        return f"({', '.join(str(c) for c in self.components)})"
    
    def __repr__(self):
        return self.__str__()
    
    def __len__(self):
        return len(self.components)
    
    def __getitem__(self, index):
        return self.components[index]
    
    def __setitem__(self, index, value):
        self.components[index] = value
    
    def __add__(self, other):
        if not isinstance(other, Vector) or len(self) != len(other):
            raise ValueError("Can only add vectors of the same dimension")
        
        return type(self)([a + b for a, b in zip(self.components, other.components)])
    
    def __sub__(self, other):
        if not isinstance(other, Vector) or len(self) != len(other):
            raise ValueError("Can only subtract vectors of the same dimension")
        
        return type(self)([a - b for a, b in zip(self.components, other.components)])
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return type(self)([c * other for c in self.components])
        
        if isinstance(other, Vector) and len(self) == len(other):
            return sum(a * b for a, b in zip(self.components, other.components))
        
        raise ValueError("Incompatible types for multiplication operation")
    
    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return self * other
        
        raise ValueError("Incompatible types for multiplication operation")
    
    def length(self):
        return math.sqrt(sum(c * c for c in self.components))
    
    def normalize(self):
        length = self.length()
        if length == 0:
            raise ValueError("Cannot normalize zero vector")
        
        return type(self)([c / length for c in self.components])


class Vector2D(Vector):
    def __init__(self, x=0, y=0):
        if isinstance(x, (list, tuple)) and len(x) == 2:
            super().__init__(x)
        elif isinstance(x, Vector) and len(x) == 2:
            super().__init__(x.components)
        else:
            super().__init__([x, y])
    
    @property
    def x(self):
        return self.components[0]
    
    @x.setter
    def x(self, value):
        self.components[0] = value
    
    @property
    def y(self):
        return self.components[1]
    
    @y.setter
    def y(self, value):
        self.components[1] = value
    
    def cross(self, other):
        if not isinstance(other, Vector2D):
            raise ValueError("Cross product is only defined for Vector2D")
        
        return self.x * other.y - self.y * other.x


class Vector3D(Vector):
    def __init__(self, x=0, y=0, z=0):
        if isinstance(x, (list, tuple)) and len(x) == 3:
            super().__init__(x)
        elif isinstance(x, Vector) and len(x) == 3:
            super().__init__(x.components)
        else:
            super().__init__([x, y, z])
    
    @property
    def x(self):
        return self.components[0]
    
    @x.setter
    def x(self, value):
        self.components[0] = value
    
    @property
    def y(self):
        return self.components[1]
    
    @y.setter
    def y(self, value):
        self.components[1] = value
    
    @property
    def z(self):
        return self.components[2]
    
    @z.setter
    def z(self, value):
        self.components[2] = value
    
    def cross(self, other):
        if not isinstance(other, Vector3D):
            raise ValueError("Cross product is only defined for Vector3D")
        
        return Vector3D(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )


class Matrix:
    def __init__(self, rows, cols, values=None):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]
        
        if values is not None:
            if isinstance(values, Matrix):
                for i in range(min(rows, values.rows)):
                    for j in range(min(cols, values.cols)):
                        self.data[i][j] = values.data[i][j]
            else:
                flat_values = list(values) if hasattr(values, '__iter__') else [values]
                for i in range(rows):
                    for j in range(cols):
                        idx = i * cols + j
                        if idx < len(flat_values):
                            self.data[i][j] = flat_values[idx]
    
    def __str__(self):
        result = []
        for row in self.data:
            result.append(' '.join(str(x) for x in row))
        return '\n'.join(result)
    
    def __repr__(self):
        return self.__str__()
    
    def __getitem__(self, index):
        if isinstance(index, tuple) and len(index) == 2:
            row, col = index
            return self.data[row][col]
        else:
            return self.data[index]
    
    def __setitem__(self, index, value):
        if isinstance(index, tuple) and len(index) == 2:
            row, col = index
            self.data[row][col] = value
        else:
            if isinstance(value, Vector) and len(value) == self.cols:
                self.data[index] = list(value.components)
            elif hasattr(value, '__iter__') and len(value) == self.cols:
                self.data[index] = list(value)
            else:
                raise ValueError("Invalid dimensions for assignment")
    
    def __add__(self, other):
        if not isinstance(other, Matrix) or self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Can only add matrices of the same size")
        
        result = type(self)(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        
        return result
    
    def __sub__(self, other):
        if not isinstance(other, Matrix) or self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Can only subtract matrices of the same size")
        
        result = type(self)(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] - other.data[i][j]
        
        return result
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            result = type(self)(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result.data[i][j] = self.data[i][j] * other
            return result
        
        if isinstance(other, Vector) and len(other) == self.cols:
            result = [0] * self.rows
            for i in range(self.rows):
                for j in range(self.cols):
                    result[i] += self.data[i][j] * other[j]
            
            if self.rows == 2:
                return Vector2D(result)
            elif self.rows == 3:
                return Vector3D(result)
            else:
                return Vector(result)
        
        if isinstance(other, Matrix) and self.cols == other.rows:
            result = type(self)(self.rows, other.cols)
            for i in range(self.rows):
                for j in range(other.cols):
                    for k in range(self.cols):
                        result.data[i][j] += self.data[i][k] * other.data[k][j]
            return result
        
        raise ValueError("Incompatible types for multiplication operation")
    
    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return self * other
        
        raise ValueError("Incompatible types for multiplication operation")
    
    def __call__(self):
        return self.determinant()
    
    def transpose(self):
        result = type(self)(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[j][i] = self.data[i][j]
        return result
    
    def minor(self, row, col):
        result = type(self)(self.rows - 1, self.cols - 1)
        r = 0
        for i in range(self.rows):
            if i == row:
                continue
            c = 0
            for j in range(self.cols):
                if j == col:
                    continue
                result.data[r][c] = self.data[i][j]
                c += 1
            r += 1
        return result
    
    def determinant(self):
        if self.rows != self.cols:
            raise ValueError("Determinant is only defined for square matrices")
        
        if self.rows == 1:
            return self.data[0][0]
        
        if self.rows == 2:
            return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]
        
        result = 0
        for j in range(self.cols):
            result += ((-1) ** j) * self.data[0][j] * self.minor(0, j).determinant()
        
        return result


class Matrix2D(Matrix):
    def __init__(self, values=None):
        super().__init__(2, 2, values)
    
    def __call__(self):
        return self.determinant()


class Matrix3D(Matrix):
    def __init__(self, values=None):
        super().__init__(3, 3, values)
    
    def __call__(self):
        return self.determinant() 