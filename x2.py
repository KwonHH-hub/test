import os
print("hello python hello")
dir = os.getcwd()
print(dir)
f = open('./myname.txt', 'r')
ff = open('./myname2.txt', 'w')

while 1:
    line = f.readline()
    print(line)
    if "Gildong" in line:
        ff.write(line.replace("Gildong", "DangMoo"))
    elif "115200" in line:
        ff.write(line.replace("1152000", "9600"))
    else:
        ff.write(line)
    if not line:
        break
f.close()
ff.close()


# f.close()
# print("i'm here : ", x)
# if "Gildong" in x:
#     print("if문 들어오니")
#     f.write(x.replace("Gildong", "DangMoo"))
#     f.close()