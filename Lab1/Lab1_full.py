import numpy as np

identity_matrix = np.eye(12)
print("Задание 1:\n", identity_matrix)

chessboard = np.zeros((9, 9), dtype=int)
chessboard[::2, 1::2] = 1
chessboard[1::2, ::2] = 1
print("\nЗадание 2:\n", chessboard)

np.random.seed(42)
vector = np.random.random(10)
sorted_vector = np.sort(vector)
print("\nЗадание 3:\n", sorted_vector)

np.random.seed(42)
fourth_array = np.random.randint(3, 5, (8, 3))
has_all_fours = np.any(np.all(fourth_array == 4, axis=1))
print("\nЗадание 4:\n", has_all_fours)

array_five = np.zeros(6)
array_five[-1] = 1
print("\nЗадание 5:\n", array_five)

array_3d = np.arange(12).reshape(2, 3, 2)
index_9 = np.unravel_index(9, (2, 3, 2))
print("\nЗадание 6:\n", index_9)
