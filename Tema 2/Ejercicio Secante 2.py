def secante_tol(f, x0, x1, tol=1e-7):
    while abs(f(x1)) > tol:
        print(f"Buscando... f({x1:.6f}) = {f(x1):.6f}")
        temp = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))
        x0, x1 = x1, temp
    return x1