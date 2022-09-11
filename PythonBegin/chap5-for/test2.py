# 李亚钦
# 2022/7/21 22:46
"""
    输出100到999之间的水仙花数
    153 = 3**3 + 5**3 + 1**3
"""

for item in range(100, 1000):
    g = item % 10
    s = item // 10 % 10
    b = item // 100
    if g**3 + s**3 + b**3 == item:
        print(item)
