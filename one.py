import pymysql
host="localhost"
database="工商银行"
user="root"
passwrod=""

def update(sql,param):
    # 连接数据库
    con=pymysql.connect(host=host,user=user,password=passwrod,database=database)
    # 创建游标
    cursor=con.cursor()
    # 进行运算
    cursor.execute(sql,param)
    # 上传到数据库
    con.commit()
    # 关闭游标
    cursor.close()
    # 关闭数据库
    con.close()

def find(sql,param,mode="all",size=1):
    # 连接数据库
    con = pymysql.connect(host=host, user=user, password=passwrod, database=database)
    # 创建游标
    cursor = con.cursor()
    # 进行运算
    cursor.execute(sql,param)
    # 上传到数据库
    con.commit()
    # 进行判断
    if mode=="all":
        return cursor.fetchall()
    elif mode=="one":
        return cursor.fetchone()
    elif mode=="many":
        return cursor.fetchmany(size)
    # 关闭游标
    cursor.close()
    # 关闭数据库
    con.close()

# 获取数据
f = open("a.txt", "r+", encoding="utf-8")
# 将所有行的数据放入列表中
lis = f.readlines()
# 遍历数据
for i in lis:
    # 把数据的换行换成空字符串，并且以逗号隔开，并且把数据赋值给use_lis
    use_lis = i.replace("\n","").split(",")
    # 书写sql语句
    sql="insert into 用户 values(%s,%s,%s)"
    # 把数据传给param
    param=use_lis
    # 调用update方法
    update(sql,param)
# 关闭数据
f.close()

# 查询的sql语句
sql="select sum(净资产) from 用户"
# sum(净资产)是一个字段，如果放到param里面则为一个str类型
param=[]
# 调用find方法
data=find(sql,param,mode="all",size=1)
# 显示总资产
print(data[0][0])

# 将数据库文件转为文本文件
sql="select * from 用户"
param=[]
# 打开b.txt文件
c = open("b.txt","r+",encoding="utf-8")
# 找到数据库中的数据赋值给m
m=find(sql,param,mode="all",size=1)
# 遍历数据库中的数据
for i in m:
    # 把数据库中数据的每一个每次都赋值给a
    a=i[0]+','+str(i[1])+','+str(i[2])+"\n"
    # 把数据库文件传到b.txt文件中保存
    c.write(a)
# 关闭b.txt文件
c.close()

# sql="insert into 用户 value(%s,%s,%s)"
# param=["names[use_lis[0]]","names[use_lis[1]]",names[int(use_lis[2])]]
# update(sql,param)

