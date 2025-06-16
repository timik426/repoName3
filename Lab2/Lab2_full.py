import pandas as pd
import numpy as np
df_amazon = pd.read_excel('AmazonBooks.xlsx')

df_amazon = pd.read_excel('AmazonBooks.xlsx')
df_amazon.head(3)

print("Задание №1:\n", df_amazon.tail(10))

df_amazon_sorted = df_amazon.sort_values(by='Year', ascending=True)
print("\nЗадание №2:\n", df_amazon_sorted.head())

df_expensive = df_amazon[df_amazon['Price'] > 20]
print("\nЗадание №3:\n", df_expensive.head())

df_subset = df_amazon[['Name', 'User Rating', 'Reviews']]
print("\nЗадание №4:\n", df_subset.head())

df_2011 = df_amazon[df_amazon['Year'] == 2011]
quantile_75 = df_2011['Reviews'].quantile(0.75)
authors_above_quantile = df_2011[df_2011['Reviews'] > quantile_75]['Author'].unique().tolist()
print("\nЗадание №5:\n", authors_above_quantile)

df_amazon['genre_categories'] = df_amazon['Genre'].astype('category')
df_amazon['genre_codes'] = df_amazon['genre_categories'].cat.codes
print("\nЗадание №6:\n", df_amazon[['genre_categories', 'genre_codes']].head())
