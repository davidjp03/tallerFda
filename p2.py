def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# 1. Generar primeros 100 números de Fibonacci
fib = fibonacci(10)

primos = [n for n in fib if es_primo(n)]

primo_max = max(primos) if primos else None

suma_digitos = 0

for d in str(primo_max):
    suma_digitos += int(d)
    
print("Primo más grande:", primo_max)
print("Suma de sus dígitos:", suma_digitos)    