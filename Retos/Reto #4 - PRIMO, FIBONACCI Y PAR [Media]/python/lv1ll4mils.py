import math

# función para validar si es primo
def es_primo(n: int) -> bool:
    if n <= 1:
        return False

    for i in range(2, int(n**0.5) +1):
        if n % i == 0:
            return False

    return True


# funciones para validar si es fibonacci
def es_cuadrado_perfecto(x: int) -> bool:
    s = int(math.isqrt(x))
    return s * s == x

def es_fibonacci(n: int) -> bool:
    return es_cuadrado_perfecto(5 * n * n + 4) or es_cuadrado_perfecto(5 * n * n - 4)


# función para validar si es primo
def es_par(n: int) -> bool:
    return n % 2 == 0


# registrar el número a verificar
validar_numero = int(input("Ingresa un número para validar: "))


# crear variables a cada validador
primo = es_primo(validar_numero)
fibonacci = es_fibonacci(validar_numero)
par = es_par(validar_numero)

# variabe de inicio en la verificación
mensaje = f"{validar_numero} "

#bucles para verificar cada variable
if primo:
    mensaje += "es primo, "
else:
    mensaje += "no es primo, "

if fibonacci:
    mensaje += "fibonacci "
else:
    mensaje += "no es fibonacci "

if par:
    mensaje += "y es par"
else:
    mensaje += "y es impar"

# salida de mensaje final
print(mensaje)