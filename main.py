import numpy as np
import cv2 
import matplotlib.pyplot as plt
from read import leer
from def_roi import seleccionar_rois  # Importar la función específica
from calibracion import crear_curva_de_calibracion_pol, calcular_valores_medios_rois
path = "./cdc.tif"

image = leer(path)

# Dosis correspondientes a cada ROI
dosis = np.array([0, 100, 150, 200, 250, 300,350,400,500])

rois = seleccionar_rois(image)


# Calcular los valores medios de píxel para cada ROI
valores_medios = calcular_valores_medios_rois(rois)

# Crear la curva de calibración
polinomio, dosis_fit, valores_fit = crear_curva_de_calibracion_pol(dosis, valores_medios)

# Leer la imagen TIFF para calcular la dosis
image_to_analyze = leer("./cdc.tif")

# Calcular la dosis para cada píxel de la imagen
dosis_por_pixel = np.polyval(polinomio, image_to_analyze)
