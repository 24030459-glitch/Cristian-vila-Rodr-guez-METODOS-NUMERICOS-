import numpy as np
import matplotlib.pyplot as plt

def jacobi_graficado(A, b, it=20):
    n = len(b)
    x = np.zeros(n)
    errores = []
    
    for k in range(it):
        x_new = (b - (np.dot(A, x) - np.diag(A)*x)) / np.diag(A)
        errores.append(np.linalg.norm(x_new - x))
        x = x_new
        
    plt.plot(range(it), errores, marker='o')
    plt.title("Error por iteración (Jacobi)")
    plt.xlabel("Iteración")
    plt.ylabel("Error")
    plt.grid()
    plt.show()

A = np.array([[5, -1, 1], [2, 4, 0], [1, 1, 5]], dtype=float)
b = np.array([10, 12, -1], dtype=float)
jacobi_graficado(A, b)