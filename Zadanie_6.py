import csv


# Функция для определения категории покупки на основе источника
def get_purchase_category(source):
    """
  Определяет категорию покупки на основе источника.

    Args:
        источник (str): Источник визита.

    Returns:
        str: Категория покупки или None, если ни одна категория не соответствует источнику.
    """
    if source == 'context':
        return 'Электроника'
    elif source == 'email':
        return 'Продукты'
    elif source == 'other':
        return 'Продукты'
    else:
        return None # Нет соответствующей категории

# Открываем входной и выходной файлы
with open('visit_log.csv', 'r', encoding='utf-8') as visit_log, \
     open('funnel.csv', 'w', encoding='utf-8', newline='') as funnel:

    # Создаем объекты для чтения и записи CSV
    reader = csv.reader(visit_log)
    writer = csv.writer(funnel)

    # Записываем строку заголовка в выходной файл
    writer.writerow(['user_id', 'source', 'category'])

    # Обрабатываем каждую строку во входном файле
    next(reader)  # Пропускаем строку заголовка в visit_log.csv
    for row in reader:
        user_id, source = row

        # Определяем категорию покупки
        category = get_purchase_category(source)

        #Если есть категория покупки, записываем строку в выходной файл
        if category:
            writer.writerow([user_id, source, category])

print("Обработка файлов завершена.")