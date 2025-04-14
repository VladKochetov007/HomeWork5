from main_lab_6 import *
import unittest

class TestIterators(unittest.TestCase):
    
    def test_protected_dict_int_iterator(self):
        dict_int = ProtectedDictInt({5: 10, 2: 4, 8: 16, 1: 2})
        keys = list(dict_int)
        self.assertEqual(keys, [1, 2, 5, 8])
        
        # Test empty dict
        empty_dict = ProtectedDictInt()
        self.assertEqual(list(empty_dict), [])
    
    def test_rational_list_iterator(self):
        rationals = [
            Rational("1/2"), Rational("3/4"), Rational("1/4"),
            Rational("5/2"), Rational("3/2"), Rational("7/4")
        ]
        rational_list = RationalList(rationals)
        
        # Check descending order of denominators
        result = list(rational_list)
        for i in range(len(result) - 1):
            self.assertTrue(result[i].d >= result[i+1].d or 
                           (result[i].d == result[i+1].d and result[i].n >= result[i+1].n))
        
        # Test empty list
        empty_list = RationalList()
        self.assertEqual(list(empty_list), [])
    
    def test_custom_list_iterator(self):
        numbers = CustomList([1, 4, 2, 7, 3, 8, 5, 6])
        result = list(numbers)
        
        # Check odd numbers are ascending
        odd_numbers = [x for x in result if x % 2 == 1]
        self.assertEqual(odd_numbers, sorted(odd_numbers))
        
        # Check even numbers are descending
        even_numbers = [x for x in result if x % 2 == 0]
        self.assertEqual(even_numbers, sorted(even_numbers, reverse=True))
        
        # Test empty list
        empty_list = CustomList()
        self.assertEqual(list(empty_list), [])
    
    def test_segment_set_iterator(self):
        segments = SegmentSet([
            Segment(-1, 1),
            Segment(2, 4),
            Segment(-3, -2)
        ])
        
        result = list(segments)
        # Check ascending order of start points
        for i in range(len(result) - 1):
            self.assertTrue(result[i].start <= result[i+1].start or
                           (result[i].start == result[i+1].start and result[i].end <= result[i+1].end))
        
        # Test empty set
        empty_set = SegmentSet()
        self.assertEqual(list(empty_set), [])
    
    def test_custom_set_iterator(self):
        custom_set = CustomSet({3, 1, 4, 2, 5})
        result = list(custom_set)
        self.assertEqual(result, [1, 2, 3, 4, 5])
        
        # Test empty set
        empty_set = CustomSet()
        self.assertEqual(list(empty_set), [])
    
    def test_mutable_string_iterator(self):
        text = MutableString("Hello")
        result = list(text)
        self.assertEqual(result, ['H', 'e', 'l', 'l', 'o'])
        
        # Test empty string
        empty_string = MutableString("")
        self.assertEqual(list(empty_string), [])
    
    def test_matrix_iterator(self):
        matrix = Matrix(2, 2, [1, 2, 3, 4])
        result = list(matrix)
        self.assertEqual(result, [1, 2, 3, 4])
        
        # Test 3x3 matrix
        matrix3d = Matrix3D([1, 2, 3, 4, 5, 6, 7, 8, 9])
        result = list(matrix3d)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    
    def test_polynom_iterator(self):
        p = Polynom([1, -3, 0, 2])  # 2x^3 + 0x^2 - 3x + 1
        result = list(p)
        self.assertEqual(result, [1, -3, 0, 2])
        
        # Test empty polynomial
        empty_polynom = Polynom([])
        self.assertEqual(list(empty_polynom), [])
    
    def test_custom_set_mixed(self):
        mixed_set = CustomSetMixed([1, 3.14, "hello", 2, 2.71, "world", 3, 1.41, "python"])
        result = list(mixed_set)
        
        # Check integers are sorted ascending
        ints = [x for x in result if isinstance(x, int)]
        self.assertEqual(ints, sorted(ints))
        
        # Check floats are sorted descending
        floats = [x for x in result if isinstance(x, float)]
        self.assertEqual(floats, sorted(floats, reverse=True))
        
        # Check strings are sorted ascending
        strings = [x for x in result if isinstance(x, str)]
        self.assertEqual(strings, sorted(strings))
        
        # Check types are in correct order (int, float, str)
        type_order = []
        for item in result:
            if isinstance(item, int):
                type_order.append(0)
            elif isinstance(item, float):
                type_order.append(1)
            else:
                type_order.append(2)
        
        self.assertEqual(type_order, sorted(type_order))
        
        # Test empty set
        empty_set = CustomSetMixed()
        self.assertEqual(list(empty_set), [])
    
    def test_sentence_iterator(self):
        sentence = Sentence("The quick brown fox jumps over the lazy dog")
        result = list(sentence)
        self.assertEqual(result, sorted(["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]))
        
        # Test empty sentence
        empty_sentence = Sentence("")
        self.assertEqual(list(empty_sentence), [])
    
    def test_custom_dict_iterator(self):
        custom_dict = CustomDict()
        text = "the quick brown fox jumps over the lazy dog"
        for word in text.split():
            custom_dict[word] = len(word)
        
        # Check keys are sorted alphabetically
        result = list(custom_dict)
        self.assertEqual(result, sorted(set(text.split())))
        
        # Test empty dict
        empty_dict = CustomDict()
        self.assertEqual(list(empty_dict), [])
    
    def test_string_dict_iterator(self):
        string_dict = StringDict()
        translations = {
            "hello": ["привіт", "вітання"],
            "world": ["світ", "всесвіт"],
            "python": ["пітон", "пайтон"]
        }
        
        for eng, ukr_list in translations.items():
            string_dict[eng] = ukr_list
        
        # Check keys are sorted alphabetically
        result = list(string_dict)
        self.assertEqual(result, sorted(translations.keys()))
        
        # Test empty dict
        empty_dict = StringDict()
        self.assertEqual(list(empty_dict), [])

if __name__ == '__main__':
    unittest.main() 