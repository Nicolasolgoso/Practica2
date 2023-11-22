# Hey, aquí está mi intento de análisis estadístico en Python. Espero que funcione.

# Importar las bibliotecas necesarias
import numpy as np
from scipy import stats  

# Función para calcular la media
def calcular_media(datos):
    return np.mean(datos)

# Función para calcular la desviación estándar
def calcular_desviacion_estandar(datos):
    return np.std(datos)

# Función para hacer una prueba t de una muestra
def prueba_t_una_muestra(datos, media_nula):
    t_estadistico, valor_p = stats.ttest_1samp(datos, media_nula)
    return t_estadistico, valor_p

# Función para hacer una prueba t de dos muestras
def prueba_t_dos_muestras(datos1, datos2):
    t_estadistico, valor_p = stats.ttest_ind(datos1, datos2)
    return t_estadistico, valor_p

# Función para hacer una prueba chi-cuadrado
def prueba_chi_cuadrado(observado, esperado):
    chi_estadistico, p_value = stats.chisquare(f_obs=observado, f_exp=esperado)
    return chi_estadistico, p_value

# Función principal para correr el programa
def principal():
    print("¡Bienvenido al Programa de Análisis Estadístico!")

    # Ingresar datos experimentales
    datos = list(map(float, input("Ingresa tus datos experimentales separados por espacios: ").split()))

    # Calcular y mostrar la media
    media = calcular_media(datos)
    print(f"Media: {media}")

    # Calcular y mostrar la desviación estándar
    desviacion_estandar = calcular_desviacion_estandar(datos)
    print(f"Desviación Estándar: {desviacion_estandar}")

    # Opciones de pruebas de hipótesis
    print("\nPruebas de Hipótesis:")
    print("1. Prueba t de una muestra")
    print("2. Prueba t de dos muestras")
    print("3. Prueba chi-cuadrado")
    # Preguntar al usuario que elija una prueba de hipótesis (1/2/3)
    eleccion_prueba = int(input("Elige una prueba de hipótesis (1/2/3): "))

    if eleccion_prueba == 1:
        # Para la prueba t de una muestra
        media_nula = float(input("Ingresa la media nula para la prueba t de una muestra: "))
        t_estadistico, valor_p = prueba_t_una_muestra(datos, media_nula)
        print(f"Prueba t de una muestra: t_estadistico = {t_estadistico}, valor_p = {valor_p}")

    elif eleccion_prueba == 2:
        #Para la prueba t de dos muestras
        datos2 = list(map(float, input("Ingresa el segundo conjunto de datos para la prueba t de dos muestras: ").split()))
        t_estadistico, valor_p = prueba_t_dos_muestras(datos, datos2)
        print(f"Prueba t de dos muestras: t_estadistico = {t_estadistico}, valor_p = {valor_p}")

    elif eleccion_prueba == 3:
        #Para la prueba de chi-cuadrado
        observado = list(map(float, input("Ingresa las frecuencias observadas separadas por espacios: ").split()))
        esperado = list(map(float, input("Ingresa las frecuencias esperadas separadas por espacios: ").split()))
        chi_estadistico, valor_p = prueba_chi_cuadrado(observado, esperado)
        print(f"Prueba chi-cuadrado: chi_estadistico = {chi_estadistico}, valor_p = {valor_p}")
        
    else:
        print("Opción no válida. Saliendo del programa.")

# Ejecutar el programa
if __name__ == "__main__":
    principal()



