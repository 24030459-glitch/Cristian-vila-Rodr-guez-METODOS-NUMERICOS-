def newton_seguro(f, df, x0, max_it=10):
    xn = x0
    for i in range(max_it):
        try:
            m = df(xn)
            if abs(m) < 1e-10: raise ZeroDivisionError
            xn = xn - f(xn)/m
            print(f"Paso {i}: x = {xn:.4f}")
        except ZeroDivisionError:
            print("Error: Derivada nula. Intenta con otro punto inicial.")
            break