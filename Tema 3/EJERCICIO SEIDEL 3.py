def gs_con_log(A, b, it=10):
    n = len(b)
    x = [0.0] * n
    with open("resultado_gs.txt", "w") as f:
        f.write("Log de iteraciones Gauss-Seidel\n")
        for k in range(it):
            for i in range(n):
                s = sum(A[i][j] * x[j] for j in range(n) if i != j)
                x[i] = (b[i] - s) / A[i][i]
            f.write(f"Iteración {k+1}: {str(x)}\n")
    print("Historial guardado en resultado_gs.txt")

A = [[4, 1, 2], [3, 5, 1], [1, 1, 3]]
b = [4, 7, 3]
gs_con_log(A, b)