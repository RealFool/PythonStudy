print("hello")

# 输出到文件
fb = open('/text.txt', 'a+') # a+文件不存在则创建，存在则往后加
print('hello', file=fb)
fb.close()

# 不换行
print('hello', 'world')





