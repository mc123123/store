a=int(input("请输入三角形的第一条边:"))
b=int(input("请输入三角形的第二条边:"))
c=int(input("请输入三角形的第三条边:"))
if a!=0 and b!=0 and c!=0 and (a+b>c) and (a+c>b) and (b+c>a):
    print("能组成三角形")
    if a**2+b**2==c**2 or b**2+c**2==a**2 or a**2+c**2==b**2:
        print("组成直角三角形")
    elif a==b and b==c and a==c:
        print("组成等边三角形")
    elif a==b or a==c or b==c:
        print("组成等腰三角形")
    else:
        print("组成普通三角形")
else:
    print("不能组成三角形")
