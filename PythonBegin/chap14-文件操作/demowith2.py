# 李亚钦
# 2022/7/23 23:57
"""用with实现文件拷贝"""
with open('a.png', 'rb') as a:
    with open('copy2.png', 'wb') as copy:
        copy.write(a.read())
