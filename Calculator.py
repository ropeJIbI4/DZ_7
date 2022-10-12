def calculator(a, b, operator):

    if operator == '+':
        return a+b
    if operator == '-':
        return a-b
    if operator == '*':
        return a*b
    if operator == '/':
        if b == 0:
            print('на ноль делить нельзя!')
            return False
        return a / b 