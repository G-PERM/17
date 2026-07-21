import sys, random
from colorama import init
init(autoreset=True)
B = "\033[1m"
I = "\033[1;3m"
R = "\033[0m"
print(f"{B}\nWelcome to Dice Casino\n{R}\nDifficulty levels:\nBreeze (Enter 1 to choose)\nDrift (Enter 2 to choose)\nFloat (Enter 3 to choose)\nGlide (Enter 4 to choose)\nGustwave (Enter 5 to choose)\nStormburst (Enter 6 to choose)\nHypergale (Enter 7 to choose)\n")
w = l = t = 0
def i():
    print("\nEnter 1, 2, 3, 4, 5, 6, or 7 to set difficulty.\n")
def f():
    print("\nInvalid guess. Please enter an integer between 1 and 6.\n")
def m():
    print("\nType either Y/y or N/n.\n")
def s(a, p, y, n, z, v, r, t):
    p += n
    print(f"{y}{a}\nScore: {p}")
    if p < z:
        z = p
        print(f"New Low Score: {z}")
    elif p > v:
        v = p
        print(f"New High Score: {v}")
    print()
    r += 1
    t += 1
    return p, y, z, v, r, t
def q(n):
    if n == int(n):
        n = int(n)
    else:
        n = round(n, 8)
    return n
def k(w, l, t, v, z, p, F=False):
    T = "Final stats" if F else "Stats"
    e = str(q(w / t * 100)) + "%"
    h = str(q(l / t * 100)) + "%"
    print(
        f"{B}\n{T}:\nWins: {w}\nWin%: {e}\nLosses: {l}\nLoss%: {h}\nTotal Rounds: {t}\nHighest score: {v}\nLowest score: {z}\nFinal score: {p}\n{R}")
    print(f"{I}Thanks for Playing!{R}")
def j(n):
    if n == 1:
        print(f"{B}\n\n\nEND OF FILE ERROR\nEXITING...{R}")
    else:
        print(f"{B}\n\n\nEXITING...{R}")
    if t == 0:
        print(f"{I}Thanks for Playing!{R}")
    else:
        k(w, l, t, v, z, p, F=True)
    sys.exit()
def u():
    while True:
        try:
            c = input("Continue(Y/y or N/n): \n").strip()
            if c in ("Y", "y", "N", "n"):
                break
            else:
                m()
                continue
        except (ValueError):
            m()
            continue
        except (EOFError):
            j(1)
        except (KeyboardInterrupt):
            j(2)
    if c == "Y" or c == "y":
        print()
        return True
    else:
        k(w, l, t, v, z, p)
        return False
while True:
    try:
        o = int(input("Select Difficulty Level: "))
        if 1 <= o <= 7:
            d = [5, 10, 15, 20, 25, 50, 100]
            x = d[o - 1]
            print()
            break
        else:
            i()
            continue
    except (ValueError):
        i()
        continue
    except (EOFError):
        j(1)
    except (KeyboardInterrupt):
        j(2)
while True:
    try:
        a = random.randint(1,6)
        g = int(input("Guess: "))
        if 1 <= g <= 6:
            if a == g:
                if t == 0:
                    p = 100
                    z = p
                    v = p
                    print(f"You won!\nDice rolled the same:{a}")
                    print(f"Score: {p}\n")
                    w += 1
                    t += 1
                else:
                    p, y, z, v, w, t = s(a, p, "You won!\nDice rolled the same:", 100, z, v, w, t)
                b = u()
                if b:
                    continue
                else:
                    break
            else:
                if t == 0:
                    p = -x
                    z = p
                    v = p
                    print(f"Better luck next time!\nDice rolled: {a}")
                    print(f"Score: {p}\n")
                    l += 1
                    t += 1
                else:
                    p, y, z, v, l, t = s(a, p, "Better luck next time!\nDice rolled:", -x, z, v, l, t)
                b = u()
                if b:
                    continue
                else:
                    break
        else:
            f()
            continue
    except (ValueError):
        f()
        continue
    except (EOFError):
        j(1)
    except (KeyboardInterrupt):
        j(2)