# 李亚钦
# 2022/7/22 14:10
# 创建字典的两种方式
# 方式一，{}
scores = {'张三': 80, '李四': 90, '王五': 85}
print(scores, type(scores))

# 方式二，内置函数dict
person = dict(name='张三', age=20)
print(person, type(person))

# 查找
print(scores['张三'])
print(scores.get('张三'))
print(scores.get('陈六'))
print(scores.get('陈六', '键不存在'))  # 键值不存在时输出后面的

# 判断键值是否存在
print('张三' in scores)
print('陈六' not in scores)

# 删除键值对
del scores['张三']
print(scores)
# scores.clear()  # 清空字典

# 新增元素
scores['陈六'] = 100
print(scores)

# 修改元素
scores['陈六'] = 99
print(scores)


# 视图操作
keys = scores.keys()
print(keys, type(keys))
print(list(keys))

values = scores.values()
print(values, type(values))
print(list(values))

items = scores.items()
print(items, type(items))
print(list(items))  # 转换之后的列表元素由元组组成， [('李四', 90), ('王五', 85), ('陈六', 99)]

# 字典的遍历
for key in scores:
    print(key, scores[key], scores.get(key))
