# 李亚钦
# 2022/7/24 0:15
"""累出指定目录下的所有py文件"""
import os
path = os.getcwd()
listdir = os.listdir(path)
for filename in listdir:
    if filename.endswith('.py'):
        print(filename)

