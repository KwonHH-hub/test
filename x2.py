import os
print("hello python hello")
dir = os.getcwd()

f = open(dir + 'myname.txt', 'r+')
x = f.readline()
if 'Gildong' in x:
    x.replace('Gildong', 'DangMoo')
f.close()