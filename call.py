def sum(a):
    i = 1
    while i <= a:
        j = 1
        while j <= i:
            print(j, "x", i, "=", (j * i), "   ", end="")
            j = j + 1
        print()
        i = i + 1
s=int(input("请输入一个数："))
sum(s)
