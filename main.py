from src.protected_dict import ProtectedDictInt
from src.rational_list import RationalList
from src.rational import Rational
from src.custom_list import CustomList
from src.segment import Segment, SegmentSet
from src.custom_set import CustomSet
from src.mutable_string import MutableString
from src.matrix import Matrix3D, Vector3D
from src.polynom import Polynom
from src.complex import Complex
from src.sentence import Sentence
from src.custom_dict import CustomDict
from src.string_dict import StringDict
from typing import List, Union, Sequence

def process_expression(expression: str) -> Rational:
    tokens = expression.split()
    rational_tokens = [Rational(token) if token not in {'+', '-', '*', '/'} else token for token in tokens]
    
    for op in ['*', '/']:
        i = 1
        while i < len(rational_tokens) - 1:
            if rational_tokens[i] == op:
                result = rational_tokens[i-1] * rational_tokens[i+1] if op == '*' else rational_tokens[i-1] / rational_tokens[i+1]
                rational_tokens[i-1:i+2] = [result]
            else:
                i += 1
    
    result = rational_tokens[0]
    for i in range(1, len(rational_tokens) - 1, 2):
        result = result + rational_tokens[i+1] if rational_tokens[i] == '+' else result - rational_tokens[i+1]
    
    return result

def process_task1() -> List[Rational]:
    with open('input01.txt', 'r') as file:
        expressions = [expr.strip() for expr in file.readlines() if expr.strip()]
    
    results = [process_expression(expr) for expr in expressions]
    for expr, result in zip(expressions, results):
        print(f"{expr} = {result}")
    
    return results

def process_task2() -> tuple[RationalList, Rational]:
    with open('input01.txt', 'r') as file:
        content = file.read()
    
    rationals = [Rational(token) for token in content.split() 
                if token not in {'+', '-', '*', '/'} and token.strip()]
    
    rational_list = RationalList(rationals)
    return rational_list, rational_list.sum()

def process_file_for_task2(filename: str) -> RationalList:
    with open(filename, 'r') as file:
        content = file.read()
    
    rational_list = RationalList()
    for token in content.split():
        try:
            rational_list += Rational(token.strip())
        except (ValueError, ZeroDivisionError):
            continue
    
    return rational_list

def test_task_531() -> None:
    print("Завдання 5.3.1 - Операції з раціональними числами")
    results = process_task1()
    
    results_dict = ProtectedDictInt({i: result for i, result in enumerate(results)})
    print("\nРезультати у ProtectedDict:")
    print(results_dict)
    
    print("\nСума всіх раціональних чисел:")
    rational_list, total_sum = process_task2()
    print(f"Всі раціональні числа у списку: {rational_list}")
    print(f"Сума: {total_sum}")

def test_task_532() -> None:
    print("Завдання 5.3.2 - Обробка файлів з раціональними числами")
    
    files = ['input01.txt', 'input02.txt', 'input03.txt']
    lists = [process_file_for_task2(f) for f in files]
    
    for file, lst in zip(files, lists):
        print(f"\nОбробка файлу {file}:")
        print(f"Кількість чисел: {len(lst)}")
        print(f"Сума чисел: {lst.sum()}")
    
    combined_list = sum(lists[1:], lists[0])
    print("\nОб'єднаний список:")
    print(f"Кількість чисел: {len(combined_list)}")
    print(f"Сума всіх чисел: {combined_list.sum()}")

def test_task_541() -> None:
    print("Завдання 5.4.1 - CustomList")
    text = "Це текст із числами: 1, 3, 1984, 7777, 0, 42, -10, 123, 0, 1, 3"
    
    custom_list = CustomList()
    for word in text.split():
        try:
            custom_list += int(word.strip(',.;:!?'))
        except ValueError:
            continue
    
    print(f"Знайдені числа: {custom_list}")
    print(f"Кількість чисел: {len(custom_list)}")
    print(f"Сума чисел: {custom_list.sum()}")
    
    test_numbers = [1, 3, 1984, 7777]
    print(f"Чи містяться числа {', '.join(map(str, test_numbers))} в тексті?")
    for num in test_numbers:
        print(f"{num}: {num in custom_list}")
    
    print(f"Кількість ненульових чисел: {custom_list.count_non_zero()}")

def test_task_542() -> None:
    print("Завдання 5.4.2 - Segment і SegmentSet")
    
    inequalities = [
        (1, -3, 2, ">="),
        (1, -4, 3, ">"),
        (1, 2, -3, ">="),
    ]
    
    solution_set = SegmentSet()
    
    for a, b, c, sign in inequalities:
        print(f"{a}x^2 + {b}x + {c} {sign} 0")
        discriminant = b*b - 4*a*c
        
        if discriminant < 0:
            interval = SegmentSet(Segment(-float('inf'), float('inf'))) if (a > 0) == (sign in [">", ">="]) else SegmentSet()
        else:
            x1, x2 = sorted([(-b - discriminant**0.5) / (2*a), (-b + discriminant**0.5) / (2*a)])
            
            if a > 0:
                if sign in [">", ">="]:
                    interval = SegmentSet([
                        Segment(-float('inf'), x1, True, sign == ">="),
                        Segment(x2, float('inf'), sign == ">=", True)
                    ])
                else:
                    interval = SegmentSet(Segment(x1, x2, sign == "<=", sign == "<="))
            else:
                if sign in [">", ">="]:
                    interval = SegmentSet(Segment(x1, x2, sign == ">=", sign == ">="))
                else:
                    interval = SegmentSet([
                        Segment(-float('inf'), x1, True, sign == "<="),
                        Segment(x2, float('inf'), sign == "<=", True)
                    ])
        
        print(f"Розв'язок: {interval}")
        solution_set = interval if not solution_set.segments else solution_set * interval
    
    print(f"Розв'язок системи: {solution_set}")

def test_task_543() -> None:
    print("Завдання 5.4.3 - CustomSet")
    
    texts = [
        "This is the first file with some words. This file has some unique words.",
        "This is the second file with different words. Some words are the same.",
        "The third file has completely different content."
    ]
    
    sets = [CustomSet(word.lower().strip(',.;:!?') for word in text.split()) for text in texts]
    
    all_words = sets[0].intersection(*sets[1:])
    any_words = sets[0].union(*sets[1:])
    only_first = sets[0].difference(*sets[1:])
    
    print(f"Слова, що містяться в усіх файлах ({len(all_words)}): {all_words}")
    print(f"Слова, що містяться принаймні в одному файлі ({len(any_words)}): {any_words}")
    print(f"Слова, що містяться лише в першому файлі ({len(only_first)}): {only_first}")

def test_task_544() -> None:
    print("Завдання 5.4.4 - MutableString")
    
    text = "Це текст з англiйськими символами замiсть украiнських. Тут є росiйське 'р' та латинське 'i'."
    mutable_text = MutableString(text)
    print(f"Оригінальний текст: {mutable_text}")
    
    replacements = {'i': 'і', 'р': 'р', 'с': 'с', 'е': 'е', 'о': 'о', 'а': 'а'}
    for i, char in enumerate(mutable_text):
        if char in replacements:
            mutable_text[i] = replacements[char]
    
    print(f"Виправлений текст: {mutable_text}")
    print(f"Довжина виправленого тексту: {len(mutable_text)}")

def test_task_545() -> None:
    print("Завдання 5.4.5 - Matrix і Vector")
    
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
    print(f"Визначник матриці A: {a()}")
    print("Перевірка розв'язку:")
    print(f"A * x = {a * Vector3D(x)}")
    print(f"b = {b}")

def test_task_546() -> None:
    print("Завдання 5.4.6 - Polynom")
    
    p1 = Polynom([1, -5, 6])
    p2 = Polynom([2, 1])
    
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
    print(f"Похідна p1: {p1.derivative()}")
    print(f"Первісна p1: {p1.integral()}")

def solve_quadratic(a: Union[Complex, float], b: Union[Complex, float], c: Union[Complex, float]) -> str:
    if a == 0:
        if b == 0:
            return "Рівняння не має коренів" if c != 0 else "Рівняння має нескінченно багато розв'язків"
        return f"x = {-c / b}"
    
    discriminant = b*b - 4*a*c
    if isinstance(discriminant, Complex) or discriminant >= 0:
        x1 = (-b + discriminant ** 0.5) / (2 * a)
        x2 = (-b - discriminant ** 0.5) / (2 * a)
    else:
        discriminant = Complex(0, abs(discriminant) ** 0.5)
        x1 = (-b + discriminant) / (2 * a)
        x2 = (-b - discriminant) / (2 * a)
    return f"x1 = {x1}, x2 = {x2}"

def test_task_547() -> None:
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
    
    print(f"Рівняння з дійсними коефіцієнтами: x^2 - 3x + 2 = 0")
    print(f"Розв'язок: {solve_quadratic(1, -3, 2)}")
    
    print(f"Рівняння з комплексними коефіцієнтами: x^2 + {Complex(0, 2)}x + 1 = 0")
    print(f"Розв'язок: {solve_quadratic(Complex(1, 0), Complex(0, 2), Complex(1, 0))}")

def test_task_548() -> None:
    print("Завдання 5.4.8 - Sentence")
    
    text = "Це речення містить кілька слів які треба замінити. Це речення також містить слова які треба видалити."
    sentences = [Sentence(line.strip()) for line in text.split(".") if line.strip()]
    
    print("Оригінальний текст:")
    for sentence in sentences:
        print(f"- {sentence}")
    
    words_to_replace = {"речення": "твердження", "слів": "лексем", "кілька": "декілька"}
    words_to_delete = ["які", "також"]
    
    print("\nТекст після заміни слів:")
    sentences = [sentence.replace(old, new) for sentence in sentences 
                for old, new in words_to_replace.items()]
    for sentence in sentences:
        print(f"- {sentence}")
    
    print("\nТекст після видалення слів:")
    sentences = [sentence - word for sentence in sentences for word in words_to_delete]
    total_words = sum(len(sentence) for sentence in sentences)
    
    for sentence in sentences:
        print(f"- {sentence}")
    print(f"\nЗагальна кількість слів у відкоригованому тексті: {total_words}")

def test_task_549() -> None:
    print("Завдання 5.4.9 - CustomDict")
    
    text = "Це текст містить багато слів. Деякі слова повторюються. Слова мають різну довжину. Різні слова мають різну частоту."
    word_dict = CustomDict()
    
    for word in text.lower().split():
        word = word.strip(',.;:!?')
        if word:
            word_dict[word] = word_dict.get(word, 0) + 1
    
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

def test_task_5410() -> None:
    print("Завдання 5.4.10 - StringDict")
    
    eng_ukr_dict = StringDict()
    eng_words = "mystery mystery cat mystery cat apple".split()
    ukr_words = "таємниця загадка кіт таїнство кішка яблуко".split()
    
    for eng, ukr in zip(eng_words, ukr_words):
        if eng in eng_ukr_dict:
            if ukr not in eng_ukr_dict[eng]:
                eng_ukr_dict[eng].append(ukr)
        else:
            eng_ukr_dict[eng] = [ukr]
    
    print("Англо-український словник:")
    for eng, ukr_list in eng_ukr_dict.items():
        print(f"{eng}: {', '.join(ukr_list)}")
    
    ukr_eng_dict = eng_ukr_dict.create_reverse_dict()
    print("\nУкраїно-англійський словник:")
    for ukr, eng_list in ukr_eng_dict.items():
        print(f"{ukr}: {', '.join(eng_list)}")
    
    word_to_translate = "mystery"
    translations = eng_ukr_dict.get_translations(word_to_translate)
    print(f"\nПереклади для слова '{word_to_translate}': {', '.join(translations)}")
    
    word_most_translations = eng_ukr_dict.word_with_most_translations()
    print(f"Слово з найбільшою кількістю перекладів: {word_most_translations} ({len(eng_ukr_dict[word_most_translations])} перекладів)")
    
    single_translation_words = eng_ukr_dict.words_with_single_translation()
    print(f"Англійські слова з одним перекладом: {', '.join(single_translation_words)}")
    
    print(f"Кількість різних англійських слів: {eng_ukr_dict.count_unique_words()}")
    print(f"Кількість різних українських слів: {eng_ukr_dict.count_unique_translations()}")

def main() -> None:
    tasks = {
        "1": (test_task_531, "Завдання 5.3.1 - Операції з раціональними числами"),
        "2": (test_task_532, "Завдання 5.3.2 - Обробка файлів з раціональними числами"),
        "3": (test_task_541, "Завдання 5.4.1 - CustomList"),
        "4": (test_task_542, "Завдання 5.4.2 - Segment і SegmentSet"),
        "5": (test_task_543, "Завдання 5.4.3 - CustomSet"),
        "6": (test_task_544, "Завдання 5.4.4 - MutableString"),
        "7": (test_task_545, "Завдання 5.4.5 - Matrix і Vector"),
        "8": (test_task_546, "Завдання 5.4.6 - Polynom"),
        "9": (test_task_547, "Завдання 5.4.7 - Complex"),
        "10": (test_task_548, "Завдання 5.4.8 - Sentence"),
        "11": (test_task_549, "Завдання 5.4.9 - CustomDict"),
        "12": (test_task_5410, "Завдання 5.4.10 - StringDict")
    }
    
    print("Доступні завдання:")
    for key, (_, description) in tasks.items():
        print(f"{key}. {description}")
    
    choice = input("Виберіть номер завдання (1-12): ")
    if choice in tasks:
        tasks[choice][0]()
    else:
        print("Некоректний вибір завдання")

if __name__ == "__main__":
    main()
