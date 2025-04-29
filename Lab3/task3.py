import re

try:
    with open('task2.py', 'r', encoding='utf-8') as file:
        input_code = file.read()

    cleaned_code = re.sub(r'(#.*|\n\s*\n+)', r'\n', input_code).strip('\n')
    cleaned_code = re.sub(r'^\s*\n', '', cleaned_code, flags=re.MULTILINE)

    with open('cleaned_task2.py', 'w', encoding='utf-8') as outfile:
        outfile.write(cleaned_code)

    print("Очищений код з 'task2.py' збережено у 'cleaned_task2.py'")
except FileNotFoundError:
    print("Помилка: Файл 'task2.py' не знайдено.")
except Exception as e:
    print(f"Виникла помилка: {e}")