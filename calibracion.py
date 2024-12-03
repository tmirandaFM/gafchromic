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


#Funcion para calcular dosis por pixel 
def calcular_dosis (image, polinomio):
    """
    Calcula la dosis para cada píxel de la imagen utilizando el polinomio de calibración.

    Parámetros:
    image: np.array
        Imagen de la cual se calculará la dosis.
    polinomio: np.poly1d
        Polinomio de calibración utilizado para calcular la dosis.

    Retorna:
    np.array
        Imagen con los valores de dosis calculados para cada píxel.
    """
    dosis_por_pixel = np.polyval(polinomio, image)
    return dosis_por_pixel