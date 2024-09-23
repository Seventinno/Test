from typing import List
from random import choice
from statistics import median


def insertion_sort(lista):
    for i in range(1,len(lista)):
        key = lista[i]
        j = i - 1

        while j >= 0 and key < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key


def quick_sort(lista):
    pivot = choice(lista)

    lowers = [x for x in lista if x < pivot]
    equals = [x for x in lista if x == pivot]
    greaters = [x for x in lista if x > pivot]

    quick_sort(lowers)
    quick_sort(equals)
    quick_sort(greaters)

    lista[:] = lowers + equals + greaters
    return lista

# Metodo 1
def calculate_median(numbers: List[float]) -> float:
    if not numbers:
        return None

    if len(numbers) > 10:
        sorted_numbers = quick_sort(numbers)
    else:
        sorted_numbers = numbers[:]
        insertion_sort(sorted_numbers)

    n = len(sorted_numbers)
    if n % 2 == 1:
        return float(sorted_numbers[n // 2])
    else:
        mid1 = n // 2 - 1
        mid2 = n // 2
        return round((sorted_numbers[mid1] + sorted_numbers[mid2]) / 2, 2)


# Metodo 2

def calculate_median2(numbers: List[float]) -> float:
    if not numbers:
        return None
    return median(numbers)


# Metodo 3
def quickselect(arr: List[float], k: int) -> float:
    if len(arr) == 1:
        return arr[0]

    pivot = choice(arr)

    lows = [el for el in arr if el < pivot]
    highs = [el for el in arr if el > pivot]
    pivots = [el for el in arr if el == pivot]

    if k < len(lows):
        return quickselect(lows, k)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots))


def calculate_median3(numbers: List[float]) -> float:
    if not numbers:
        return None

    n = len(numbers)
    if n % 2 == 1:
        return float(quickselect(numbers, n // 2))
    else:
        left = quickselect(numbers, n // 2 - 1)
        right = quickselect(numbers, n // 2)
        return round((left + right) / 2, 2)


def check_entry(entrada: str) -> List[int]:
    try:
        # Convertir cada elemento a entero y validar que son números
        return list(map(int, entrada.split()))
    except ValueError:
        print("Error: Ingrese solo números separados por espacios.")
        return []


# Input
ingreso = input("Ingresa x cantidad de numeros separados por un espacio: ")

numbers = list(map(int, ingreso.split()))

# Calculate median and print result
media = calculate_median(numbers)
if media is None:
    print("Median: None")
else:
    print(f"Median: {media:.2f}")