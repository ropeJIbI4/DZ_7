from fractions import Fraction   

def check_input_fraction(string):
    '''
     Пользовательский ввод рационального числа в формате целого числа,простой дроби x/x:;
        
    '''
    try:
        num_N = Fraction(input(string))
        return(num_N)
    except ValueError:
        print('некорректный ввод!')
        return check_input_fraction(string)
    

def check_input_complex(string):
    '''
     Пользовательский ввод комплексного числа в формате a+bj;
     
    
    '''
    try:
        complex_N = complex(input(string))
        return(complex_N)
    except ValueError:
        print('некорректный ввод!')
        return check_input_complex(string)
        

def check_input_operator(string):
    '''
     Пользовательский ввод арифметического оператора (+, -, *, /).
     
    
    '''
    operator = input(string)
    if operator == '+' or operator == '-' or operator == '*' or operator == '/':
        return operator
    else:
        print('некорректный ввод!')
        return check_input_operator(string)


def check_input_type_number(string):
    '''
     Пользовательский выбор типа вводимого числа (рациональное → 1 или комплексное → 2).
    
    '''
    try:
        type_number = int(input(string))
        if type_number == 1 or type_number== 2:
            return int(type_number)
        else:
            print('некорректный ввод!')
            return check_input_type_number(string)
    except ValueError:
        print('некорректный ввод!')
        return check_input_type_number(string)
