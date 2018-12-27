import random


def split_list(l: list, func):
    """
    :param l: лист для разделения
    :param func: функция, возвращающая True/False для каждого элемента
    :return: Два новых листа
    """
    list_a = []
    list_b = []

    for i in l:
        if func(i):
            list_a.append(i)
        else:
            list_b.append(i)

    return list_a, list_b


a = [random.randint(1, 1000) for i in range(20)]
print("Original:", a)
a, b = split_list(a, lambda i: i % 2 == 0)
print("Even numbers:", a)
print("Odd numbers:", b)
