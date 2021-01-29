'''
    insert,delete,update : 更新数据库。返回结果都是1或者23445
    select: 查询数据库，并返回查询结果
        区别：查询后，需要将返回的数据进行二次处理。
        获取数据：
            fetchall() 获取所有
            fetchone()  获取一条
            fetchmany() 获取多条
    优化：
        采用sql语句和数据进行分离的方式进行增，删，改，查来对数据库进行操作。
        好处：一条sql语句可以多次使用。填充的数据也可以动态替换，一本万利，岂不美哉！！！！！
    任务：
    将增、删、改、查四大操作，写出来使用模板和数据分离的方式来做。提交到云仓库，地址发到群里。
    工商银行的数据库统一采用mysql来存储。增、删、改、查都使用今天的知识来做。
    V1.2.5
    V2.1.0
'''
import pymysql
# 连接数据库
con = pymysql.connect(host="localhost",user="root",password="",database="学生")
# 建立游标
cursor = con.cursor()

# 查询
# sql = "select * from 学生表 where sn = %s"
# param = ["徐玮"]
# num = cursor.execute(sql,param)
# data = cursor.fetchall()
# print("影响了",num,"行数据")
# for i in data:
#     print(i)

# 增加
# sql = "insert into 学生表 value(%s,%s,%s,%s,%s)"
# param = ['s11','张大明','女',20,3]
# num = cursor.execute(sql,param)
# data = cursor.fetchall()
# print("影响了",num,"行数据")

# 删除
# sql = "delete  from 学生表 where sn=%s"
# param = ["张大明"]
# num = cursor.execute(sql,param)
# data = cursor.fetchall()
# print("影响了",num,"行数据")

# 修改
# sql = "update 学生表 set sn=%s where sno='s3'"
# param = ['徐虎']
# num = cursor.execute(sql,param)
# data3=cursor.fetchall()
# print("影响了",num,"行数据")
con.commit()
cursor.close()
con.close()