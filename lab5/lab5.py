import itertools
import numpy as np

def isomorphic(graph1, graph2):
    # Перевірка, чи графи мають однакову розмірність
    if np.shape(graph1) != np.shape(graph2):
        return False

    num = len(graph1)
    for perm in itertools.permutations(range(num)):
        valid = True
        checking = {}

        # Перевіряємо, чи перестановка є дійсним ізоморфізмом
        for i in range(num):
            for j in range(num):
                if graph1[i][j] != graph1[perm[i]][perm[j]]:
                    valid = False
                    break
            if not valid:
                break

            # Записуємо відповідність між вершинами графів
            checking.setdefault(graph1[i][i], graph2[perm[i]][perm[i]])
            if checking[graph1[i][i]] != graph2[perm[i]][perm[i]]:
                valid = False
                break

        if valid:
            return True

    return False

# Зчитування даних матриці з файлу
with open('D:/Anastasiia Marchuk/politeh/semestr 4.2/дискретні моделі/lab5/m1.txt') as file:
    adjacency_matrix1 = np.loadtxt(file, dtype=int)
    print(f"\nМатриця суміжності першого графу:\n{adjacency_matrix1}")
with open('D:/Anastasiia Marchuk/politeh/semestr 4.2/дискретні моделі/lab5/m2.txt') as file:
    adjacency_matrix2 = np.loadtxt(file, dtype=int)
    print(f"\nМатриця суміжності другого графу:\n{adjacency_matrix2}")

# Перевірка чи графи є ізоморфними
if isomorphic(adjacency_matrix1, adjacency_matrix2):
    print("\nГрафи є ізоморфні.")
else:
    print("\nГрафи НЕ ізоморфні.")