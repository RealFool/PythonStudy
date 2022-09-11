# 李亚钦
# 2022/7/22 11:26

# 对列表进行排序
print('---sort()函数，不产生新的列表对象---')
lst = [6, 8, 2, 9, 3, 1, 5, 7, 4]
print('排序前：', lst, id(lst))
lst.sort()  # 默认升序
print('排序后：', lst, id(lst))
lst.sort(reverse=True)  # 降序
print('降序', lst, id(lst))

print('---内置函数sorted()，将产生一个新的列表对象---')
lst2 = [40, 50, 20, 60, 30, 10]
print('排序前：', lst2, id(lst2))
new_lst = sorted(lst2)
print('排序后：', new_lst, id(new_lst))
desc_lst = sorted(lst2, reverse=True)
print('降序', desc_lst, id(desc_lst))
