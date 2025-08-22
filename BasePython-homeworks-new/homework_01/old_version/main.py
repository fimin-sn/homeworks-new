"""
Домашнее задание №1
Функции и структуры данных
"""
"""
1.   функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
def power_numbers(*args):
    #numbers = [i**2 for i in args]
    numbers = list(map(lambda i:i**2 ,[*args]))
    return numbers

print(power_numbers(1, 2, 5, 7))


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"
"""
2.    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """


def test_number_on_divide(item):
    condition = True
    for i in range(2, item):
        if item % i == 0:
            condition = False
            break
    return condition


def check_simple_number(test_item):
    '''
        Простое число - это натуральное число больше 1,
        которое делится нацело только на 1 и на само себя.
        Например, 2, 3, 5, 7, 11, 13, 17, 19 - это простые числа.
        Согласно условию задачи аргументы могут быть только числами,
        поэтому выделяем только натуральные числа и проверяем, чтобы
        они делились нацело на само себя. На единицу делятся все натуральные числа.
    '''
    if (isinstance(test_item,int)
            and test_item > 1
            and test_number_on_divide(test_item)):
        return True
    else:
        return False


def filter_numbers(list_numbers,filter_types):
    #print(list_numbers,filter_types)
    match filter_types:
        case 'odd': return [item for item in list_numbers if item%2 != 0]
        case 'even': return [item for item in list_numbers if item%2 == 0]
        case 'prime': return [item for item in list_numbers if check_simple_number(item)]



#Test for function select_simple_numbers(*args):
print(filter_numbers([1, 2, 3], ODD))
print(filter_numbers([2, 3, 4, 5], EVEN))
print(filter_numbers([1,2, 3, 4, 5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,complex(2,3),15.1,138,137,270,277,281,998,997,1027,1021,8861,8859,16831,16850,182200,188389], PRIME))