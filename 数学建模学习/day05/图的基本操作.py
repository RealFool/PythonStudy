# 李亚钦
# 2022/8/11 19:11
import networkx as nx
import matplotlib.pyplot as plt

# 创建空的网格
nf = nx.Graph()
# 添加结点
nf.add_node('A')
# 也可以多个添加
nf.add_nodes_from(['B', 'C', 'D', 'E', 'F', 'G'])
nf.number_of_nodes()  # 查看节点数

# 添加连线
nf.add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'),
                   ('E', 'F'), ('F', 'G'), ('G', 'A')])
print(nf.number_of_edges())  # 边的数目

print('-'*10)
print(nx.density(nf))
print(nx.diameter(nf))
print(nx.clustering(nf))
print(nx.transitivity(nf))
print(list(nf.neighbors('A')))
print(nx.degree_centrality(nf))
print(nx.closeness_centrality(nf))
print(nx.betweenness_centrality(nf))


# 绘制网络图
nx.draw(nf, with_labels=True)
plt.show()



