import re

date_str = "2024-02-11"

match = re.match(r'(\d{4})-(\d{2})-(\d{2})', date_str)  

if match:
    year, month, day = match.groups()
    converted_date = f"{day}-{month}-{year}"
    print('“yyyy-mm-dd” формат:', date_str)
    print('“dd-mm-yyyy” формат:', converted_date)
else:
    print("Невірний формат дати. Використовуйте формат yyyy-mm-dd.")
