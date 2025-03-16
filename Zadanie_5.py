import datetime

newspaper_formats = {
    "The Moscow Times": "%A, %B %d, %Y",
    "The Guardian": "%A, %d.%m.%y",
    "Daily News": "%A, %d %B %Y"
}

def parse_date(date_string, newspaper):
    """
   Анализирует строку даты в соответствии с форматом указанной газеты и возвращает объект datetime.

 Аргументы:
 date_string (str): строка даты для анализа.
 газета (str): Название газеты, формат даты которой используется.

 Возвращается:
 datetime: объект datetime, представляющий проанализированную дату, или нет, если синтаксический анализ завершается неудачей.
 """
    try:
        date_format = newspaper_formats[newspaper]
        date_object = datetime.datetime.strptime(date_string, date_format)
        return date_object
    except (ValueError, KeyError):
        return None  # Или вызовите исключение, в зависимости от желаемого поведения.


while True:
    newspaper = input("Введите название газеты (или 'exit', чтобы выйти): ")
    if newspaper.lower() == "exit":
        break

    if newspaper not in newspaper_formats:
        print(f"Ошибка: газета '{newspaper}' не найдена в известных форматах.")
        continue
    date_string = input("Введите строку даты: ")

    date_object = parse_date(date_string, newspaper)

    if date_object:
        print(f"Проанализированная дата: {date_object}")
    else:
        print("Ошибка: не удалось разобрать дату. Пожалуйста, проверьте формат и орфографию.")