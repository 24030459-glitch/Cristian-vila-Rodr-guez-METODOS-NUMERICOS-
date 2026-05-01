def biseccion_recursiva(f, a, b, tol, iteracion=1):
    c = (a + b) / 2
    print(f"Iter {iteracion}: c = {c:.6f}")
    if abs(f(c)) < tol or (b - a) / 2 < tol:
        return c
    return biseccion_recursiva(f, a, c, tol, iteracion+1) if f(a)*f(c) < 0 \
           else biseccion_recursiva(f, c, b, tol, iteracion+1)