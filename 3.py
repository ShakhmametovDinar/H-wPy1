# Задача 6

a=int(input("Введите число: "))
d=0
f=0

b=a/1000
c=a%1000
b=int(b)
c=int(c)

while(b>0):
    d=b%10
    b/=10
    f+=d  
while(c>0):
    d=c%10
    c/=10
    f+=d 
     
if(b==c):
    print("ДА")
else:
    print("НЕТ")
