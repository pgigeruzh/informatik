# 1. Die Lehrerin möchte, dass sie die Zahlen von 1 bis 1000 aufschreiben.
for i in range(1000):
	print(i+1)

# 2. Die Lehrerin verlangt nun, dass sie von 1000 wieder rückwärts auf 1 zählen.
for i in range(1000):
	print(1000-i)

# 3. Nun möchte die Lehrerin auch noch, dass sie die 7er-Reihe bis 1000 (1x7, 2x7, 3x7…) aufschreiben. 
for i in range(int(1000/7)):
    print((i+1) * 7)