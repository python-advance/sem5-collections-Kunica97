import random


def insertion_sort(collection):
    """
    функция сортировки коллекции методом вставки
    :param collection: индексируемая коллекция
    :return: возвращает отсортированную коллекцию
    """
    for i in range(len(collection)):
        j = i - 1
        key = collection[i]
        while collection[j] > key and j >= 0:
            collection[j + 1] = collection[j]
            j -= 1
        collection[j + 1] = key
    return collection


# заполнение массива случайными числами с помощью генератора и модуля random
a = [random.randint(1, 1000) for i in range(20)]
print("Original:", a)
print("Insertion:", insertion_sort(a))
print("Sorted function:", sorted(a))
a.sort()
print("Sort method:", a)
