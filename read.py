def leer(path):
    import cv2
    import matplotlib.pyplot as plt
    import numpy as np

    image = cv2.imread(path, cv2.IMREAD_UNCHANGED)

    # Verificar si la imagen fue cargada correctamente
    if image is None:
        print(f"No se pudo cargar la imagen en la ruta: {path}")
        return None

    # Convertir la imagen de BGR a RGB si tiene tres canales
    if len(image.shape) == 3:
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        red_channel = image_rgb[:, :, 0]  # Tomar solo el canal rojo
    else:
        red_channel = image  # Si es en escala de grises, no se necesita conversión

    # Mostrar la imagen del canal rojo con Matplotlib
    plt.imshow(red_channel, cmap='gray')
    plt.axis('off')  # Ocultar los ejes
    plt.show()

    return red_channel  # Devolver la imagen del canal rojo
