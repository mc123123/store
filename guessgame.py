
# 三次没猜中，系统锁定5秒
import random
import time # 时间包
# num就当成系统随机产生的随机数
num = random.randint(0,100)
counter = 0 # 计数器
sum=3
nub=100
print(num)
while True:  # 一直执行循环体
    while sum == counter:
        sum = sum + 3
        print("三次没猜中，系统锁定5秒！")
        f = 1
        while f <= 5:
            print(".", end="")  # 缓缓打印一个
            time.sleep(1)  # 睡眠 1秒
            f = f + 1
    counter=counter+1
    n = input("请输入0-100之内要猜的数字：")
    n = int(n)
    if n > num:
        print("0-",n,"之间")
        matrix=n
    elif n < num:
        matrix2=n
        print(n,"到100之间")
    else:
        print("恭喜猜中了！您本次猜了：",counter,"次！")
        break #跳出循环体



















