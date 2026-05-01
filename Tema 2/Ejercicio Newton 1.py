def newton_simple(f, df, x0, tol=0.001):
    x = x0
    while abs(f(x)) > tol:
        print(f"x actual: {x:.5f} | f(x): {f(x):.5f}")
        x = x - f(x)/df(x)
    return x