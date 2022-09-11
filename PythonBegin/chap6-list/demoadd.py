# 李亚钦
# 2022/7/22 11:01

# append在列表末尾加一个元素
lst = [1, 2, 3, 4, 5, 6]
print(lst)
lst.append(7)
print(lst)

# extend在列表末尾可添加多个元素
lst2 = [8, 9]
lst.extend(lst2)
print(lst)

#  insert可在列表任意位置添加一个元素
print('insert可在列表任意位置添加一个元素')
lst.insert(1, 'python')  # 在指定位置添加一个元素
print(lst)

# 切片，可在列表任意位置，添加多个元素
lst3 = ['hello', 'world']
lst[2::] = lst3  # 覆盖了切片
print(lst)
lst[1:1:] = [6, 6, 6]  # 在1位置添加多个元素
print(lst)
