import os
print("hello python hello")
dir = os.getcwd()
print(dir)
f = open('./myname.txt', 'r+')

x = f.readline()
print("i'm here : ", x)
if "Gildong" in x:

    x.replace("Gildong", "DangMoo")
f.close()