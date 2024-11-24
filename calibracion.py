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

def crear_curva_de_calibracion(valores_medios, dosis):
    """
    Crea una curva de calibración basada en los valores medios de píxel y los valores de dosis.

    Parámetros:
    valores_medios: list o np.array
        Lista con los valores medios de píxel para cada ROI.
    dosis: list o np.array
        Lista con los valores de dosis correspondientes para cada ROI.
    
    Retorna:
    None
    """
    if len(valores_medios) != len(dosis):
        print("El número de valores medios no coincide con el número de valores de dosis proporcionados.")
        return

    # Crear el gráfico de la curva de calibración
    plt.figure()
    plt.scatter(dosis, valores_medios, color='red', label='Datos de calibración')
    plt.plot(dosis, valores_medios, linestyle='--', color='blue', label='Curva de calibración')

    plt.xlabel("Dosis")
    plt.ylabel("Valor medio del píxel")
    plt.title("Curva de Calibración")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Guardar el gráfico en un archivo
    plt.savefig("curva_calibracion.png")
    print("Gráfico guardado como 'curva_calibracion.png'")
