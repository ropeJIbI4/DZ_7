from fractions import Fraction
import search as srch


def rational_number() -> Fraction:
    '''
     Получение рационального числа от пользователя.
    
    '''
    return srch.check_input_fraction('введите рациональное число в формате целого числа,простой дроби x/x: ')


def complex_number() -> complex:
    '''
     Получение комплексного числа от пользователя.
    
    '''
    return srch.check_input_complex('введите комплексное число в формате a+bj: ')


def operation() -> str:
    '''
     Получение знака арифметической операции от пользователя.
    
    '''
    return srch.check_input_operator('введите символ арифметической операции (+, -, *, /): ')


def type_number() -> int:
    '''
     Получение типа вводимого числа от пользователя (рациональное или комплексное)
    
    '''
    return srch.check_input_type_number('выберете тип числа которое собираетесь ввести (1 → рациональное; 2 → комплексное): ')


def show_result_console(num_1, num_2, operator, result):
    '''
     Вывод результата действия с числами (введёнными пользователем) в консоль.
    
    '''
    print(num_1, operator, num_2, '=', result)


def input_number():
    '''
     Итоговая функция получения числа от пользователя.
     
    '''
    num_type = type_number()
    if num_type == 1:
        number = rational_number()
    else:
        number = complex_number()
    return number