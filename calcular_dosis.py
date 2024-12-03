import numpy as np
import tifffile as tiff
from calibracion import crear_curva

def calcular_dosis(imagen_tiff, dosis_fit, valores_fit, polinomio):
    # Leer la imagen TIFF
    imagen = tiff.imread(imagen_tiff)
    
    # Asegurarse de que la imagen esté en formato de punto flotante
    imagen = imagen.astype(np.float32)
    
    # Calcular la dosis en cada punto usando el polinomio de calibración
    dosis = np.polyval(polinomio, imagen)
    
    return dosis