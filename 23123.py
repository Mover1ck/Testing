def F(n):
    if n < 15: return n
    if n >= 15: return n+F(n-1)

print(F(2025)-F(2022))