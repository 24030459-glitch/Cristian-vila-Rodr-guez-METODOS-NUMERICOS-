def secante_clasica(f, x0, x1, iters=5):
    for i in range(iters):
        f0, f1 = f(x0), f(x1)
        x_new = x1 - f1 * (x1 - x0) / (f1 - f0)
        print(f"Salto {i+1}: De {x1:.4f} a {x_new:.4f}")
        x0, x1 = x1, x_new