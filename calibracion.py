import numpy as np
import matplotlib.pyplot as plt
def calcular_valores_medios_rois(rois):
    
    """
    Calcula el valor medio de píxel de cada ROI.

    Parámetros:
    rois: list o array de np.array
        Lista o array que contiene las imágenes de cada ROI.

    Retorna:
    list
        Lista con los valores medios de píxel de cada ROI.
    """
    valores_medios = [np.mean(roi) for roi in rois]
    return valores_medios

def crear_curva_de_calibracion_pol(dosis, valores_medios):
    """
    Crea una curva de calibración polinómica basada en los valores medios de píxel y los valores de dosis.

    Parámetros:
    dosis: list o np.array
        Lista con los valores de dosis correspondientes para cada ROI.
    valores_medios: list o np.array
        Lista con los valores medios de píxel para cada ROI.
    
    Retorna:
    None
    """
    if len(valores_medios) != len(dosis):
        print("El número de valores medios no coincide con el número de valores de dosis proporcionados.")
        return

    # Ajustar un polinomio de grado 3 a los datos
    coeficientes = np.polyfit(dosis, valores_medios, 3)
    polinomio = np.poly1d(coeficientes)

    # Generar valores de dosis para la curva
    dosis_fit = np.linspace(min(dosis), max(dosis), 500)
    valores_fit = polinomio(dosis_fit)

    return polinomio, dosis_fit, valores_fit

    # Crear el gráfico de la curva de calibración
    plt.figure()
    plt.scatter(dosis, valores_medios, color='red', label='Datos de calibración')
    plt.plot(dosis_fit, valores_fit, linestyle='--', color='blue', label='Curva de ajuste polinómico')

    plt.xlabel("Dosis")
    plt.ylabel("Valor medio del píxel")
    plt.title("Curva de Calibración (Ajuste Polinómico)")
    plt.legend()
    plt.grid(True)
    plt.savefig("curva_calibracion_ajuste_polinomico.png")
    print("Gráfico guardado como 'curva_calibracion_ajuste_polinomico.png'")
    plt.show()