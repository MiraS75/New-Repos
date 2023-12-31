def month_to_season(month_number):
    # Создаем словарь, связывающий номера месяцев с сезонами
    seasons = {
        1: "Зима",
        2: "Зима",
        3: "Весна",
        4: "Весна",
        5: "Весна",
        6: "Лето",
        7: "Лето",
        8: "Лето",
        9: "Осень",
        10: "Осень",
        11: "Осень",
        12: "Зима"
    }

    # Проверяем, что номер месяца находится в допустимом диапазоне (1-12)
    if month_number < 1 or month_number > 12:
        return "Неверный номер месяца"

    # Извлекаем сезон из словаря и возвращаем его
    return seasons[month_number]

# Пример использования функции
month_number = 2
season = month_to_season(month_number)
print(f"Месяц {month_number} соответствует сезону: {season}")