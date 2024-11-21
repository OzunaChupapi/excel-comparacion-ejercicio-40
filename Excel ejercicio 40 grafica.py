# Parámetros del problema
m = 5         # masa en kg
g = 9.81      # gravedad en m/s^2
k = 0.05      # constante en kg/m
dt = 0.1      # paso de tiempo en segundos
t_max = 15    # tiempo máximo en segundos

# Inicialización de tiempo y velocidad
time = [0]    # Lista para los valores de tiempo
v = [0]       # Lista para los valores de velocidad

# Método de Euler
while time[-1] < t_max:
    # Calcular la derivada dv/dt manualmente sin pow() ni **
    dv_dt = -g - (k / m) * (v[-1] * v[-1] ** 2)  # Esto es lo mismo que v[-1]**2
    # Actualizar la velocidad y el tiempo
    v.append(v[-1] + dv_dt * dt)
    time.append(time[-1] + dt)

# Mostrar resultados
print(f"{'Tiempo (s)':<12}{'Velocidad (m/s)':<20}")
print("=" * 30)
for t, vel in zip(time, v):
    print(f"{t:<12.2f}{vel:<20.6f}")
