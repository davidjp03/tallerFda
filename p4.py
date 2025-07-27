import random

def calculate_pi_monte_carlo(n=1000000):
    inside_circle = 0
    for _ in range(n):
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1
    return (inside_circle / n) * 4

print("Estimación de Pi:", calculate_pi_monte_carlo(10))