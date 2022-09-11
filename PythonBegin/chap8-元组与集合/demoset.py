# 李亚钦
# 2022/7/22 17:25
"""创建集合的几种方式"""
"""集合是没有value的字典"""

s = {1, 2, 25, 45, 32}
print(s, type(s))

print(set(range(6)))

print(set({1, 5, 65, 55}))

print(set([1, 65, 23, 10, 20]))

print(set((12, 55, 10, 30)))

print(set('python'))

# 创建空集合，不能用{}
ss = set()
print(ss, type(ss))

"""集合的先关操作"""
"""集合元素的判断操作"""
s0 = {1, 2, 3, 4, 5}
print(1 in s0)
print(1 not in s0)
print(10 in s0)
print(10 not in s0)
"""集合新增操作"""
s0.add(6)  # 一次新增一个元素
print(s0)
s0.update({7, 8, 9})  # 一次新增至少一个元素
print(s0)
s0.update(([10, 20, 30]))  # 可以是列表
print(s0)
s0.update((40, 50, 30))  # 可以使元组
print(s0)
"""集合元素的删除操作"""
s0.remove(10)  # 一次删除一个指定元素，元素不存在则Key error抛出异常
print(s0)
s0.discard(100)  # 一次删除一个指定元素，元素不存在则不会抛出异常
print(s0)
s0.pop()  # 一次删除任意一个元素
print(s0)
s0.clear()  # 清空集合
print(s0)

"""集合之间的关系"""
s1 = {10, 20, 30, 40, 50}
s2 = {10, 20, 30}
s3 = {10, 20, 100}
s4 = {200, 300}
"""两个集合是否相等"""
print(s1 == s2)
print(s1 != s2)
"""一个集合是否是另一个集合的子集"""
print(s2.issubset(s1))
print(s3.issubset(s1))
"""一个集合是否是另一个集合的超集"""
print(s1.issuperset(s2))
print(s1.issuperset(s3))
"""两个集合是否没有交集"""
print(s1.isdisjoint(s2))
print(s1.isdisjoint(s4))

"""集合的数学操作"""
s5 = {10, 20, 30, 40}
s6 = {30, 40, 50, 60}
"""交集"""
print(s5.intersection(s6))
print(s5 & s6)  # intersection与&等价
"""并集"""
print(s5.union(s6))
print(s5 | s6)  # union与|等价
"""差集"""
print(s5.difference(s6))
print(s5 - s6)  # difference与-等价
"""对称差集"""
print(s5.symmetric_difference(s6))
print(s5 ^ s6)  # symmetric_difference与^等价

"""集合生成式"""
s7 = {i for i in range(6)}
print(s7)
s8 = {i**2 for i in range(6)}
print(s8)
