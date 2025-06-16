import pandas as pd
import numpy as np
import sqlalchemy as sql
import requests
from bs4 import BeautifulSoup

df_salary = pd.read_excel('Employee_Salary_Dataset.ods', engine='odf', sheet_name='Sheet1')
print("Задание 1: Датасет:\n", df_salary.head())

print("\nЗадание 2: Информация:")
df_salary.info()

df_salary.columns = [col.lower() for col in df_salary.columns]
print("\nЗадание 3: Столбцы в нижнем регистре:\n", df_salary.head())

q1 = df_salary['salary'].quantile(0.25)
q3 = df_salary['salary'].quantile(0.75)
iqr = q3 - q1
lower = q1 - 3 * iqr  # нижняя граница
upper = q3 + 3 * iqr  # верхняя граница
# Оставляем только те строки, где зарплата в пределах границ
df_no_outliers = df_salary[(df_salary['salary'] >= lower) & (df_salary['salary'] <= upper)]
print("\nЗадание 4: Без выбросов:\n", df_no_outliers.head())

# Задание 5: Тянем таблицу с Википедии про доходы в Сибирском ФО
url = "https://ru.wikipedia.org/wiki/%D0%94%D0%BE%D1%85%D0%BE%D0%B4%D1%8B_%D0%BD%D0%B0%D1%81%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Находим все таблицы, нам нужна третья (Сибирский ФО)
tables = soup.find_all('table', class_='wikitable')
siberian_table = tables[2]  # Индекс 2 - это наша таблица

# Вытаскиваем данные из таблицы
rows = siberian_table.find_all('tr')
data = []
for row in rows[1:]:  # Пропускаем первую строку с заголовками
    cols = row.find_all('td')
    cols = [col.text.strip().replace('\xa0', '').replace(',', '.') for col in cols]
    # Берем только первые 5 колонок, если их больше
    cols = cols[:5]  # Убеждаемся, что ровно 5 столбцов
    data.append(cols)

# Делаем датафрейм с правильным количеством столбцов
columns = ['Субъект', '2015_октябрь', '2015_ноябрь', '2015_декабрь', '2016_январь']  # Убрал лишний "2016_февраль"
df_incomes = pd.DataFrame(data, columns=columns)

# Чистим столбцы с числами, убираем "руб." и переводим в float
for col in columns[1:]:
    df_incomes[col] = df_incomes[col].str.replace('руб.', '').astype(float)

print("\nЗадание 5: Данные по доходам в Сибирском ФО:\n", df_incomes)

engine = sql.create_engine('sqlite:///incomes.db')
# Записываем датафрейм в таблицу incomes, если она уже есть - перезаписываем
df_incomes.to_sql('incomes', engine, if_exists='replace', index=False)
print("\nЗадание 6: Сохранил таблицу в SQLite")
