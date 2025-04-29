import re  # Імпортуємо бібліотеку для регулярних виразів

text = "first amount is 123.45, second amount is $400, another amount is $50.99, also $12.345"

# Використовуємо регулярний вираз для пошуку сум, що починаються з '$'
amounts = re.findall(r'\$\s?(\d+\.\d*|\d+)', text)

# Перетворюємо знайдені рядки сум у числа типу float
float_amounts = [float(amount) for amount in amounts]  

# Обчислюємо загальну суму та округлюємо до 2 знаків після коми
total_sum = round(sum(float_amounts), 2) 

# Виводимо знайдені суми
print('Знайдені суми:', float_amounts) 

# Виводимо загальну суму
print('Загальна сума:', total_sum)
