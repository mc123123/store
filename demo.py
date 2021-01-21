
# 循环打印  0~ 10之间的数
i = 1
s = 0
s1 = 0
while i <= 10:
    if i % 2 == 0: #  判断是否是偶数
        s = s + i
    else:
        s1 = s1 + i  # 存奇数
    i = i + 1

# 求 1~ 10之间的和
print("1~10之间的偶数和为：",s,"奇数的和为：",s1)

# 求1~10之间偶数的和？

# 打印1~10的5的倍数？
j = 1

while j <= 10:
    if j % 5== 0:
        print(j)
    j = j + 1

























score = input("请输入您的分数：")  # "86"  -->  86tio
score = int(score)

if score >= 90  and score <= 100:
    print("优秀！Excellent!")
elif score >= 80  and score < 90:
    print("良好！good!")
elif score >= 70 and score <80:
    print("一般般！just so so!")
elif score >= 60  and score < 70:
    print("刚及格!")
elif score >= 0 and score < 60:
    print("不及格!小伙子你很危险！您的试卷正在路上！")
else:
    print("您的输入不合法！")















































