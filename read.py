def leer(path):
    import cv2
    import matplotlib.pyplot as plt
    import numpy as np
    image=cv2.imread(path,cv2.COLOR_BGR2RGB)

# Verificar si la imagen fue cargada correctamente
    if image is None:
        print(f"No se pudo cargar la imagen en la ruta: {path}")
    else:
        # Convertir la imagen de BGR a RGB si tiene tres canales
        if len(image.shape) == 3:
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        else:
            image_rgb = image  # Si es en escala de grises, no se necesita conversión

    if image_rgb.dtype == np.uint16:  # Si es una imagen de 16 bits
        image_rgb = (image_rgb / 65535.0) * 255  # Normalizar a [0, 255]
        image_rgb = image_rgb.astype(np.uint8)


    # Mostrar la imagen con Matplotlib
    plt.imshow(image_rgb, cmap='gray' if len(image.shape) == 2 else None)
    plt.axis('off')  # Ocultar los ejes
    plt.show()

    return image_rgb  # Devolver la imagen procesada