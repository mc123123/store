a=[1,5,21,30,15,9,30,24]
sum=0
for i in range(0,8):
    if int(a[i])%5==0:
        sum=sum+int(a[i])
print(sum)