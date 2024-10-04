import time
from functools import lru_cache

# Python має дві вбудовані функції сортування: sorted і sort. 
# Функції сортування Python використовують Timsort — гібридний алгоритм сортування, 
# що поєднує в собі сортування злиттям і сортування вставками.


# Порівняйте три алгоритми сортування: злиттям, вставками та Timsort за часом виконання. 
# Аналіз повинен бути підтверджений емпіричними даними, отриманими шляхом тестування алгоритмів на різних наборах даних. 
# Емпірично перевірте теоретичні оцінки складності алгоритмів, наприклад, сортуванням на великих масивах. Для заміру часу виконання алгоритмів використовуйте модуль timeit.

# Покажіть, що поєднання сортування злиттям і сортування вставками робить алгоритм Timsort набагато ефективнішим, 
# і саме з цієї причини програмісти, в більшості випадків, використовують вбудовані в Python алгоритми, а не кодують самі. 
# Зробіть висновки.

start = time.perf_counter()

end = time.perf_counter()
print("Plain version. Seconds taken: {:.7f}".format(end - start))

start = time.perf_counter()
fibonacci_recursive(n)
end = time.perf_counter()
print("Plain recursive version. Seconds taken: {:.7f}".format(end - start))

start = time.perf_counter()
fibonacci_lru(n)
end = time.perf_counter()
print("lru cache version. Seconds taken: {:.7f}".format(end - start))


# Функція сортування злиттям
def merge_sort(arr):
    # Якщо довжина масиву менше або дорівнює 1, повертаємо масив як є
    if len(arr) <= 1:
        return arr

    # Визначаємо середину масиву
    mid = len(arr) // 2
    # Ділимо масив на ліву і праву половини
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Рекурсивно сортуємо обидві половини
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Зливаємо дві відсортовані половини
    return merge(left_half, right_half)


# Функція злиття двох відсортованих масивів
def merge(left, right):
    result = []  # Результуючий масив
    left_index, right_index = 0, 0  # Індекси для лівого і правого масивів

    # Зливаємо масиви, порівнюючи елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Додаємо залишкові елементи з обох масивів
    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result  # Повертаємо злитий масив


# Приклад використання
array = [12, 11, 13, 5, 6, 7]

print(f"Given array is {array}")
print(f"Sorted array is {merge_sort(array)}")


def insertion_sort_recursive(arr, n):
    if n <= 1:  # Базовий випадок: якщо масив має один або менше елементів, він вже відсортований
        return

    insertion_sort_recursive(arr, n - 1)  # Сортуємо перші n-1 елементів рекурсивно

    key = arr[n - 1]  # Зберігаємо останній елемент як ключ
    j = n - 2  # Починаємо порівнювати з попереднім елементом
    while j >= 0 and arr[j] > key:  # Поки не дійшли до початку масиву і ключ менший за поточний елемент
        arr[j + 1] = arr[j]  # Зсуваємо поточний елемент вправо
        j -= 1  # Переміщаємось на одну позицію вліво
    arr[j + 1] = key  # Вставляємо ключ на правильну позицію
    return arr  # Повертаємо відсортований масив

# Використання рекурсивного сортування вставками
array = [12, 11, 13, 5, 6, 7]
print(f"Given array is {array}")
print(f"Sorted array is {insertion_sort_recursive(array, len(array))}")


# Вбудований Timsort. sorted і sort

# Використання вбудованих в python sorted and sort

array = [12, 11, 13, 5, 6, 7]
print(f"Given array is {array}")
print(f"Sorted array is {insertion_sort_recursive(array, len(array))}")
