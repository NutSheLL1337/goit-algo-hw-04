import time
from functools import lru_cache
import random

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


print("Вимірюємо для звичайного масиву: ")
# Приклад використання
array = [12, 11, 13, 5, 6, 7]
start = time.perf_counter()

print(f"Given array is {array}")
print(f"Sorted array is {merge_sort(array)}")
end = time.perf_counter()
print("Merge sort. Seconds taken: {:.7f}".format(end - start))


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
start = time.perf_counter()
print(f"Given array is {array}")
print(f"Sorted array is {insertion_sort_recursive(array, len(array))}")

end = time.perf_counter()
print("Insertion sort. Seconds taken: {:.7f}".format(end - start))


# Використання вбудованих в python sorted and sort
array = [12, 11, 13, 5, 6, 7]
start = time.perf_counter()
print(f"Given array is {array}")
print(f"Sorted array is {sorted(array)}")
end = time.perf_counter()
print("Timsort. Seconds taken: {:.7f}".format(end - start))


print("Вимірюємо для різних наборів даних: ")
# Функція для вимірювання часу виконання
def measure_time(sort_func, arr):
    start = time.perf_counter()
    sort_func(arr)
    end = time.perf_counter()
    return end - start

# Генерація масиву випадкових чисел
large_array = random.sample(range(100000), 10000)

# Вимірювання часу для сортування злиттям
merge_time = measure_time(merge_sort, large_array.copy())
print(f"Merge sort. Time taken: {merge_time:.7f} seconds")

# Вимірювання часу для сортування вставками (на невеликому масиві)
insertion_time = measure_time(lambda arr: insertion_sort_recursive(arr, len(arr)), large_array[:100].copy())
print(f"Insertion sort. Time taken: {insertion_time:.7f} seconds")

# Вимірювання часу для вбудованого Timsort
timsort_time = measure_time(sorted, large_array.copy())
print(f"Timsort. Time taken: {timsort_time:.7f} seconds")
print("Висновки:\nСортування вбудованого Timsort є найбільш ефективним по часу. \nВоно добре працює для різних масивів даних, як маленьких так і великих")