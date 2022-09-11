# 李亚钦
# 2022/7/22 14:37
# 字典生成式
items = ['Zhangsan', 'Lisi', 'Wangwu']
values = [80, 85, 90]

dit = {item: value for item, value in zip(items, values)}
print(dit)
dit = {item.upper(): value for item, value in zip(items, values)}
print(dit)
