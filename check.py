n1, n2 = 0, 1
count = 0

n = int(input("enter the number for fibonacci"))

if n<= 0:
    print("wrong value")
elif n == 1:
    print(n1)
    print(n2)
else:
    while count < n:
        
        n3 = n1 +n2
        n1 = n2
        n2 = n3
        count = count + 1
        print(n3)
        print(n3)
