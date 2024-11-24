import numpy as np
import cv2 
import matplotlib.pyplot as plt
from read import leer
from def_roi import seleccionar_rois  # Importar la función específica
from calibracion import calcular_valores_medios_rois, crear_curva_de_calibracion  # Importar las funciones específicas
path = "./cdc.tif"

image = leer(path)

# Dosis correspondientes a cada ROI
dosis = np.array([0, 100, 150, 200, 250, 300,350,400,500])

rois = seleccionar_rois(image)


# Calcular los valores medios de píxel para cada ROI
valores_medios = calcular_valores_medios_rois(rois)

# Crear la curva de calibración
crear_curva_de_calibracion(valores_medios, dosis)

cv2.waitKey(0)
cv2.destroyAllWindows()

