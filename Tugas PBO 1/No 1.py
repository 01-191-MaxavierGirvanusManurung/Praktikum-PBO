n = int(input("Height : "))

for i in range (n):
    for j in range(n-i):
        print(' ', end = "")
    for k in range(i*2+1):
        print('*', end = "")
    print()
