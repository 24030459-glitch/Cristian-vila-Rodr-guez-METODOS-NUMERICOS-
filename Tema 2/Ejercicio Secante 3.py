import math
def secante_trig(f, x0, x1):
    for i in range(6):
        x2 = x1 - (f(x1)*(x1-x0)) / (f(x1)-f(x0))
        print(f"Iter {i}: Aproximación = {x2:.8f}")
        x0, x1 = x1, x2