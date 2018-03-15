n = int(input("Multiplicand: "))
rng = int(input("Multiplier range: "))

for multiplier in range(1, rng+1):
    print(n, 'x', multiplier, '=', n*multiplier)
