import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Customer-Churn-Records.csv')
print("Задание 1: Датасет загружен, вот первые строки:\n", df.head())

df.columns = [col.lower().replace(' ', '_') for col in df.columns]
print("\nЗадание 2: Названия столбцов обновлены:\n", df.head())

print("\nЗадание 3: Инфа по датафрейму:")
df.info()

avg_balance_by_geo = df.groupby('geography')['balance'].mean()
# Рисуем график
avg_balance_by_geo.plot(kind='bar')
plt.title('Средний баланс по странам')
plt.xlabel('Страна')
plt.ylabel('Средний баланс')
plt.show()
print("\nЗадание 4: Диаграмма готова!")

mean_balance_by_country = df.groupby('geography')['balance'].mean().to_dict()
# Добавляем новый столбец
df['balance_by_country'] = df['geography'].map(mean_balance_by_country)
print("\nЗадание 5: Добавил столбец balance_by_country:\n", df.head())

pivot_data = df.groupby(['geography', 'gender'])['numofproducts'].sum().unstack()
# Рисуем график с накоплением
pivot_data.plot(kind='bar', stacked=True)
plt.title('Общее количество продуктов по странам и полу')
plt.xlabel('Страна')
plt.ylabel('Количество продуктов')
plt.legend(title='Пол')  # Добавляем легенду
plt.show()
print("\nЗадание 6: Диаграмма готова")
