print("Write the number of soldiers")
a=int(input())
b=[]
for i in range(1, a//4):
    if a%(i*i)==0:
        b.append(i)
print(max(b)*max(b))