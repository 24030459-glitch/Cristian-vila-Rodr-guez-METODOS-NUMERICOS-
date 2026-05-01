def biseccion(f, a, b, tol=1e-5, max_iter=100):
    print(f"{'Iter':<5} | {'a':<10} | {'b':<10} | {'m (Raíz)':<10} | {'f(m)':<10}")
    print("-" * 55)
    
    for i in range(1, max_iter + 1):
        m = (a + b) / 2
        fm = f(m)
        print(f"{i:<5} | {a:<10.6f} | {b:<10.6f} | {m:<10.6f} | {fm:<10.6f}")
        
        if abs(fm) < tol or (b - a) / 2 < tol:
            return m
        
        if f(a) * fm < 0:
            b = m
        else:
            a = m
    return m

# Ejemplo: f(x) = x^2 - 2
biseccion(lambda x: x**2 - 2, 1, 2)