# Создаем функцию is_year_leap, которая проверяет, является ли год високосным.
def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False

# Вызываем функцию и передаем год (например, 2024) в качестве аргумента.
year_to_check = 2024
result = is_year_leap(year_to_check)

# Выводим результат в консоль.
print(f"год {year_to_check}: {result}")