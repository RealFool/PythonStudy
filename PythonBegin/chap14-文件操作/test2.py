# 李亚钦
# 2022/7/24 0:19
"""文件递归遍历"""
import os
path = os.getcwd()
listdir = os.walk(path)
for dirPath, dirName, filename in listdir:
    # print(dirPath)
    # print(dirName)
    # print(filename)
    for dir in dirName:
        print(os.path.join(dirPath, dir))
    for subFile in filename:
        print(os.path.join(dirPath, subFile))
    print('----------------------------')


