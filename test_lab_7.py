from main_lab_7 import *

def test_protected_dict_int():
    d = ModifiedProtectedDictInt()
    try:
        d[1.5] = 10
        assert False, "Should raise ProtectedDictIntError"
    except ProtectedDictIntError as e:
        print("ProtectedDictIntError test passed (invalid key type)")
    
    d[1] = 10
    try:
        d[1] = 20
        assert False, "Should raise ProtectedDictIntError"
    except ProtectedDictIntError as e:
        print("ProtectedDictIntError test passed (modify existing)")

def test_rational_error():
    try:
        r = ModifiedRational(1, 0)
        assert False, "Should raise RationalError"
    except RationalError as e:
        print("RationalError test passed")

def test_rational_value_error():
    r = ModifiedRational(1, 2)
    try:
        r + "invalid"
        assert False, "Should raise RationalValueError"
    except RationalValueError as e:
        print("RationalValueError test passed")

def test_rational_list():
    lst = ModifiedRationalList()
    try:
        lst.append("invalid")
        assert False, "Should raise RationalValueError"
    except RationalValueError as e:
        print("RationalValueError in list test passed")

def test_custom_list():
    lst = ModifiedCustomList()
    try:
        lst.append(1.5)
        assert False, "Should raise CustomListNotIntError"
    except CustomListNotIntError as e:
        print("CustomListNotIntError test passed")

def test_segment():
    try:
        s = ModifiedSegment(5, 1)
        assert False, "Should raise SegmentError"
    except SegmentError as e:
        print("SegmentError test passed")

def test_custom_set():
    s = ModifiedCustomSet()
    s.add(1)
    try:
        s.add("string")
        assert False, "Should raise CustomSetError"
    except CustomSetError as e:
        print("CustomSetError test passed (type mismatch)")
    
    s2 = ModifiedCustomSet()
    s2.add("string")
    try:
        s & s2
        assert False, "Should raise CustomSetError"
    except CustomSetError as e:
        print("CustomSetError test passed (operation type mismatch)")

def test_mutable_string():
    s = ModifiedMutableString("test")
    try:
        s[-1]
        assert False, "Should raise IndexPositiveError"
    except IndexPositiveError as e:
        print("IndexPositiveError test passed (get)")
    
    try:
        s[-1] = 'x'
        assert False, "Should raise IndexPositiveError"
    except IndexPositiveError as e:
        print("IndexPositiveError test passed (set)")

def test_matrix():
    # Create matrices with incompatible dimensions for addition
    m1 = ModifiedMatrix(2, 2, [[1, 2], [3, 4]])
    m2 = ModifiedMatrix(2, 3, [[1, 2, 3], [4, 5, 6]])
    try:
        m1 + m2
        assert False, "Should raise MatrixOperationError"
    except MatrixOperationError as e:
        print("MatrixOperationError test passed (addition)")
    
    # Create matrices with incompatible dimensions for multiplication
    m3 = ModifiedMatrix(2, 3, [[1, 2, 3], [4, 5, 6]])
    m4 = ModifiedMatrix(2, 2, [[1, 2], [3, 4]])
    try:
        m3 * m4
        assert False, "Should raise MatrixOperationError"
    except MatrixOperationError as e:
        print("MatrixOperationError test passed (multiplication)")

def test_dict_str_int():
    d = DictStrInt()
    try:
        d[123] = 456
        assert False, "Should raise DictStrIntError"
    except DictStrIntError as e:
        print("DictStrIntError test passed (invalid key)")
    
    try:
        d["key"] = "value"
        assert False, "Should raise DictStrIntError"
    except DictStrIntError as e:
        print("DictStrIntError test passed (invalid value)")

def test_string_dict():
    d = ModifiedStringDict()
    try:
        d["keyКлюч"] = "value"
        assert False, "Should raise StringDictError"
    except StringDictError as e:
        print("StringDictError test passed (mixed letters in key)")
    
    try:
        d["key"] = "valueЗначення"
        assert False, "Should raise StringDictError"
    except StringDictError as e:
        print("StringDictError test passed (mixed letters in value)")

def test_sentence():
    s = ModifiedSentence("Hello world")
    
    # Test setting non-string value
    try:
        s[0] = 123
        assert False, "Should raise SentenceError"
    except SentenceError as e:
        print("SentenceError test passed (non-string assignment)")
    
    # Test adding non-string/non-sentence value
    try:
        s + 123
        assert False, "Should raise SentenceError"
    except SentenceError as e:
        print("SentenceError test passed (invalid addition)")
    
    # Test subtracting non-string/non-sentence value
    try:
        s - 123
        assert False, "Should raise SentenceError"
    except SentenceError as e:
        print("SentenceError test passed (invalid subtraction)")
    
    # Test adding non-string word
    try:
        s.add(123)
        assert False, "Should raise SentenceError"
    except SentenceError as e:
        print("SentenceError test passed (invalid word addition)")

def run_all_tests():
    print("Running all tests...")
    test_protected_dict_int()
    test_rational_error()
    test_rational_value_error()
    test_rational_list()
    test_custom_list()
    test_segment()
    test_custom_set()
    test_mutable_string()
    test_matrix()
    test_dict_str_int()
    test_string_dict()
    test_sentence()
    print("\nAll tests completed!")

if __name__ == "__main__":
    run_all_tests() 