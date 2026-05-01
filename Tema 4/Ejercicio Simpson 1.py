import math

def p(t):
    return t**2 * math.sin(t) + 50

def simpson_ideal(a, b, n):
    h = (b - a) / n
    suma = p(a) + p(b)
    for i in range(1, n):
        if i % 2 != 0:
            suma += 4 * p(a + i * h)
        else:
            suma += 2 * p(a + i * h)
    return (h / 3) * suma

print(f"Energía total: {simpson_ideal(0, 10, 20):.6f} J")