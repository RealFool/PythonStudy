# 李亚钦
# 2022/7/23 23:23
"""读文件"""
file = open('a.txt', 'r', encoding='UTF-8')
print(file.readlines())
file.close()

"""写文件，文件存在则覆盖"""
file2 = open('b.txt', 'w', encoding='UTF-8')
file2.write('python')
file2.write('hello')
file2.close()

"""追加模式，文件存在则追加"""
file3 = open('c.txt', 'a', encoding='UTF-8')
file3.write('python')
file3.close()

""""二进制模式打开文件，例如拷贝图片"""
file4 = open('a.png', 'rb')
file5 = open('copy.png', 'wb')
file5.write(file4.read())
file5.close()
file4.close()

