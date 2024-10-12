number=int(input("Enter data:"))
n1=number//10000
n2=number//1000 % 10
n3=number // 100 % 10
n4=number % 100 // 10
n5=number % 10
print(n5)
print(n4)
print(n3)
print(n2)
print(n1)