num=int(input("Enter number of names: "))
names=[]
for i in range(num):
    names.append(str(input("Enter name: ")))
print(" ".join(names))