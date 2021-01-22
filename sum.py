
sum=0 #和
avg=0 #平均数
max=0 #最大值
i=0
for i in range(1,11):
    i=int(input("请输入数字:"))
    sum=sum+i

    if i>=max:
        max=i
    avg=sum/10
print("总和为:",sum,"最大值为:",max,"平均数为:",avg)