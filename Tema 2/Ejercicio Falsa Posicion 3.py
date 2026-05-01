def falsa_pos_limite(f, a, b, max_it=15):
    res = []
    for _ in range(max_it):
        x = b - (f(b)*(a-b))/(f(a)-f(b))
        res.append(x)
        if f(a)*f(x) < 0: b = x
        else: a = x
    print("Flujo de aproximaciones:", [round(r, 4) for r in res])
    