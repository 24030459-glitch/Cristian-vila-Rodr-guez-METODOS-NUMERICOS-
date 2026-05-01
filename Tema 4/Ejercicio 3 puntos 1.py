import math
def T(x): return math.exp(-x**2) * math.cos(x)
x0, h = 1.0, 0.01
aprox = (T(x0 + h) - T(x0 - h)) / (2 * h)
print(f"Valor aproximado: {aprox:.10f}")