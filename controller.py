import Calculator as calc
import UI as ui
import logger

def button_click():
    '''
    Работа проекта "Калькулятор" 
       
    '''
    num_1 = ui.input_number() 
    num_2 = ui.input_number() 
    action_arithmetic = ui.operation() 

    result = calc.calculator(num_1, num_2, action_arithmetic) 
    ui.show_result_console(num_1, num_2, action_arithmetic, result) 

    logger.logger(num_1, action_arithmetic, num_2, result) 