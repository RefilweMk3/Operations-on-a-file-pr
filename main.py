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