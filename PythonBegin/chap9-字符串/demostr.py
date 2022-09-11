# 李亚钦
# 2022/7/22 18:15
"""字符串的查询操作"""
s = "hello,hello"
print(s.index('lo'))    # 查找lo第一次出现的位置，不存在则异常
print(s.find('lo'))     # 查找lo第一次出现的位置，不存在会返回-1
print(s.rindex('lo'))   # 查找lo最后一次出现的位置，不存在则异常
print(s.rfind('lo'))    # 查找lo最后一次出现的位置，不存在会返回-1
