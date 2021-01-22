List=[1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
a=1;b=2;c=3;d=4;e=5;f=6;g=7;h=8;j=9;k=10
a1=0;b1=0;c1=0;d1=0;e1=0;f1=0;g1=0;h1=0;j1=0;k1=0
for i in range(0,15):
    if a==int(List[i]):
        a1=a1+1
    elif b==int(List[i]):
        b1=b1+1
    elif c==int(List[i]):
        c1=c1+1
    elif d==int(List[i]):
        d1=d1+1
    elif e==int(List[i]):
        e1=e1+1
    elif f==int(List[i]):
        f1=f1+1
    elif g==int(List[i]):
        g1=g1+1
    elif h==int(List[i]):
        h1=h1+1
    elif j==int(List[i]):
        j1=j1+1
    elif k==int(List[i]):
        k1=k1+1
print(a,"有",a1,"次")
print(b,"有",b1,"次")
print(c,"有",c1,"次")
print(d,"有",d1,"次")
print(e,"有",e1,"次")
print(f,"有",f1,"次")
print(g,"有",g1,"次")
print(h,"有",h1,"次")
print(j,"有",j1,"次")
print(k,"有",k1,"次")