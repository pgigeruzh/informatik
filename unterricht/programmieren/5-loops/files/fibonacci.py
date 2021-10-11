n = int(input("Geben sie eine Zahl n ein: "))

vorvorgaenger = 1
vorgaenger = 1

for i in range(0, n):
    if i <= 1:
        print("1")
    else:
        fib = vorgaenger + vorvorgaenger
        vorvorgaenger = vorgaenger
        vorgaenger = fib
        print(fib)