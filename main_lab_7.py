from src.protected_dict import ProtectedDictInt
from src.rational import Rational
from src.rational_list import RationalList
from src.custom_list import CustomList
from src.segment import Segment
from src.custom_set import CustomSet
from src.mutable_string import MutableString
from src.matrix import Matrix
from src.polynom import Polynom
from src.sentence import Sentence
from src.string_dict import StringDict

class ProtectedDictIntError(KeyError):
    def __init__(self, message: str):
        super().__init__(message)

class RationalError(ZeroDivisionError):
    def __init__(self, message: str = "Denominator cannot be zero"):
        super().__init__(message)

class RationalValueError(ValueError):
    def __init__(self, message: str):
        super().__init__(message)

class CustomListNotIntError(TypeError):
    def __init__(self, message: str = "Only integers are allowed"):
        super().__init__(message)

class SegmentError(ValueError):
    def __init__(self, message: str = "Start point cannot be greater than end point"):
        super().__init__(message)

class CustomSetError(TypeError):
    def __init__(self, message: str):
        super().__init__(message)

class IndexPositiveError(IndexError):
    def __init__(self, message: str):
        super().__init__(message)

class MatrixOperationError(ArithmeticError):
    def __init__(self, message: str):
        super().__init__(message)

class IndexValueError(ValueError):
    def __init__(self, message: str):
        super().__init__(message)

class DictStrIntError(ValueError):
    def __init__(self, message: str):
        super().__init__(message)

class StringDictError(ValueError):
    def __init__(self, message: str):
        super().__init__(message)

class DictIntFloat(dict):
    def __setitem__(self, key: int, value: float | int) -> None:
        if not isinstance(key, int):
            raise IndexValueError("Key must be an integer")
        if not isinstance(value, (float, int)):
            raise IndexValueError("Value must be float or integer")
        super().__setitem__(key, float(value))

class ModifiedProtectedDictInt(ProtectedDictInt):
    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise ProtectedDictIntError("Keys must be integers")
        if key in self._data:
            raise ProtectedDictIntError("Cannot modify existing key")
        self._data[key] = value

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise ProtectedDictIntError("Keys must be integers")
        return self._data[key]

class ModifiedRational(Rational):
    def __init__(self, numerator=0, denominator=1):
        try:
            if denominator == 0:
                raise RationalError()
            super().__init__(numerator, denominator)
        except ZeroDivisionError:
            raise RationalError()

    def __add__(self, other):
        try:
            return super().__add__(other)
        except TypeError:
            raise RationalValueError("Invalid operand type for addition")

    def __sub__(self, other):
        try:
            return super().__sub__(other)
        except TypeError:
            raise RationalValueError("Invalid operand type for subtraction")

class ModifiedRationalList(RationalList):
    def append(self, value):
        try:
            if not isinstance(value, (Rational, int)):
                raise RationalValueError("Can only append Rational or int values")
            super().append(value)
        except ValueError as e:
            raise RationalValueError(str(e))

class ModifiedCustomList(CustomList):
    def append(self, value):
        if not isinstance(value, int):
            raise CustomListNotIntError()
        super().append(value)

class ModifiedSegment(Segment):
    def __init__(self, start, end):
        if start > end:
            raise SegmentError()
        super().__init__(start, end)

class ModifiedCustomSet(CustomSet):
    def __init__(self):
        super().__init__()
        self._type = None

    def add(self, item):
        if self._type is None:
            self._type = type(item)
        elif not isinstance(item, self._type):
            raise CustomSetError(f"Item must be of type {self._type}")
        super().add(item)

    def __and__(self, other):
        if not isinstance(other, CustomSet) or self._type != other._type:
            raise CustomSetError("Sets must be of same type")
        return super().__and__(other)

    def __or__(self, other):
        if not isinstance(other, CustomSet) or self._type != other._type:
            raise CustomSetError("Sets must be of same type")
        return super().__or__(other)

    def __sub__(self, other):
        if not isinstance(other, CustomSet) or self._type != other._type:
            raise CustomSetError("Sets must be of same type")
        return super().__sub__(other)

class ModifiedMutableString(MutableString):
    def __getitem__(self, index):
        if not isinstance(index, int) or index < 0:
            raise IndexPositiveError(f"Invalid index: {index}")
        return super().__getitem__(index)

    def __setitem__(self, index, value):
        if not isinstance(index, int) or index < 0:
            raise IndexPositiveError(f"Invalid index: {index}")
        super().__setitem__(index, value)

class ModifiedMatrix(Matrix):
    def __add__(self, other):
        if not isinstance(other, Matrix) or self.rows != other.rows or self.cols != other.cols:
            raise MatrixOperationError("Matrix dimensions must match for addition")
        try:
            return super().__add__(other)
        except ValueError as e:
            raise MatrixOperationError(str(e))

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.cols != other.rows:
                raise MatrixOperationError("Invalid dimensions for matrix multiplication")
        try:
            return super().__mul__(other)
        except ValueError as e:
            raise MatrixOperationError(str(e))

class ModifiedPolinom(DictIntFloat, Polynom):
    def __setitem__(self, key, value):
        try:
            super().__setitem__(key, value)
        except IndexValueError as e:
            raise IndexValueError(f"Invalid polynomial coefficient: {e}")

class DictStrInt(dict):
    def __setitem__(self, key: str, value: int) -> None:
        if not isinstance(key, str):
            raise DictStrIntError("Key must be a string")
        if not isinstance(value, int):
            raise DictStrIntError("Value must be an integer")
        super().__setitem__(key, value)

class ModifiedStringDict(StringDict):
    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise StringDictError("Key must be a string")
        
        if any(ord(c) > 127 for c in key) and any(ord(c) <= 127 for c in key):
            raise StringDictError("Cannot mix Ukrainian and English letters in key")
            
        if isinstance(value, str):
            if any(ord(c) > 127 for c in value) and any(ord(c) <= 127 for c in value):
                raise StringDictError("Cannot mix Ukrainian and English letters in value")
            
            if any(ord(c) > 127 for c in key) != any(ord(c) > 127 for c in value):
                raise StringDictError("Key and value must be in the same language")
                
        super().__setitem__(key, value)

class SentenceError(ValueError):
    def __init__(self, message: str):
        super().__init__(message)

class ModifiedSentence(Sentence):
    def __setitem__(self, index, value):
        if not isinstance(value, str):
            raise SentenceError("Can only set string values")
        super().__setitem__(index, value)

    def __add__(self, other):
        if not isinstance(other, (Sentence, str)):
            raise SentenceError("Can only add Sentence or string")
        return super().__add__(other)

    def __sub__(self, other):
        if not isinstance(other, (Sentence, str)):
            raise SentenceError("Can only subtract Sentence or string")
        return super().__sub__(other)

    def add(self, word):
        if not isinstance(word, str):
            raise SentenceError("Can only add string words")
        return super().add(word)
