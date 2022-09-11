# 李亚钦
# 2022/7/22 11:14

# remove删除列表中指定元素
lst = [1, 2, 3, 4, 5, 6, 7]
lst.remove(7)
print(lst)

# pop删除列表中指定索引位置的元素，不指定，则默认删除最后一个元素
lst.pop(5)
print(lst)
lst.pop()
print(lst)

# 切片， 删除切片位置的至少一个元素
lst[1:3:] = []
print(lst)
