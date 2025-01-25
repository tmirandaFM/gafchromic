def leer(path):
    import cv2
    import matplotlib.pyplot as plt
    import numpy as np

    # Leer la imagen en color
    image = cv2.imread(path)

    # Verificar si la imagen fue cargada correctamente
    if image is None:
        print(f"No se pudo cargar la imagen en la ruta: {path}")
        return None

    # Convertir la imagen de BGR a RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Extraer el canal rojo
    red_channel = image[:, :, 2]

    # Mostrar la imagen del canal rojo con Matplotlib
    plt.imshow(red_channel, cmap='Reds')
    plt.axis('off')  # Ocultar los ejes
    plt.show()

    print(f"Dimensiones de la imagen: {red_channel.shape}")
    return red_channel
