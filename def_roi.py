def seleccionar_rois(imagen):
    import matplotlib.pyplot as plt
    import cv2
    # Convertir de BGR a RGB para asegurarse de que los colores sean correctos
    if len(imagen.shape) == 3:
        imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    else:
        imagen_rgb = imagen  # Si es en escala de grises, no se necesita conversión

    # Inicializar la lista para almacenar las ROIs
    rois = []

    # Mostrar la imagen y permitir la selección de múltiples ROIs
    while True:
        # Mostrar la imagen y permitir la selección de una ROI
        cv2.imshow("Imagen", imagen_rgb)
        roi = cv2.selectROI("Imagen", imagen_rgb, fromCenter=False, showCrosshair=True)

        # Si se seleccionó un área válida (no todas las coordenadas son cero)
        if roi != (0, 0, 0, 0):
            x, y, w, h = roi
            roi_imagen = imagen_rgb[int(y):int(y + h), int(x):int(x + w)]
            rois.append(roi_imagen)
            print(f"ROI {len(rois)} seleccionada.")

        # Preguntar al usuario si quiere seleccionar otra ROI
        key = cv2.waitKey(0) & 0xFF
        if key == 27:  # Presiona 'ESC' para terminar la selección de ROIs
            break

    # Cerrar todas las ventanas abiertas
    cv2.destroyAllWindows()

    for i, roi_imagen in enumerate(rois):
        ventana_nombre = f"ROI {i+1}"
        cv2.imshow(ventana_nombre, roi_imagen)

    for i, roi_imagen in enumerate(rois):
        plt.figure(figsize=(10, 5))
        for canal, color in enumerate(['b', 'g', 'r']):  # Colores para los canales BGR
            histograma = cv2.calcHist([roi_imagen], [canal], None, [256], [0, 256])
            plt.plot(histograma, color=color)
            plt.xlim([0, 256])
        plt.title(f'Histogramas de los canales BGR de ROI {i+1}')
        plt.xlabel('Intensidad de píxel')
        plt.ylabel('Número de píxeles')
        plt.legend(['Canal Azul', 'Canal Verde', 'Canal Rojo'])
        plt.savefig(f'histograma_roi_{i+1}.png')
        plt.close()

    return rois

