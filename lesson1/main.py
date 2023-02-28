# This is the way
# Author: pythontoday
# YouTube: https://www.youtube.com/c/PythonToday/videos

import re
from bs4 import BeautifulSoup

with open("lesson1/html.html") as file: #прочитать его и сохраниь содержимое в перменную src
    src = file.read()
# print(src) вывод всего html текста

soup = BeautifulSoup(src, "lxml") #скармилваем код бибилотеке, lmxl - название парсера который будет использоваться

#title = soup.title распечатем title сайта
#print(title)
# print(title.text) содержимое тега без самого тега
# print(title.string)

# .find() .find_all()
# page_h1 = soup.find("h1") ищет заголовки h1 и забирает первый надейный подходяий жлемент
# print(page_h1)
#
# page_all_h1 = soup.find_all("h1") все подходящие в виде списка
# print(page_all_h1)
#
# for item in page_all_h1: их можно пербрать в цикле
#     print(item.text)

#user_name = soup.find("div", class_="user__name")
#print(user_name.text.strip()) text.strip() чтобы был только полезный текст а не блок коа целиком, так как это метод супа а не полноценный html текст

# user_name = soup.find(class_="user__name").find("span").text
# print(user_name)

# user_name = soup.find("div", {"class": "user__name", "id": "aaa"}).find("span").text если нужны жесткие требования отбора то можно передать нужные параметры
# print(user_name)

#find_all_spans_in_user_info = soup.find(class_="user__info").find_all("span") поиск всех span с классом user_info
#print(find_all_spans_in_user_info)
#for item in find_all_spans_in_user_info:
#    print(item.text)

# print(find_all_spans_in_user_info[0])
# print(find_all_spans_in_user_info[2].text)

# social_links = soup.find(class_="social__networks").find("ul").find_all("a")  все ссылки пользователя
# print(social_links)

# all_a = soup.find_all("a")
# print(all_a)
#
# for item in all_a:
#     item_text = item.text
#     item_url = item.get("href") для ссылок
#     print(f"{item_text}: {item_url}")

# .find_parent() .find_parents() ищют родтеля или родителей элементов, поднимабтся по структуре html жерева снизу вверх

# post_div = soup.find(class_="post__text").find_parent()
# print(post_div)

# post_div = soup.find(class_="post__text").find_parent("div", "user__post")
# print(post_div)

# post_divs = soup.find(class_="post__text").find_parents("div", "user__post")
# print(post_divs)

# .next_element .previous_element next двигается пошагово а второе показывает предыдущий жлеменьт
# next_el = soup.find(class_="post__title").next_element.next_element.text
# print(next_el)
#
# next_el = soup.find(class_="post__title").find_next().text
# print(next_el)

# .find_next_sibling() .find_previous_sibling() тоже самое внутри искомого тега
# next_sib = soup.find(class_="post__title").find_next_sibling()
# print(next_sib)

# prev_sib = soup.find(class_="post__date").find_previous_sibling()
# print(prev_sib)

# post_title = soup.find(class_="post__date").find_previous_sibling().find_next().text
# print(post_title)

links = soup.find(class_="some__links").find_all("a") #получим ссылки
print(links)
#получим их атрибуты  цикле
for link in links:
    link_href_attr = link.get("href")
    link_href_attr1 = link["href"]

    link_data_attr = link.get("data-attr")
    link_data_attr1 = link["data-attr"]
    
    print(link_href_attr1)
    print(link_data_attr1)

# find_a_by_text = soup.find("a", text="Одежда")
# print(find_a_by_text)
#
# find_a_by_text = soup.find("a", text="Одежда для взрослых")
# print(find_a_by_text)

# find_a_by_text = soup.find("a", text=re.compile("Одежда")) поиск с помощью регшулярных выражений
# print(find_a_by_text)





#find_all_clothes = soup.find_all(text=re.compile("([Оо]дежда)")) поиск в двух регистрах как в верхнем так и в нижнем
#print(find_all_clothes)