import os
print("hello python hello")
dir = os.getcwd()
print(dir)
f = open('./myname.txt', 'a')

x = f.readline()
print("i'm here : ", x)
if "Gildong" in x:
    print("if문 들어오니")
    f.write(x.replace("Gildong", "DangMoo"))
f.close()