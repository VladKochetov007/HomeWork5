from src.protected_dict import ProtectedDictInt
from src.rational_list import RationalList
from src.rational import Rational

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

def main():
    print("Task 1 - Evaluate expressions:")
    results = process_task1()
    
    results_dict = ProtectedDictInt()
    for i, result in enumerate(results):
        results_dict[i] = result
    
    print("\nResults stored in ProtectedDict:")
    print(results_dict)
    
    print("\nTask 2 - Sum of all rational numbers:")
    rational_list, total_sum = process_task2()
    
    print(f"All rationals in list: {rational_list}")
    print(f"Sum of all rational numbers: {total_sum}")

if __name__ == "__main__":
    main()
