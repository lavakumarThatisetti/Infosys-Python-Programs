#print(len(dir(__builtins__)))
#print(help(max))

i=input("enter the n value")
num=int(i)
print(num)
sum=0;
for i in range(num):
    sum=sum+i
print(sum)
a=0;
b=1;
for i in range(num):
    c=a+b;
    print(c,end=",")
    a=b;
    b=c;
