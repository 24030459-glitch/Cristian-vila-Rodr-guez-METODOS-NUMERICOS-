def newton_auto_derivar(f, x0, h=1e-5):
    x = x0
    for i in range(10):
        df_num = (f(x + h) - f(x)) / h # Definición de derivada
        x = x - f(x) / df_num
        print(f"Iteración {i+1}: x = {x:.6f}")
    return x