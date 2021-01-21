i=9
while i >= 1: # while控制层的走向
    j = 1
    while j <= i:  # 控制每一层的打印操作
        print(j,"x",i,"=",(j*i),"   ",end="")   # 打印一个星号，但是不换行
        j = j + 1
    i = i - 1
    print()  # 当每一层做完的时候，换行
