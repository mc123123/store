names=[
    ["曹操","56","男","106","IBM",500,"50"],
    ["大乔","19","女","230","微软",501,"60"],
    ["小乔","19","女","210","Oracle",600,"60"],
    ["许褚","45","男","230","Tencent",700,"10"]
]
# pay=0
# for i in range(0,4):
#     pay=pay+int(names[i][1])
# pay=pay/4
# print(pay)
# names.append(["刘备","45","男","220","alibaba",500,"30"])
# man="男"
# woman="女"
# nan=0
# nv=0
# for i in range(0,5):
#    if man==names[i][2]:
#       nan=nan+1
#    else:
#        nv=nv+1
# print("男",nan,"人","女",nv,"人")
#
# pay=0
# for i in range(0,4):
#     pay=pay+names[i][5]
# pay=pay/4
# print(pay)
#
# pay=0
# for i in range(0,4):
#     pay=pay+names[i][1]
# pay=pay/4
# print(pay)
names.append(["刘备","45","男","220","alibaba",500,"30"])
# print(names)
a=0
b=0
c=0
d=0
for i in range(0,5):
 if int(names[i][6])==50:
     a=a+1
 elif int(names[i][6])==60:
     b=b+1
 elif int(names[i][6])==10:
     c=c+1
 elif int(names[i][6])==30:
     d=d+1
print("50部门的有",a,"个人"," ",
      "60部门的有",b,"个人"," ",
      "10部门的有",c,"个人"," ",
      "30部门的有",d,"个人")