import numpy as np
import cv2 
import matplotlib.pyplot as plt
from read import leer
from def_roi import seleccionar_rois  # Importar la función específica

path="./cdc.tif"

image=leer(path)

roi=seleccionar_rois(image)


# Esperar a que se presione una tecla para cerrar todas las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()