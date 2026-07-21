import math
while True:
    try:
        n = float(input("Enter Number: "))
        if n % 1 == 0:
            n = int(n)
        if n >= 0:
            a = math.sqrt(n)
            if a % 1 == 0:
                a = int(a)
        else:
            n *= -1
            a = math.sqrt(n)
            if a % 1 == 0:
                a = int(a)
            a = str(a) + "𝑖"
            n *= -1
        print(f"Square root of {n} is {a}.")
        break
    except ValueError:
        print("Enter real(float) numbers only.")
        continue