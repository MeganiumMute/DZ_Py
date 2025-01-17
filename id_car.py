import re

def check_transport_number():

    # Запрашивает у пользователя ввод транспортного номера,
    # проверяет его валидность и выводит результат.
    
    pattern = re.compile(r'([АВЕКМНОРСТУХABEKMHOPCTYX]\d{3}[АВЕКМНОРСТУХABEKMHOPCTYX]{2})(\d{2,3})$')

    while True:
        car_id = input("Введите транспортный номер (или 'exit' для завершения): ")
        if car_id.lower() == 'exit':
            break

        match = pattern.match(car_id.upper())

        if match:
            number = match.group(1)
            region = match.group(2)
            print(f'Номер {number} валиден. Регион: {region}.')
        else:
            print("Номер не валиден.")

# Вызываем функцию для начала работы
if __name__ == "__main__":
    check_transport_number()