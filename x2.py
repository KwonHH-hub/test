import os
print("hello python hello")
dir = os.getcwd()
print(dir)
f = open('./myname.txt', 'r+')

x = f.readline()
print("i'm here : ", x)
if "Gildong" in x:
    print("if문 들어오니")
    x.replace("Gildong", "DangMoo", 1)
f.close()