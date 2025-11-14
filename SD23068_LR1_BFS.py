import streamlit as st

# ==========================================
# DISPLAY GRAPH IMAGE
# ==========================================
st.title("Breadth-First Search (BFS)")
st.image("LabReport_BSD2513_#1.jpg", caption="Directed Graph", use_container_width=True)

# ==========================================
# GRAPH 
# ==========================================
graph = {
    'A': ['B','D'],
    'B': ['A','C','E','G'],
    'C': ['B','D'],
    'D': ['C'],
    'E': ['H'],
    'H': ['G','F'],
    'G': ['F'],
    'F': []
}

nodes = list(graph.keys())

# ==========================================
# BFS FUNCTION 
# ==========================================
def bfs(graph, start):
    visited = []
    queue = []

    visited.append(start)
    queue.append(start)

    while queue:
        m = queue.pop(0)
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

    return visited

# ==========================================
# STREAMLIT UI
# ==========================================
start_node = st.selectbox("Select starting node:", nodes)

if st.button("Run BFS"):
    result = bfs(graph, start_node)
    st.subheader("BFS Traversal Order")
    st.write(" → ".join(result))
