import re

def process_text():
    """
    Запрашивает у пользователя ввод текста,
    удаляет все последовательные повторы слов и выводит результат.
    """
    pattern = re.compile(r'\b(\w+)(?:\s+\1\b)+', re.IGNORECASE)

    while True:
        text = input("Введите текст (или 'exit' для завершения): ")
        if text.lower() == 'exit':
            break
        result = pattern.sub(r'\1', text)
        print("Результат:", result)


if __name__ == "__main__":
    process_text()