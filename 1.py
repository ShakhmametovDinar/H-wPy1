# Задача 2
a=int(input("Введите число: "))
c = 0

while(a>0):
    b=a%10
    a/=10
    c+=b
print(int(c))
