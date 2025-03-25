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

def main():
    with open('input01.txt', 'r') as file:
        expressions = file.readlines()
    
    results_dict = ProtectedDictInt()
    
    results_list = RationalList()
    
    for i, expr in enumerate(expressions):
        result = process_expression(expr.strip())
        results_dict[i] = result
        results_list += result
    
    print("Results stored in ProtectedDict:")
    print(results_dict)
    
    print("\nAll results in RationalList:")
    print(results_list)

if __name__ == "__main__":
    main()
