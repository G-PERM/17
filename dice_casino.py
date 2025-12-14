import random
print("\033[1m\nWelcome to Dice Casino\n\033[0m")
print("Difficulty levels:")
print("Breeze (Enter 1 to choose)")
print("Drift (Enter 2 to choose)")
print("Float (Enter 3 to choose)")
print("Glide (Enter 4 to choose)")
print("Gustwave (Enter 5 to choose)")
print("Stormburst (Enter 6 to choose)")
print("Hypergale (Enter 7 to choose)\n")
w = 0
l = 0
tg = 0
while True:
    try:
        o = int(input("Select Difficulty Level: "))
        if 0 <= o - 1 <= 6:
            diff = [5, 10, 15, 20, 25, 50, 100]
            x = diff[o - 1]
            print()
            break
        else:
            print("Enter 1, 2, 3, 4, 5, 6, or 7 to set difficulty.\n")
            continue
    except ValueError:
        print("Enter 1, 2, 3, 4, 5, 6, or 7 to set difficulty.\n")
        continue
while True:
    try:
        a = random.randint(1,6)
        g = int(input("Guess: "))
        if 1 <= g <= 6:
            if a == g:
                if t == 0:
                    p = 100
                    
                p += 100
                w += 1
                tg += 1
                print("You won!")
                print("Dice rolled the same:", a)
                print(f"Score: {p}")
                if p > hs:
                    hs = p
                    print(f"New High Score: {hs}\n")
                else:
                    print()
                while True:
                    c = input("Continue(Yes or No): \n")
                    if c in ("Yes", "No"):
                        break
                    else:
                        print("Say either Yes or No.\n")
                        continue
                if c == "Yes":
                    print()
                    continue
                elif c == "No":
                    wp = str(w/tg * 100) + "%"
                    lp = str(l/tg * 100) + "%"
                    print(f"\033[1m\nStats:\nWins: {w}\nWin%: {wp}\nLosses: {l}\nLoss%: {lp}\nTotal Rounds: {tg}\nHighest score: {hs}\nLowest score: {56 bn}\nFinal score: {p}\n\033[0m")
                    print("\033[1;3mThanks for Playing!\033[0m")
                    break
            else:
                p -= x
                l += 1
                tg += 1
                print("Better luck next time.")
                print("Dice rolled:", a)
                print(f"Score: {p}")
                if p < ls:
                    ls = p
                    print(f"New Low Score: {ls}\n")
                else:
                    print()
                continue
        else:
            print("Invalid guess. Please enter an integer between 1 and 6.\n")
            continue         
    except ValueError:
        print("Invalid guess. Please enter an integer between 1 and 6.\n")
        continue