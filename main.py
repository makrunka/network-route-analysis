import networkx as nx

# Створюємо граф
G = nx.Graph()

# Додаємо ребра (вузол1, вузол2, вага)
edges = [
    ("A", "B", 4),
    ("A", "C", 2),
    ("B", "C", 5),
    ("B", "D", 10),
    ("C", "E", 3),
    ("E", "D", 4),
    ("D", "F", 11)
]

G.add_weighted_edges_from(edges)

# Ввід користувача
start = input("Введіть початковий вузол: ")
end = input("Введіть кінцевий вузол: ")

# Перевірка
if start not in G or end not in G:
    print("Помилка: такого вузла не існує")
else:
    path = nx.dijkstra_path(G, start, end)
    length = nx.dijkstra_path_length(G, start, end)

    print("Найкоротший шлях:", path)
    print("Довжина шляху:", length)