import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

st.title("Аналіз маршрутів у мережі")

# Створення графа
G = nx.Graph()

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

nodes = list(G.nodes())

start = st.selectbox("Оберіть початковий вузол:", nodes)
end = st.selectbox("Оберіть кінцевий вузол:", nodes)

if st.button("Знайти маршрут"):
    path = nx.dijkstra_path(G, start, end)
    length = nx.dijkstra_path_length(G, start, end)

    st.success(f"Шлях: {path}")
    st.info(f"Довжина: {length}")

    # Візуалізація
    pos = nx.spring_layout(G)

    plt.figure()
    nx.draw(G, pos, with_labels=True, node_color="lightblue")

    # Підсвічування маршруту
    path_edges = list(zip(path, path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="red", width=2)

    st.pyplot(plt)