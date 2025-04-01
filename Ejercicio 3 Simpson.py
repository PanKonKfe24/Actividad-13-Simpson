"""
           Autor:
   Juan Pablo Buitrago Rios
   juanybrisagames@gmail.com
   Version 2.0 : 30/03/2025 11:50pm

"""

import numpy as np
import matplotlib.pyplot as plt

#Ejercicio 3

def simpson_rule(f, a, b, n):
    """Aproxima la integral de f(x) en [a, b] usando la regla de Simpson."""
    if n % 2 == 1:
        raise ValueError("El número de subintervalos (n) debe ser par.")
    
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)  # Puntos del intervalo
    fx = f(x)  # Evaluamos la función en esos puntos
    
    # Regla de Simpson
    integral = (h / 3) * (fx[0] + 2 * np.sum(fx[2:n:2]) + 4 * np.sum(fx[1:n:2]) + fx[n])
    
    return integral

# Función de ejemplo
def funcion(x):
    return -100 * x  # Cambiar esta función según el problema


# Parámetros de integración
k = 0.5  # Conductividad térmica en W/m·K
a, b = 0, 2  # Límites de integración (posición x1 y x2)
n_valores = [6, 10, 20, 30]  # Número de subintervalos (debe ser par)

# Solución analítica
solucion_analitica =  k * (-100 * (b**2 / 2 - a**2 / 2))

# Mostrar solución analítica
print(f"Solución analítica: W = {solucion_analitica:.6f} J\n")

# Encabezado de la tabla
print("n\tAproximación (C)\tError absoluto")
print("-" * 40)

# Calcular y mostrar resultados para cada n
for n in n_valores:
    # Aproximación de la integral
    resultado = k * simpson_rule(funcion, a, b, n)
    error = abs(solucion_analitica - resultado)
    print(f"{n}\t{resultado:.6f}\t\t{error:.6e}")
    # Gráfica de la función y la aproximación con la regla de Simpson
    x_vals = np.linspace(a, b, 100)
    y_vals = funcion(x_vals)

    plt.plot(x_vals, y_vals, label=r"$\frac{dT}{dx} = -100x$", color="blue")
    plt.fill_between(x_vals, y_vals, alpha=0.3, color="cyan", label="Área aproximada")
    plt.scatter(np.linspace(a, b, n+1), funcion(np.linspace(a, b, n+1)), color="red", label="Puntos de interpolación")
    plt.xlabel("x (m)")
    plt.ylabel("dT/dx")
    plt.legend()
    plt.title("Aproximación de la integral con la regla de Simpson")
    plt.grid()

    # Guardar la figura
    plt.savefig(f"simpson{n}.png")
    plt.show()



# Mostrar resultado
print(f"La aproximación de la integral usando la regla de Simpson es: {resultado}")

