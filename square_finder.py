import math
while True:
    try:
        n = int(input("Enter Number: "))
        o = n
        if n >= 0:
            if math.sqrt(n) == int(math.sqrt(n)):
                print(f"{n} is a perfect square.")
                break
            else:
                while math.sqrt(n) != int(math.sqrt(n)):
                    n += 1
                print(f"{n} is the next perfect square after {o}.")
                break
        else:
            m = abs(n)
            if math.sqrt(m) == int(math.sqrt(m)):
                print(f"{n} is a perfect imaginary square.")
                break
            else:
                while math.sqrt(m) != int(math.sqrt(m)):
                    m -= 1
                n = m * -1
                print(f"{n} is the next perfect imaginary square after {o}.")
                break
    except ValueError:
        print("Enter a integer only.")
        continue