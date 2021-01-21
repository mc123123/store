import time
sum = 0
count=3
while True:
    while count == sum:
        count = count + 3
        print("三次没输入正确的密码，系统锁定5秒！")
        f = 1
        while f <= 5:
            print(".", end="")  # 缓缓打印一个
            time.sleep(1)  # 睡眠 1秒
            f = f + 1
    a = int(input("请输入账号:"))
    b = int(input("请输入密码:"))

    if b==123:
        print("登录成功")
        break
    else:
        print("登录失败")
        sum=sum+1