from typing import List


def calculate_median(numbers: List[float]) -> float:
    if not numbers:
        return None

    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)

    if n % 2 == 1:
        return float(sorted_numbers[n // 2])
    else:
        mid1 = n // 2 - 1
        mid2 = n // 2
        return round((sorted_numbers[mid1] + sorted_numbers[mid2]) / 2, 2)


ingreso = input("Ingresa x cantidad de numeros separados por un espacio: ")

numbers = list(map(int, ingreso.split()))

median = calculate_median(numbers)
if median is None:
    print("Median: None")
else:
    print(f"Median: {median:.2f}")