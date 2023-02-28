# This is the way
# Author: pythontoday
# YouTube: https://www.youtube.com/c/PythonToday/videos

import random
from time import sleep
import requests
from bs4 import BeautifulSoup
import json
import csv
#полуение и сохрание главнной страницы
#url = "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"

#заголовки нужны для того чтобы показать сайту что мы не бот 
headers = {
    "Accept": "*/*",
    
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}
#req = requests.get(url, headers=headers)
#src = req.text
#print(src)
#сохрание текста сайта, потмоу что сайт не любят парсинг
#with open("index.html", "w") as file:
#    file.write(src)



#для дальнейшей работы код выше ненужен, поэтому его коментируем



with open("index.html") as file:
    src = file.read()

#передадим данные супу и перейдем к сбору данных
#soup = BeautifulSoup(src, "lxml")
#cначала нужно получить все ссылки на категории тоаров, ищем общий див для всех товаров
#all_products_hrefs = soup.find_all(class_="mzr-tc-group-item-href")
 
#смотрим что удалось собрать
#all_categories_dict = {}
# for item in all_products_hrefs:
#     item_text = item.text
#     item_href = "https://health-diet.ru" + item.get("href")
#
#     all_categories_dict[item_text] = item_href
# #ссылки сохраняются в файл
# with open("all_categories_dict.json", "w") as file:
#     json.dump(all_categories_dict, file, indent=4, ensure_ascii=False) #ensure_ascii=False для работы с кирилицей



#для дальнейшей работы код выше ненужен, поэтому его коментируем


#загрузим файл джейсона в перменную
with open("all_categories_dict.json") as file:
    all_categories = json.load(file)

#нужно создать цил на каждой итерации которого мы будем заходить в категорию собирать  нее данные и записываьб их в файл
count = 0
for category_name, category_href in all_categories.items():
    if count == 0:
        rep = [",", " ", "-", "'"] #замена всех , " " - и ' на _
        for item in rep:
            if item in category_name:
                category_name = category_name.replace(item, "_")

        req = requests.get(url=category_href, headers=headers)
        src = req.text
        #сохраняем кажду категорию в отдельную страницу
        with open(f"data/{count}_{category_name}.html", "w") as file:
            file.write(src)

        with open(f"data/{count}_{category_name}.html") as file:
            src = file.read()

        soup = BeautifulSoup(src, "lxml")
        count =+1
