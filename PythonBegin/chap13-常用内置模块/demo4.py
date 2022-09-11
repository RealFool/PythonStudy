# 李亚钦
# 2022/7/23 23:08
import schedule
import time


def job():
    print('哈哈-------------')


# 定时任务
schedule.every(3).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
