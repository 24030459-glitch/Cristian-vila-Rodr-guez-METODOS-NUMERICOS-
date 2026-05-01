def cp(t):
    return 28 + 0.002 * t + 0.00001 * t**2

def simpson_term(a, b, n):
    h = (b - a) / n
    res = cp(a) + cp(b)
    for i in range(1, n):
        res += (4 if i % 2 != 0 else 2) * cp(a + i * h)
    return (h / 3) * res

print(f"Delta H: {simpson_term(300, 500, 10):.6f} kJ/mol")