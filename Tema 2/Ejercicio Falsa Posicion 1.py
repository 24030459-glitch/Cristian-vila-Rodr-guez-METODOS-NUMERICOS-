def falsa_pos_error(f, a, b, tol):
    x_ant = a
    for i in range(1, 20):
        x = b - (f(b)*(a-b))/(f(a)-f(b))
        error = abs((x - x_ant) / x) * 100 if x != 0 else 0
        print(f"i:{i} | x:{x:.5f} | Error Relativo: {error:.2f}%")
        if abs(f(x)) < tol: break
        if f(a)*f(x) < 0: b = x
        else: a = x
        x_ant = x