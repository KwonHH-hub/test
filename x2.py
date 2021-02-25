import os
print("hello python hello")
dir = os.getcwd()
print(dir)
f = open('./myname.txt', 'r+')

while 1:
    line = f.readline()
    print(line)
    if "Gildong" in line:
        f.write(line.replace("Gildong", "DangMoo"))
    else:
        f.write(line)
    if not line:
        break
# f.close()
# print("i'm here : ", x)
# if "Gildong" in x:
#     print("if문 들어오니")
#     f.write(x.replace("Gildong", "DangMoo"))
#     f.close()