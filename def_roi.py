import matplotlib.pyplot as plt
import cv2
import os

def seleccionar_rois(imagen):

    # Verificar si se está ejecutando en un entorno sin pantalla
    if os.environ.get('DISPLAY', '') == '':
        print('No display found. Using non-interactive backend.')
        plt.switch_backend('Agg')

    # Inicializar la lista para almacenar las ROIs
    rois = []

    # Mostrar la imagen y permitir la selección de múltiples ROIs
    while True:
        # Mostrar la imagen y permitir la selección de una ROI
        cv2.imshow("Imagen", imagen)
        roi_coords = cv2.selectROI("Imagen", imagen, fromCenter=False, showCrosshair=True)
        if roi_coords != (0, 0, 0, 0):
            x, y, w, h = roi_coords
            # Extract the actual sub-image from 'imagen'
            roi_subimage = imagen[y : y + h, x : x + w]
            rois.append(roi_subimage)

            print(f"ROI {len(rois)} seleccionada.")

        # Preguntar al usuario si quiere seleccionar otra ROI
        key = cv2.waitKey(0) & 0xFF
        if key == 27:  # Presiona 'ESC' para terminar la selección de ROIs
            break

    # Cerrar todas las ventanas abiertas
    cv2.destroyAllWindows()

    # Imprimir las ROIs seleccionadas
    mean_roi_value=[]
    
    for i, roi in enumerate(rois):
        print(f"ROI {i + 1}: {roi.shape}")
    # Imprimir las ROIs seleccionadas con su valor medio de píxel
    for i, roi in enumerate(rois):
        mean_val = roi.mean()
        mean_roi_value.append(mean_val)
        print(f"ROI {i + 1}: {roi.shape}, Valor medio de píxel: {mean_val}")
    return mean_roi_value