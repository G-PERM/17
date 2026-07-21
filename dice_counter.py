import random
counts = [0]*6
for _ in range(100):
    counts[random.randint(0,5)] += 1
for i, c in enumerate(counts, 1):
    print(f"{i} rolled {c} times.")