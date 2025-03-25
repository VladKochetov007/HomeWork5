from src.protected_dict import ProtectedDictInt
from src.rational_list import RationalList
from src.rational import Rational
from src.custom_list import CustomList
from src.segment import Segment, SegmentSet
from src.custom_set import CustomSet
from src.mutable_string import MutableString
from src.matrix import Matrix2D, Matrix3D, Vector2D, Vector3D
from src.polynom import Polynom
from src.complex import Complex
from src.sentence import Sentence
from src.custom_dict import CustomDict
from src.string_dict import StringDict

def process_expression(expression: str) -> Rational:
    tokens = expression.split()
    rational_tokens = []
    for token in tokens:
        if token in {'+', '-', '*', '/'}:
            rational_tokens.append(token)
        else:
            rational_tokens.append(Rational(token))
    
    i = 1
    while i < len(rational_tokens) - 1:
        if rational_tokens[i] == '*':
            result = rational_tokens[i-1] * rational_tokens[i+1]
            rational_tokens[i-1:i+2] = [result]
        elif rational_tokens[i] == '/':
            result = rational_tokens[i-1] / rational_tokens[i+1]
            rational_tokens[i-1:i+2] = [result]
        else:
            i += 1
    
    result = rational_tokens[0]
    i = 1
    while i < len(rational_tokens) - 1:
        if rational_tokens[i] == '+':
            result += rational_tokens[i+1]
        elif rational_tokens[i] == '-':
            result -= rational_tokens[i+1]
        i += 2
    
    return result

def process_task1():
    with open('input01.txt', 'r') as file:
        expressions = file.readlines()
    
    results = []
    
    for expr in expressions:
        if expr.strip():
            result = process_expression(expr.strip())
            results.append(result)
            print(f"{expr.strip()} = {result}")
    
    return results

def process_task2():
    with open('input01.txt', 'r') as file:
        content = file.read()
    
    rationals = []
    for token in content.split():
        if token not in {'+', '-', '*', '/'}:
            try:
                rational = Rational(token)
                rationals.append(rational)
            except ValueError:
                pass
    
    rational_list = RationalList(rationals)
    total_sum = rational_list.sum()
    
    return rational_list, total_sum

def process_file_for_task2(filename):
    with open(filename, 'r') as file:
        content = file.read()
    
    rational_list = RationalList()
    for token in content.split():
        if token.strip():
            try:
                rational = Rational(token.strip())
                rational_list += rational
            except (ValueError, ZeroDivisionError):
                pass
    
    return rational_list

def test_task_531():
    print("Завдання 5.3.1 - Операції з раціональними числами")
    results = process_task1()
    
    results_dict = ProtectedDictInt()
    for i, result in enumerate(results):
        results_dict[i] = result
    
    print("\nРезультати у ProtectedDict:")
    print(results_dict)
    
    print("\nСума всіх раціональних чисел:")
    rational_list, total_sum = process_task2()
    
    print(f"Всі раціональні числа у списку: {rational_list}")
    print(f"Сума: {total_sum}")

def test_task_532():
    print("Завдання 5.3.2 - Обробка файлів з раціональними числами")
    
    print("\nОбробка файлу input01.txt:")
    rational_list1 = process_file_for_task2('input01.txt')
    sum1 = rational_list1.sum()
    print(f"Кількість чисел: {len(rational_list1)}")
    print(f"Сума чисел: {sum1}")
    
    print("\nОбробка файлу input02.txt:")
    rational_list2 = process_file_for_task2('input02.txt')
    sum2 = rational_list2.sum()
    print(f"Кількість чисел: {len(rational_list2)}")
    print(f"Сума чисел: {sum2}")
    
    print("\nОбробка файлу input03.txt:")
    rational_list3 = process_file_for_task2('input03.txt')
    sum3 = rational_list3.sum()
    print(f"Кількість чисел: {len(rational_list3)}")
    print(f"Сума чисел: {sum3}")
    
    combined_list = rational_list1 + rational_list2 + rational_list3
    combined_sum = combined_list.sum()
    print("\nОб'єднаний список:")
    print(f"Кількість чисел: {len(combined_list)}")
    print(f"Сума всіх чисел: {combined_sum}")

def test_task_541():
    print("Завдання 5.4.1 - CustomList")
    
    text = "Це текст із числами: 1, 3, 1984, 7777, 0, 42, -10, 123, 0, 1, 3"
    
    custom_list = CustomList()
    for word in text.split():
        word = word.strip(',.;:!?')
        try:
            num = int(word)
            custom_list += num
        except ValueError:
            pass
    
    print(f"Знайдені числа: {custom_list}")
    print(f"Кількість чисел: {len(custom_list)}")
    print(f"Сума чисел: {custom_list.sum()}")
    
    print(f"Чи містяться числа 1, 3, 1984, 7777 в тексті?")
    for num in [1, 3, 1984, 7777]:
        print(f"{num}: {num in custom_list}")
    
    print(f"Кількість ненульових чисел: {custom_list.count_non_zero()}")

def test_task_542():
    print("Завдання 5.4.2 - Segment і SegmentSet")
    
    print("Розв'язання системи квадратних нерівностей:")
    
    inequalities = [
        (1, -3, 2, ">="),    # x^2 - 3x + 2 >= 0
        (1, -4, 3, ">"),     # x^2 - 4x + 3 > 0
        (1, 2, -3, ">="),    # x^2 + 2x - 3 >= 0
    ]
    
    solution_set = SegmentSet()
    
    for a, b, c, sign in inequalities:
        print(f"{a}x^2 + {b}x + {c} {sign} 0")
        
        discriminant = b*b - 4*a*c
        
        if discriminant < 0:
            if a > 0:
                if sign in [">", ">="]:
                    interval = SegmentSet(Segment(-float('inf'), float('inf')))
                else:
                    interval = SegmentSet()
            else:
                if sign in [">", ">="]:
                    interval = SegmentSet()
                else:
                    interval = SegmentSet(Segment(-float('inf'), float('inf')))
        else:
            x1 = (-b - discriminant**0.5) / (2*a)
            x2 = (-b + discriminant**0.5) / (2*a)
            
            if x1 > x2:
                x1, x2 = x2, x1
            
            if a > 0:
                if sign == ">":
                    interval = SegmentSet([
                        Segment(-float('inf'), x1, True, False),
                        Segment(x2, float('inf'), False, True)
                    ])
                elif sign == ">=":
                    interval = SegmentSet([
                        Segment(-float('inf'), x1, True, True),
                        Segment(x2, float('inf'), True, True)
                    ])
                elif sign == "<":
                    interval = SegmentSet(Segment(x1, x2, False, False))
                else:  # <=
                    interval = SegmentSet(Segment(x1, x2, True, True))
            else:  # a < 0
                if sign == ">":
                    interval = SegmentSet(Segment(x1, x2, False, False))
                elif sign == ">=":
                    interval = SegmentSet(Segment(x1, x2, True, True))
                elif sign == "<":
                    interval = SegmentSet([
                        Segment(-float('inf'), x1, True, False),
                        Segment(x2, float('inf'), False, True)
                    ])
                else:  # <=
                    interval = SegmentSet([
                        Segment(-float('inf'), x1, True, True),
                        Segment(x2, float('inf'), True, True)
                    ])
        
        print(f"Розв'язок: {interval}")
        
        if solution_set.segments:
            solution_set = solution_set * interval
        else:
            solution_set = interval
    
    print(f"Розв'язок системи: {solution_set}")

def test_task_543():
    print("Завдання 5.4.3 - CustomSet")
    
    text_file1 = "This is the first file with some words. This file has some unique words."
    text_file2 = "This is the second file with different words. Some words are the same."
    text_file3 = "The third file has completely different content."
    
    files = [text_file1, text_file2, text_file3]
    
    sets = []
    for file_content in files:
        words = set(word.lower().strip(',.;:!?') for word in file_content.split())
        sets.append(CustomSet(words))
    
    all_words = sets[0]
    for word_set in sets[1:]:
        all_words = all_words * word_set
    
    any_words = sets[0]
    for word_set in sets[1:]:
        any_words = any_words + word_set
    
    only_first = sets[0]
    for word_set in sets[1:]:
        only_first = only_first - word_set
    
    print(f"Слова, що містяться в усіх файлах ({len(all_words)}): {all_words}")
    print(f"Слова, що містяться принаймні в одному файлі ({len(any_words)}): {any_words}")
    print(f"Слова, що містяться лише в першому файлі ({len(only_first)}): {only_first}")

def test_task_544():
    print("Завдання 5.4.4 - MutableString")
    
    text = "Це текст з англiйськими символами замiсть украiнських. Тут є росiйське 'р' та латинське 'i'."
    
    mutable_text = MutableString(text)
    print(f"Оригінальний текст: {mutable_text}")
    
    replacements = {
        'i': 'і',
        'р': 'р',
        'с': 'с',
        'е': 'е',
        'о': 'о',
        'а': 'а'
    }
    
    for eng, ukr in replacements.items():
        for i in range(len(mutable_text)):
            if mutable_text[i] == eng:
                mutable_text[i] = ukr
    
    print(f"Виправлений текст: {mutable_text}")
    print(f"Довжина виправленого тексту: {len(mutable_text)}")

def test_task_545():
    print("Завдання 5.4.5 - Matrix і Vector")
    
    print("Розв'язання СЛАР методом Гауса:")
    
    a = Matrix3D([3, 2, -1, 2, -2, 4, -1, 0.5, -1])
    b = Vector3D([1, -2, 0])
    
    print(f"Матриця A:\n{a}")
    print(f"Вектор b: {b}")
    
    augmented = Matrix3D([
        [a[0, 0], a[0, 1], a[0, 2], b[0]],
        [a[1, 0], a[1, 1], a[1, 2], b[1]],
        [a[2, 0], a[2, 1], a[2, 2], b[2]]
    ])
    
    n = 3
    for i in range(n):
        for j in range(i+1, n):
            factor = augmented[j, i] / augmented[i, i]
            for k in range(i, n+1):
                augmented[j, k] -= factor * augmented[i, k]
    
    x = [0] * n
    for i in range(n-1, -1, -1):
        x[i] = augmented[i, n]
        for j in range(i+1, n):
            x[i] -= augmented[i, j] * x[j]
        x[i] /= augmented[i, i]
    
    print(f"Розв'язок СЛАР: x = {x}")
    
    det_a = a()
    print(f"Визначник матриці A: {det_a}")
    
    print("Перевірка розв'язку:")
    res = a * Vector3D(x)
    print(f"A * x = {res}")
    print(f"b = {b}")

def test_task_546():
    print("Завдання 5.4.6 - Polynom")
    
    p1 = Polynom([1, -5, 6])  # x^2 - 5x + 6
    p2 = Polynom([2, 1])     # 2 + x
    
    print(f"Поліном 1: {p1}")
    print(f"Поліном 2: {p2}")
    
    print(f"p1 + p2 = {p1 + p2}")
    print(f"p1 - p2 = {p1 - p2}")
    print(f"p1 * p2 = {p1 * p2}")
    
    x = 2
    print(f"p1({x}) = {p1(x)}")
    print(f"p2({x}) = {p2(x)}")
    
    p1[1] = 3
    print(f"Після зміни коефіцієнта при x в p1: {p1}")
    
    derivative = p1.derivative()
    print(f"Похідна p1: {derivative}")
    
    integral = p1.integral()
    print(f"Первісна p1: {integral}")

def test_task_547():
    print("Завдання 5.4.7 - Complex")
    
    a = Complex(1, 2)
    b = Complex(3, 4)
    
    print(f"a = {a}")
    print(f"b = {b}")
    
    print(f"a + b = {a + b}")
    print(f"a - b = {a - b}")
    print(f"a * b = {a * b}")
    print(f"a / b = {a / b}")
    
    print(f"|a| = {a.abs()}")
    print(f"a^2 = {a ** 2}")
    print(f"a^0.5 = {a ** 0.5}")
    
    print("Розв'язання квадратного рівняння a*x^2 + b*x + c = 0:")
    
    def solve_quadratic(a, b, c):
        if a == 0:
            if b == 0:
                return "Рівняння не має коренів" if c != 0 else "Рівняння має нескінченно багато розв'язків"
            return f"x = {-c / b}"
        
        discriminant = b*b - 4*a*c
        if isinstance(discriminant, Complex) or discriminant >= 0:
            x1 = (-b + discriminant ** 0.5) / (2 * a)
            x2 = (-b - discriminant ** 0.5) / (2 * a)
            return f"x1 = {x1}, x2 = {x2}"
        else:
            discriminant = Complex(0, abs(discriminant) ** 0.5)
            x1 = (-b + discriminant) / (2 * a)
            x2 = (-b - discriminant) / (2 * a)
            return f"x1 = {x1}, x2 = {x2}"
    
    a_real = 1
    b_real = -3
    c_real = 2
    print(f"Рівняння з дійсними коефіцієнтами: {a_real}x^2 + {b_real}x + {c_real} = 0")
    print(f"Розв'язок: {solve_quadratic(a_real, b_real, c_real)}")
    
    a_complex = Complex(1, 0)
    b_complex = Complex(0, 2)
    c_complex = Complex(1, 0)
    print(f"Рівняння з комплексними коефіцієнтами: {a_complex}x^2 + {b_complex}x + {c_complex} = 0")
    print(f"Розв'язок: {solve_quadratic(a_complex, b_complex, c_complex)}")

def test_task_548():
    print("Завдання 5.4.8 - Sentence")
    
    text = "Це речення містить кілька слів які треба замінити. Це речення також містить слова які треба видалити."
    
    sentences = []
    for line in text.split("."):
        if line.strip():
            sentences.append(Sentence(line.strip()))
    
    print("Оригінальний текст:")
    for sentence in sentences:
        print(f"- {sentence}")
    
    words_to_replace = {"речення": "твердження", "слів": "лексем", "кілька": "декілька"}
    words_to_delete = ["які", "також"]
    
    print("\nТекст після заміни слів:")
    total_words = 0
    for i, sentence in enumerate(sentences):
        for old_word, new_word in words_to_replace.items():
            sentences[i] = sentence.replace(old_word, new_word)
        print(f"- {sentences[i]}")
    
    print("\nТекст після видалення слів:")
    for i, sentence in enumerate(sentences):
        for word in words_to_delete:
            sentences[i] = sentences[i] - word
        print(f"- {sentences[i]}")
        total_words += len(sentences[i])
    
    print(f"\nЗагальна кількість слів у відкоригованому тексті: {total_words}")

def test_task_549():
    print("Завдання 5.4.9 - CustomDict")
    
    text = "Це текст містить багато слів. Деякі слова повторюються. Слова мають різну довжину. Різні слова мають різну частоту."
    
    word_dict = CustomDict()
    
    words = text.lower().split()
    cleaned_words = []
    for word in words:
        word = word.strip(',.;:!?')
        if word:
            cleaned_words.append(word)
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
    
    print(f"Словник слів та їхніх частот: {word_dict}")
    
    word_to_check = "слова"
    print(f"Перевірка слова '{word_to_check}': {word_to_check in word_dict}, кількість разів: {word_dict[word_to_check]}")
    
    most_common = word_dict.most_common(1)
    print(f"Слово, що зустрічається найчастіше: {most_common[0][0]} ({most_common[0][1]} разів)")
    
    count_to_find = 2
    words_with_count = word_dict.words_with_count(count_to_find)
    print(f"Слова, що зустрічаються {count_to_find} рази: {words_with_count}")
    
    longest_word = word_dict.longest_word()
    shortest_word = word_dict.shortest_word()
    print(f"Найдовше слово: {longest_word} ({len(longest_word)} символів)")
    print(f"Найкоротше слово: {shortest_word} ({len(shortest_word)} символів)")
    
    print(f"Кількість різних слів у тексті: {len(word_dict)}")

def test_task_5410():
    print("Завдання 5.4.10 - StringDict")
    
    eng_words = "mystery mystery cat mystery cat apple"
    ukr_words = "таємниця загадка кіт таїнство кішка яблуко"
    
    eng_list = eng_words.split()
    ukr_list = ukr_words.split()
    
    # Створення англо-українського словника
    eng_ukr_dict = StringDict()
    for i in range(min(len(eng_list), len(ukr_list))):
        eng = eng_list[i]
        ukr = ukr_list[i]
        if eng in eng_ukr_dict:
            if ukr not in eng_ukr_dict[eng]:
                eng_ukr_dict[eng].append(ukr)
        else:
            eng_ukr_dict[eng] = [ukr]
    
    print("Англо-український словник:")
    for eng, ukr_list in eng_ukr_dict.items():
        print(f"{eng}: {', '.join(ukr_list)}")
    
    # Створення україно-англійського словника
    ukr_eng_dict = eng_ukr_dict.create_reverse_dict()
    
    print("\nУкраїно-англійський словник:")
    for ukr, eng_list in ukr_eng_dict.items():
        print(f"{ukr}: {', '.join(eng_list)}")
    
    # Знаходження перекладів для заданого слова
    word_to_translate = "mystery"
    translations = eng_ukr_dict.get_translations(word_to_translate)
    print(f"\nПереклади для слова '{word_to_translate}': {', '.join(translations)}")
    
    # Слово з найбільшою кількістю перекладів
    word_most_translations = eng_ukr_dict.word_with_most_translations()
    print(f"Слово з найбільшою кількістю перекладів: {word_most_translations} ({len(eng_ukr_dict[word_most_translations])} перекладів)")
    
    # Англійські слова з лише одним перекладом
    single_translation_words = eng_ukr_dict.words_with_single_translation()
    print(f"Англійські слова з одним перекладом: {', '.join(single_translation_words)}")
    
    # Кількість різних слів
    print(f"Кількість різних англійських слів: {eng_ukr_dict.count_unique_words()}")
    print(f"Кількість різних українських слів: {eng_ukr_dict.count_unique_translations()}")

def main():
    tasks = {
        "1": test_task_531,
        "2": test_task_532,
        "3": test_task_541,
        "4": test_task_542,
        "5": test_task_543,
        "6": test_task_544,
        "7": test_task_545,
        "8": test_task_546,
        "9": test_task_547,
        "10": test_task_548,
        "11": test_task_549,
        "12": test_task_5410
    }
    
    print("Доступні завдання:")
    print("1. Завдання 5.3.1 - Операції з раціональними числами")
    print("2. Завдання 5.3.2 - Обробка файлів з раціональними числами")
    print("3. Завдання 5.4.1 - CustomList")
    print("4. Завдання 5.4.2 - Segment і SegmentSet")
    print("5. Завдання 5.4.3 - CustomSet")
    print("6. Завдання 5.4.4 - MutableString")
    print("7. Завдання 5.4.5 - Matrix і Vector")
    print("8. Завдання 5.4.6 - Polynom")
    print("9. Завдання 5.4.7 - Complex")
    print("10. Завдання 5.4.8 - Sentence")
    print("11. Завдання 5.4.9 - CustomDict")
    print("12. Завдання 5.4.10 - StringDict")
    
    choice = input("Виберіть номер завдання (1-12): ")
    
    if choice in tasks:
        tasks[choice]()
    else:
        print("Некоректний вибір завдання")

if __name__ == "__main__":
    main()
