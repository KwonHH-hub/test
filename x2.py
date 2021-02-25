import os
print("hello python hello")
dir = os.getcwd()
print(dir)
f = open('./myname.txt', 'r+')
f.write('x')
x = f.readline()
if 'Gildong' in x:
    x.replace('Gildong', 'DangMoo')
f.close()