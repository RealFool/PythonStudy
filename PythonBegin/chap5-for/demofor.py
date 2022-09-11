# 李亚钦
# 2022/7/21 22:39
for item in 'Hello':
    print(item)

for i in range(10):
    print(i)

for _ in range(3):
    print('若是不用自定义变量，自定义变量可写为_')

# 1-100偶数和

sum_num = 0
for item in range(1, 101):
    if not item % 2:
        sum_num += item
print(sum_num)
