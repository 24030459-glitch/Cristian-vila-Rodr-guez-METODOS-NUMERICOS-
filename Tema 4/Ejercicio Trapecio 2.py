def f_error(x):
    return 1/x

def trapecio_error(a, b, n):
    try:
        h = (b - a) / n
        # El error ocurrirá aquí al evaluar f(0)
        suma = (f_error(a) + f_error(b)) / 2
        for i in range(1, n):
            suma += f_error(a + i * h)
        return suma * h
    except ZeroDivisionError:
        return "ERROR: División por cero. La función es discontinua en x=0."

print(trapecio_error(0, 2, 50))