from src.protected_dict import ProtectedDictInt
from src.rational_list import RationalList
from src.rational import Rational
from src.custom_list import CustomList
from src.segment import Segment, SegmentSet
from src.custom_set import CustomSet
from src.mutable_string import MutableString
from src.matrix import Matrix, Matrix3D
from src.polynom import Polynom
from src.sentence import Sentence
from src.custom_dict import CustomDict
from src.string_dict import StringDict
from typing import Iterator, List, Union, Any
from dataclasses import dataclass


class ProtectedDictIntIterator:    
    def __init__(self, protected_dict: ProtectedDictInt):
        self._keys = sorted(protected_dict.keys())
        self._index = 0
    
    def __iter__(self) -> Iterator[int]:
        return self
    
    def __next__(self) -> int:
        if self._index >= len(self._keys):
            raise StopIteration
        key = self._keys[self._index]
        self._index += 1
        return key


ProtectedDictInt.__iter__ = lambda self: ProtectedDictIntIterator(self)


class RationalListIterator:    
    def __init__(self, rational_list: RationalList):
        self._rationals = sorted(
            rational_list._items,
            key=lambda x: (-x.d, -x.n)
        )
        self._index = 0
    
    def __iter__(self) -> Iterator[Rational]:
        return self
    
    def __next__(self) -> Rational:
        if self._index >= len(self._rationals):
            raise StopIteration
        rational = self._rationals[self._index]
        self._index += 1
        return rational


RationalList.__iter__ = lambda self: RationalListIterator(self)


class CustomListIterator:    
    def __init__(self, custom_list: CustomList):
        self._odd = sorted(x for x in custom_list._items if x % 2)
        self._even = sorted((x for x in custom_list._items if not x % 2), reverse=True)
        self._index = 0
        self._is_odd = True
    
    def __iter__(self) -> Iterator[int]:
        return self
    
    def __next__(self) -> int:
        if self._is_odd:
            if self._index < len(self._odd):
                value = self._odd[self._index]
                self._index += 1
                return value
            self._is_odd = False
            self._index = 0
        
        if self._index < len(self._even):
            value = self._even[self._index]
            self._index += 1
            return value
        
        raise StopIteration


CustomList.__iter__ = lambda self: CustomListIterator(self)


class SegmentSetIterator:    
    def __init__(self, segment_set: SegmentSet):
        self._segments = sorted(segment_set.segments, key=lambda s: (s.start, s.end))
        self._index = 0
    
    def __iter__(self) -> Iterator[Segment]:
        return self
    
    def __next__(self) -> Segment:
        if self._index >= len(self._segments):
            raise StopIteration
        segment = self._segments[self._index]
        self._index += 1
        return segment


SegmentSet.__iter__ = lambda self: SegmentSetIterator(self)


class CustomSetIterator:    
    def __init__(self, custom_set: CustomSet):
        self._elements = sorted(custom_set._elements)
        self._index = 0
    
    def __iter__(self) -> Iterator[Any]:
        return self
    
    def __next__(self) -> Any:
        if self._index >= len(self._elements):
            raise StopIteration
        element = self._elements[self._index]
        self._index += 1
        return element


class MutableStringIterator:    
    def __init__(self, mutable_string: MutableString):
        self._string = str(mutable_string)
        self._index = 0
    
    def __iter__(self) -> Iterator[str]:
        return self
    
    def __next__(self) -> str:
        if self._index >= len(self._string):
            raise StopIteration
        char = self._string[self._index]
        self._index += 1
        return char


MutableString.__iter__ = lambda self: MutableStringIterator(self)


class MatrixIterator:    
    def __init__(self, matrix: Matrix):
        self._matrix = matrix
        self._row = 0
        self._col = 0
    
    def __iter__(self) -> Iterator[Union[int, float]]:
        return self
    
    def __next__(self) -> Union[int, float]:
        if self._row >= self._matrix.rows:
            raise StopIteration
        
        value = self._matrix[self._row, self._col]
        self._col += 1
        
        if self._col >= self._matrix.cols:
            self._col = 0
            self._row += 1
        
        return value


Matrix.__iter__ = lambda self: MatrixIterator(self)


class PolynomIterator:    
    def __init__(self, polynom: Polynom):
        self._coefficients = polynom.coefficients
        self._index = 0
    
    def __iter__(self) -> Iterator[Union[int, float]]:
        return self
    
    def __next__(self) -> Union[int, float]:
        if self._index >= len(self._coefficients):
            raise StopIteration
        coef = self._coefficients[self._index]
        self._index += 1
        return coef


Polynom.__iter__ = lambda self: PolynomIterator(self)


@dataclass
class MixedElement:
    value: Any
    type_priority: int
    
    def __lt__(self, other: 'MixedElement') -> bool:
        if self.type_priority != other.type_priority:
            return self.type_priority < other.type_priority
        if self.type_priority == 0:  # int
            return self.value < other.value
        if self.type_priority == 1:  # float
            return self.value > other.value
        return self.value < other.value  # str


class CustomSetMixed:
    
    def __init__(self, elements: List[Union[int, float, str]] = None):
        self.elements = set(elements or [])
    
    def add(self, element: Union[int, float, str]) -> None:
        if not isinstance(element, (int, float, str)):
            raise TypeError("Element must be int, float or str")
        self.elements.add(element)
    
    def __iter__(self) -> Iterator[Union[int, float, str]]:
        def get_priority(x: Any) -> int:
            if isinstance(x, int):
                return 0
            if isinstance(x, float):
                return 1
            return 2
        
        sorted_elements = sorted(
            (MixedElement(x, get_priority(x)) for x in self.elements)
        )
        return iter(element.value for element in sorted_elements)


class SentenceIterator:    
    def __init__(self, sentence: Sentence):
        self._words = sorted(str(sentence).split())
        self._index = 0
    
    def __iter__(self) -> Iterator[str]:
        return self
    
    def __next__(self) -> str:
        if self._index >= len(self._words):
            raise StopIteration
        word = self._words[self._index]
        self._index += 1
        return word


Sentence.__iter__ = lambda self: SentenceIterator(self)


class CustomDictIterator:    
    def __init__(self, custom_dict: CustomDict):
        self._keys = sorted(custom_dict.keys())
        self._index = 0
    
    def __iter__(self) -> Iterator[str]:
        return self
    
    def __next__(self) -> str:
        if self._index >= len(self._keys):
            raise StopIteration
        key = self._keys[self._index]
        self._index += 1
        return key


CustomDict.__iter__ = lambda self: CustomDictIterator(self)


class StringDictIterator:    
    def __init__(self, string_dict: StringDict):
        self._keys = sorted(string_dict.keys())
        self._index = 0
    
    def __iter__(self) -> Iterator[str]:
        return self
    
    def __next__(self) -> str:
        if self._index >= len(self._keys):
            raise StopIteration
        key = self._keys[self._index]
        self._index += 1
        return key


StringDict.__iter__ = lambda self: StringDictIterator(self)


def test_task_621() -> None:
    print("Task 6.2.1 - ProtectedDictInt Iterator")
    dict_int = ProtectedDictInt({5: 10, 2: 4, 8: 16, 1: 2})
    print("Keys in ascending order:")
    for key in dict_int:
        print(f"{key}: {dict_int[key]}")


def test_task_631() -> None:
    print("\nTask 6.3.1 - RationalList Iterator")
    rationals = [
        Rational("1/2"), Rational("3/4"), Rational("1/4"),
        Rational("5/2"), Rational("3/2"), Rational("7/4")
    ]
    rational_list = RationalList(rationals)
    print("Rationals in descending order of denominators:")
    for rational in rational_list:
        print(rational)


def test_task_641() -> None:
    print("\nTask 6.4.1 - CustomList Iterator")
    numbers = CustomList([1, 4, 2, 7, 3, 8, 5, 6])
    print("Numbers in specified order (odd ascending, even descending):")
    for num in numbers:
        print(num)


def test_task_642() -> None:
    print("\nTask 6.4.2 - SegmentSet Iterator")
    segments = SegmentSet([
        Segment(-1, 1),
        Segment(2, 4),
        Segment(-3, -2)
    ])
    print("Segments in order of position on real axis:")
    for segment in segments:
        print(segment)


def test_task_643() -> None:
    print("\nTask 6.4.3 - CustomSet Iterator")
    custom_set = CustomSet({3, 1, 4, 2, 5})
    print("Elements in ascending order:")
    for element in custom_set:
        print(element)


def test_task_644() -> None:
    print("\nTask 6.4.4 - MutableString Iterator")
    text = MutableString("Hello, World!")
    print("Characters one by one:")
    for char in text:
        print(char)


def test_task_645() -> None:
    print("\nTask 6.4.5 - Matrix Iterator")
    matrix = Matrix3D([1, -2, 3, 4, -5, 6, 7, -8, 9])
    
    min_element = float('inf')
    max_element = float('-inf')
    sum_elements = 0
    count = 0
    
    for element in matrix:
        min_element = min(min_element, element)
        max_element = max(max_element, element)
        sum_elements += element
        count += 1
    
    print(f"Matrix:\n{matrix}")
    print(f"Minimum element: {min_element}")
    print(f"Maximum element: {max_element}")
    print(f"Sum of elements: {sum_elements}")
    print(f"Average: {sum_elements / count}")


def test_task_646() -> None:
    print("\nTask 6.4.6 - Polynom Iterator")
    p = Polynom([1, -3, 0, 2])  # 2x^3 + 0x^2 - 3x + 1
    
    print("Coefficients in ascending order of degrees:")
    for i, coef in enumerate(p):
        print(f"Coefficient at x^{i}: {coef}")
    
    coefficients = list(p)
    min_coef = min(coefficients)
    max_coef = max(coefficients)
    
    max_ratio = max((abs(coef) / (i + 1) if i else abs(coef))
                    for i, coef in enumerate(coefficients))
    
    print(f"Minimum coefficient: {min_coef}")
    print(f"Maximum coefficient: {max_coef}")
    print(f"Maximum coefficient to degree ratio: {max_ratio}")


def test_task_647() -> None:
    print("\nTask 6.4.7 - CustomSetMixed")
    mixed_set = CustomSetMixed([1, 3.14, "hello", 2, 2.71, "world", 3, 1.41, "python"])
    print("Elements in specified order:")
    for element in mixed_set:
        print(element)


def test_task_648() -> None:
    print("\nTask 6.4.8 - Sentence Iterator")
    sentence = Sentence("The quick brown fox jumps over the lazy dog")
    print("Words in lexicographical order:")
    for word in sentence:
        print(word)


def test_task_649() -> None:
    print("\nTask 6.4.9 - CustomDict Iterator")
    custom_dict = CustomDict()
    text = "the quick brown fox jumps over the lazy dog"
    for word in text.split():
        custom_dict[word] = len(word)
    
    print("Words in lexicographical order:")
    for word in custom_dict:
        print(f"{word}: {custom_dict[word]}")


def test_task_6410() -> None:
    print("\nTask 6.4.10 - StringDict Iterator")
    string_dict = StringDict()
    translations = {
        "hello": ["привіт", "вітання"],
        "world": ["світ", "всесвіт"],
        "python": ["пітон", "пайтон"]
    }
    
    for eng, ukr_list in translations.items():
        string_dict[eng] = ukr_list
    
    print("Words and translations in lexicographical order:")
    for word in string_dict:
        print(f"{word}: {', '.join(string_dict[word])}")


def main() -> None:
    tasks = {
        "1": (test_task_621, "Task 6.2.1 - ProtectedDictInt Iterator"),
        "2": (test_task_631, "Task 6.3.1 - RationalList Iterator"),
        "3": (test_task_641, "Task 6.4.1 - CustomList Iterator"),
        "4": (test_task_642, "Task 6.4.2 - SegmentSet Iterator"),
        "5": (test_task_643, "Task 6.4.3 - CustomSet Iterator"),
        "6": (test_task_644, "Task 6.4.4 - MutableString Iterator"),
        "7": (test_task_645, "Task 6.4.5 - Matrix Iterator"),
        "8": (test_task_646, "Task 6.4.6 - Polynom Iterator"),
        "9": (test_task_647, "Task 6.4.7 - CustomSetMixed"),
        "10": (test_task_648, "Task 6.4.8 - Sentence Iterator"),
        "11": (test_task_649, "Task 6.4.9 - CustomDict Iterator"),
        "12": (test_task_6410, "Task 6.4.10 - StringDict Iterator")
    }
    
    print("Available tasks:")
    for key, (_, description) in tasks.items():
        print(f"{key}. {description}")
    
    choice = input("Choose task number (1-12) or press Enter to run all: ")
    if not choice:
        for task_func, _ in tasks.values():
            task_func()
    elif choice in tasks:
        tasks[choice][0]()
    else:
        print("Invalid task number")


if __name__ == "__main__":
    main()
