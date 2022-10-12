# Импортируем библиотеку
import requests as requests

# Задаем путь к файлу
source_url = "https://api.npoint.io/c5b249352f0d87037214!"
# Выполняем запрос
result = requests.get(source_url)

if result.status_code == 200:
    print(result.json())
else:
    print("Ошибка при доступе")

a = None
