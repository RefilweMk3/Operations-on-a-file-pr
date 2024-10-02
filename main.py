print("Hey there welcome to reading py files in different ways")
file=open("ref.txt","r")
print(file.read(8))
file.close()

file=open("ref.txt","r")
print(file.readline())
file.close()

file=open("ref.txt","r")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

file=open("ref.txt","r")
print(file.readlines())
file.close()

file=open("ref.txt","r")
for x in file:
    print(x)
file.close

f1=open("main.txt","r")
f2=open("py.txt","w")

for line in f1.readlines():
    if not(line.startswith('Coding')):
        f2.write(line)
f1.close()
f2.close()

with open("ref.txt","w") as f:
    f.write("Hey there \n how are u doing today")
f.close
with open("ref.txt","r")as f:
    data = f.readlines()
    for line in data:
        word = line.split()
        print(word)
f.close()

#file=open("kg.txt","x")
#file.write("sample file")
#file.close()

#import os
#os.remove("kg")
#os.rmdir("kg")