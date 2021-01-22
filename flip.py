a=0
i=0
b=8
List=[1,2,3,4,5,6,7,8,9]
while i<=4:
   while b>=5 and b<=8:
        a=int(List[i])
        List[i]=int(List[b])
        List[b]=a
        b=b-1
        break
   i=i+1
print(List)