# 打印这个形状：

# num = input("亲输入您要的层数：")
# num = int(num)
# i = 1  # i 控制层数
#
# while i <= num: # while控制层的走向
#     j = 1
#     while j <= i:  # 控制每一层的打印操作
#         print("*",end="")   # 打印一个星号，但是不换行
#         j = j + 1
#     print() # 当每一层做完的时候，换行
#     i = i + 1

num = input("亲输入您要的层数：")
num = int(num)
i = 1  # i 控制层数
while i <= num: # while控制层的走向
    j = 1
    while j <= i:  # 控制每一层的打印操作
        print(j,"x",i,"=",(j*i),"   ",end="")   # 打印一个星号，但是不换行
        j = j + 1
    print() # 当每一层做完的时候，换行
    i = i + 1













