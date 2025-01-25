import numpy as np
import cv2 
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from read import leer
from def_roi import seleccionar_rois  # Importar la función específica
from calibracion import crear_curva_de_calibracion_pol, calcular_dosis_limitado_tiff

imagen_calibracion = "./cdc.tif"

image = leer(imagen_calibracion)

# Dosis correspondientes a cada ROI
dosis = np.array([0, 100, 150, 200, 250, 300, 350, 400, 500])

# Crear rois para calibración
rois = seleccionar_rois(image)

# Calcular los valores medios de píxel para cada ROI
#valores_medios = calcular_valores_medios_rois(rois)

# Ajustar un poco la ventana de intensidades permitidas
do_min = np.min(rois) * 0.9
do_max = np.max(rois) * 1.1

# Crear la curva de calibración
polinomio, dosis_fit, valores_fit = crear_curva_de_calibracion_pol(dosis, rois)


imagen_a_analizar=leer("./e_normal.tif")
# Inicializar un array para almacenar la dosis por píxel (float)

mapa_dosis = np.zeros_like(imagen_a_analizar, dtype=float)

# Si la imagen es en **grayscale** (2D array), shape = (height, width)
# Si la imagen es color (por ejemplo, RGB), shape = (height, width, 3).
# Ajustar la siguiente parte según corresponda.
# ----------------------------------------------------------------------------
# Supongamos que es GRAYSCALE (1 canal).
# ----------------------------------------------------------------------------

# Calcular la dosis para cada píxel de la imagen
for i in range(imagen_a_analizar.shape[0]):
    for j in range(imagen_a_analizar.shape[1]):
        pixel_value = imagen_a_analizar[i, j]  # single-channel value
        if do_min < pixel_value < do_max:
            mapa_dosis[i, j] = np.polyval(polinomio, pixel_value)

# Si tu imagen es RGB (3 canales), necesitarás decidir cómo calcular 'pixel_value',
# por ejemplo, usando una media o un canal específico:
# pixel_value = np.mean(imagen_a_analizar[i, j, :])

# Guardar el mapa de dosis como una imagen
# NOTA: cv2.imwrite espera por defecto una imagen de 8 bits (0..255) o 16 bits sin signo.
#       Si 'mapa_dosis' contiene floats o valores muy grandes, se requiere normalización.
#       Aquí lo convertimos a 16 bits por ejemplo (ajustar según tus rangos).

mapa_dosis_16 = cv2.normalize(mapa_dosis, None, alpha=0, beta=65535, 
                              norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_16U)
cv2.imwrite('mapa_dosis.tiff', mapa_dosis_16)

# Crear la figura con Plotly
fig = go.Figure()

# 1) Añadir la imagen original como un heatmap
#   - Si es grayscale y 2D, no hay axis=2. 
#   - Si tu imagen era RGB, para la visualización en un solo canal se hace la media en axis=2.
#   Aquí asumiremos grayscale.
fig.add_trace(go.Heatmap(
    z=imagen_a_analizar,       # Grayscale original
    colorscale='gray',
    colorbar=dict(title='Intensidad Original'),
    visible=True
))

# 2) Añadir el mapa de dosis calculado
fig.add_trace(go.Heatmap(
    z=mapa_dosis,  # O 'mapa_dosis_16' si quieres ver la versión entera
    colorscale='Jet',
    colorbar=dict(title='Dosis Calculada'),
    visible=False
))

# Configurar el layout para permitir cambiar entre imágenes
fig.update_layout(
    title='Imagen Original y Dosis Calculada',
    updatemenus=[
        dict(
            type="buttons",
            x=1.05,
            y=0.9,
            buttons=[
                dict(
                    label="Imagen Original",
                    method="update",
                    args=[{"visible": [True, False]}]
                ),
                dict(
                    label="Dosis Calculada",
                    method="update",
                    args=[{"visible": [False, True]}]
                )
            ]
        )
    ]
)

fig.show()

print("Mapa de dosis guardado exitosamente.")
