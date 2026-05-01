def falsa_pos_mejorada(f, a, b, tol):
    fa, fb = f(a), f(b)
    for i in range(50):
        x = (a*fb - b*fa) / (fb - fa)
        fx = f(x)
        print(f"Punto calculado: {x:.6f}")
        if abs(fx) < tol: return x
        if fa * fx < 0:
            b, fb = x, fx
            fa /= 2 # Ajuste para evitar que 'a' se estanque
        else:
            a, fa = x, fx
            fb /= 2