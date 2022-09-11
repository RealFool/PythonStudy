# 李亚钦
# 2022/8/11 21:03
import networkx as nk
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edge('A', 'B', weight=4)
G.add_edge('B', 'D', weight=2)
G.add_edge('A', 'C', weight=3)
G.add_edge('C', 'D', weight=5)
G.add_edge('A', 'D', weight=6)
G.add_edge('C', 'F', weight=7)
G.add_edge('A', 'G', weight=1)
G.add_edge('H', 'B', weight=2)
"""
network 库内置五种图形布局设置：
    circular_layout:顶点在一个圆环上均匀分布
    random_layout:顶点随机分布
    shell_layout：顶点在同心圆上分布
    spring_layout:用Fruchterman-Reingold算法排列顶点
    spectral_layout:根据图的Laplace特征向量排列顶点
"""
# 指定顶点位置
# pos = {1: (2.5, 10), 2: (0, 5), 3: (7.5, 10), 4: (5, 5), 5: (2.5, 0), 6: (7.5, 0), 7: (10, 5)}
pos = nx.spring_layout(G)

# 生成邻接矩阵
mat = nx.to_numpy_matrix(G)
print('生成邻接矩阵:', mat)

# 计算两点间的最短路径
# 迪杰斯特拉算法 dijkstra_path
path = nx.dijkstra_path(G, source='H', target='F')
print('结点H到F的最短路径为：', path)
distance = nx.dijkstra_path_length(G, source='H', target='F')
print('结点H到F的最短距离为：', distance)

# 一点到所有点的最短路径
p = nx.shortest_path(G, source='H')  # target not specified
d = nx.shortest_path_length(G, source='H')
for node in G.nodes():
    print('H到', node, '的最短路径为：', p[node], end='\t')
    print('H到', node, '的最短距离为：', d[node])

# 任意两点间的最短距离
# print(nx.shortest_path_length(G))

# 最小生成树
T = nx.minimum_spanning_tree(G)  # # 返回包括最小生成树的图, 边有权重
print(T.nodes)
print(T.edges)
print(sorted(T.edges))
print(sorted(T.edges(data=True)))

mst1 = nx.tree.minimum_spanning_edges(G, algorithm="kruskal")  # 返回值 带权的边
print('克里斯卡尔算法：', list(mst1))
mst2 = nx.tree.minimum_spanning_edges(G, algorithm="prim", data=False)  # data=False 表示返回值不带权
print('普里姆算法：', list(mst2))

# 绘制网络图

nx.draw(G, pos, with_labels=True, alpha=0.8)  # 绘制无向图
labels = nx.get_edge_attributes(G, 'weight')  # YouCans, SUPT
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color='c')  # 显示边的权值
nx.draw_networkx_edges(G, pos, edgelist=T.edges, edge_color='r', width=4)  # 最小生成树，设置指定边的颜色
plt.show()

# nx.draw(G, with_labels=True)
# nx.draw(T, with_labels=True)
# plt.show()
