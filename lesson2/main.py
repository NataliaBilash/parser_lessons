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

#нужно создать цикл на каждой итерации которого мы будем заходить в категорию собирать  нее данные и записываьб их в файл
#счетчик итераций
iteration_count = int(len(all_categories)) - 1
count = 0
print(f"Всего итераций: {iteration_count}")
for category_name, category_href in all_categories.items():

    rep = [",", " ", "-", "'"] #замена всех , " " - и ' на _
    for item in rep:
        if item in category_name:
            category_name = category_name.replace(item, "_")

    req = requests.get(url=category_href, headers=headers)
    src = req.text
    #сохраняем кажду категорию в отдельную страницу в папку data
    with open(f"/home/zeroff/Рабочий стол/parcer/lesson2/data/{count}_{category_name}.html", "w") as file:
        file.write(src)

    with open(f"/home/zeroff/Рабочий стол/parcer/lesson2/data/{count}_{category_name}.html") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")

    # проверка страницы на наличие таблицы с продуктами
    alert_block = soup.find(class_="uk-alert-danger")
    if alert_block is not None:
        continue

    #собираем заголовки таблици, калории граммы и тд
    table_head = soup.find(class_="mzr-tc-group-table").find("tr").find_all("th")
    product = table_head[0].text #ПРОДУКТ   
    calories = table_head[1].text #калории
    proteins = table_head[2].text #
    fats = table_head[3].text #жиры
    carbohydrates = table_head[4].text #углеводы

    #открываем файл на запись в таблицу
    with open(f"/home/zeroff/Рабочий стол/parcer/lesson2/data/{count}_{category_name}.csv", "w", encoding="utf-8") as file: 
        writer = csv.writer(file) #writter будет писателем в который передается файл со странцей, ниже указано что запсывать в файл
        writer.writerow(
            (
                product,
                calories,
                proteins,
                fats,
                carbohydrates
            )
        )
    

    # собираем данные продуктов
    products_data = soup.find(class_="mzr-tc-group-table").find("tbody").find_all("tr")

    product_info = [] #для файла джейсон
    for item in products_data:
        product_tds = item.find_all("td")

        title = product_tds[0].find("a").text
        calories = product_tds[1].text
        proteins = product_tds[2].text
        fats = product_tds[3].text
        carbohydrates = product_tds[4].text

        product_info.append( #json
            {
                "Title": title,
                "Calories": calories,
                "Proteins": proteins,
                "Fats": fats,
                "Carbohydrates": carbohydrates
            }
        )  

        with open(f"/home/zeroff/Рабочий стол/parcer/lesson2/data/{count}_{category_name}.csv", "a", encoding="utf-8") as file: #меняем с w на а так как нам аппендом ниже надо дозаписывать
            writer = csv.writer(file) #writter будет писателем в который передается файл со странцей, ниже указано что запсывать в файл
            writer.writerow(
                (
                    title,
                    calories,
                    proteins,
                    fats,
                    carbohydrates
                )
            )
        
    with open(f"/home/zeroff/Рабочий стол/parcer/lesson2/data/{count}_{category_name}.json", "a", encoding="utf-8") as file:
        json.dump(product_info, file, indent=4, ensure_ascii=False)

    count += 1
    print(f"# Итерация {count}. {category_name} записан...") #простио счеткик итераций
    iteration_count = iteration_count - 1

    if iteration_count == 0:
        print("Работа завершена")
        break

    print(f"Осталось итераций: {iteration_count}")
    sleep(random.randrange(2, 4)) #рандомная пауза между итерациями
