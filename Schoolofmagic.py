names=[
    ["罗恩",23,35,44],
    ["哈利",60,77,68,88,90],
    ["赫敏",97,99,89,91,95,90],
    ["马尔福",100,85,90]
]
sum=0
sum1=0
sum2=0
sum3=0
for i in range(0,3):
    sum=names[0][i+1]+sum
print("罗恩的总成绩为:",sum)
for i in range(0,5):
    sum1=names[1][i+1]+sum1
print("哈利的总成绩为：",sum1)
for i in range(0,6):
    sum2=names[2][i+1]+sum2
print("赫敏的总成绩:",sum2)
for i in range(0,3):
    sum3=names[3][i+1]+sum3
print("马尔福的总成绩:",sum3)