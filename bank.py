import random

# 银行的名称
bank_name = "北京市工商银行昌平支行"

# 银行的库
users = {}

'''
{"张三":
    {account:"12345",
    "国家":"中国"}
}
'''

# 欢迎界面
welcome = '''
*********************************
*    欢迎来到中国工商银行管理系统 *
*********************************
*    1.开户                      *
*    2.存钱                      *
*    3.取钱                      *
*    4.转账                      *
*    5.查询                      *
*    6.bye！                     *
*********************************
'''

# 专门来获取8位随机账号
def getRandom():
    li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    # 循环8次
    string = ""
    for i in range(8):  # 循环8次获取随机字符
        ch = li[random.randint(0, 9)]
        string = string + str(ch)
    return string

# 银行的核心开户方法
def bank_addUser(account, username, password, money, country, province, street, door):
    # 先判断银行库是否已满 ： 100个最大
    if len(users) >= 100:
        return 3
    # 判断是否已经存在
    elif username in users:  # 这种方式只判断是否在字典的键里存在
        return 2

    # 可以正常开户：将个人数据存到用户库里
    else:
        users[username] = {
            "account": account,
            "password": password,
            "money": money,
            "country": country,
            "province": province,
            "street": street,
            "door": door,
            "bank_name": bank_name
        }
        return 1

def bank_savemoney(username, money):
    i = users.values()    # 字典里面的值给了i
    if username in users:  # 判断用户里面有没有用户名
        users[username]["money"]=money+users[username]["money"]
        return 1
    else:
        return 2

def query():
    username = input("请输入用户名:")
    password = input("请输入密码:")
    savequery = bank_query(username, password)
    if savequery == 1:
        print("您的用户名为:", username)
        print("您的密码为:", users[username]["password"])
        print("您的余额为:", users[username]["money"])
        print("您所在国家为:", users[username]["country"])
        print("您所在省份为:", users[username]["province"])
        print("您所在街道为:", users[username]["street"])
        print("您所在门牌号为:", users[username]["door"])
        print("开户行名为:", users[username]["bank_name"])
    elif savequery == 2:
        print("密码输入错误")
    else:
        print("该用户不存在")


def bank_query(username, password):
    a = users.values()  #把值赋给a
    if username in users:  #判断用户里面有没有用户名
        for i in a:  #遍历字典
            if password in users:   #
                return 1
            else:
                return 2
    else:
        return 3
# 银行的核心取款方法
def bank_withdraw_money(username,password,money):
    a = users.values()     # 把值赋给a
    if username in users:  # 判断用户里面有没有用户名
        for i in a:   # 遍历字典
            if password in users:
                if (money < users[username]["money"]) or (money == users[username]["money"]):
                    users[username]["money"]=users[username]["money"]-money
                    return 1
                else:
                    return 3
            else:
                return 2
    else:
        return 0

def withdraw_money():
    username = input("请输入用户名：")
    password = input("请输入取款密码：")
    money = int(input("请输入您的取款金额："))
    # 将数据传给银行
    status1=bank_withdraw_money(username,password,money)
    if status1==0:
        print("您输入的账号不存在！")
    elif status1==2:
        print("您输入的密码错误！")
    elif status1==3:
        print("您的余额不足！")
    elif status1==1:
        print("取款成功！您当前的余额为：",username,users[username]["money"])

def savemoney():
    username=input("请输入用户名:")
    while True:
        money = input("请输入金额:")
        if money.isdigit():
            money = int(money)
            break
        else:
            print("余额输入错误，请重新输入！")
    print(users[username]["money"])
    returnvalue = bank_savemoney(username, money)
    if returnvalue == 1:
        print("存钱成功！！！","您的账号为:",username,"您的余额为:",users[username]["money"])
    else:
        print("查无此用户！！！")

# 普通的开户方法
def addUser():
    # 完成具体的开户输入
    # 姓名(str)、密码(int:6位数字)、地址、存款余额(int)、国家(str)、省份(str)、街道(str)、门牌号(str)
    username = input("请输入姓名：")
    password = input("请输入初始取款密码：")
    money = int(input("请输入您的初始金额："))  # 金额是整数形式
    print("接下来输入地址信息：")
    country = input("请输入您所在国家：")
    province = input("请输入您所在省份：")
    street = input("请输入您所在的街道：")
    door = input("请输入您地址的门牌号：")
    account = getRandom()  # 获取随机账号

    # 将数据传给银行
    status = bank_addUser(account, username, password, money, country, province, street, door)
    if status == 3:
        print("对不起，银行用户已满！请携带证件到其他银行办理！")
    elif status == 2:
        print("对不起，您的个人信息已存在！请勿重复开户！")
    elif status == 1:
        print("恭喜，开户成功！以下是您的个人开户信息：")
        print("-------------------------------------")
        print("您的账号为:", users[username]["account"])
        print("您的密码为:", users[username]["password"])
        print("您的余额为:", users[username]["money"])
        print("您的用户名为:", username)
        print("您所在国家为:", users[username]["country"])
        print("您所在省份为:", users[username]["province"])
        print("您所在街道为:", users[username]["street"])
        print("您所在门牌号为:", users[username]["door"])
        print("开户行名为:", users[username]["bank_name"])
        print(users)

def bank_transfer(out_username, up_username, out_pass, out_money):
    if out_username in users and up_username in users:
        if out_pass == users[out_username]["password"]:
            if out_money <= users[out_username]["money"]:
                return 0
            else:
                return 3
        else:
            return 2
    else:
        return 1

def transferMoney():
    out_username = input("请输入转出账号:")
    up_username = input("请输入转入账号:")
    out_pass = input("请输入转出账号密码:")
    out_money = int(input("请输入转出的金额:"))

    status5 = bank_transfer(out_username, up_username, out_pass, out_money)
    if status5 == 1:
        print("转出账户或转入账户不存在！")
    elif status5 == 2:
        print("密码不正确！")
    elif status5 == 3:
        print("余额不足！")
    elif status5 == 0:
        users[out_username]["money"] = users[out_username]["money"] - out_money
        users[up_username]["money"] = users[up_username]["money"] + out_money
        print("转账成功！","转出账号为:",out_username,"转出账号余额为:",users[out_username]["money"],"转入账号为:",up_username,"转入账号余额为:",users[up_username]["money"])

while True:
    print(welcome)  # 打印欢迎信息
    chose = input("请输入您的业务编号：")
    if chose == "1":
        addUser()
    elif chose == "2":
        savemoney()
    elif chose == "3":
        withdraw_money()
    elif chose == "4":
        transferMoney()
    elif chose == "5":
        query()
    elif chose == "6":
        print("退出成功！欢迎下次光临！")
        break
    else:
        print("输入非法！请重新输入！")
