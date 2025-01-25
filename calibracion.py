import numpy as np
import matplotlib.pyplot as plt

def crear_curva_de_calibracion_pol(dosis, valores_medios):
    """
    Crea una curva de calibración polinómica basada en los valores medios de píxel y los valores de dosis.

    Parámetros:
    dosis: list o np.array
        Lista con los valores de dosis correspondientes para cada ROI.
    valores_medios: list o np.array
        Lista con los valores medios de píxel para cada ROI.
    
    Returns:
        polinomio (numpy.poly1d): el objeto polinómico ajustado
        dosis_fit (numpy.ndarray): array de dosis usado para la curva
        valores_fit (numpy.ndarray): valores estimados por el polinomio    """

    # Verificar que los datos tengan la misma longitud
    if len(valores_medios) != len(dosis):
        print("El número de valores medios no coincide con el número de valores de dosis proporcionados.")
        return
    # Ajustar un polinomio de grado 4 a los datos
    coeficientes = np.polyfit(dosis, valores_medios, 4)
    polinomio = np.poly1d(coeficientes)

    # Generar valores de dosis para la curva
    dosis_fit = np.linspace(min(dosis), max(dosis), 1000)
    valores_fit = polinomio(dosis_fit)

    return polinomio, dosis_fit, valores_fit


#funcion para calcular la dosis por pixel
def calcular_dosis_limitado_tiff(image, polinomio,max_intensity):
    """
    Aplica un polinomio de calibración para calcular la dosis por píxel en una imagen TIFF,
    limitando la evaluación a un rango de intensidades. Los píxeles fuera de rango se marcan
    como 0 (o podrían definirse con otro valor).

    Parámetros
    ----------
    image : np.ndarray
        Imagen TIFF de entrada, generalmente en un tipo entero (p.ej., uint16).
    polinomio : np.poly1d
        Polinomio de calibración (por ejemplo, obtenido de np.polyfit).
    min_intensity : int o float
        Intensidad mínima válida para aplicar la calibración.
    max_intensity : int o float
        Intensidad máxima válida para aplicar la calibración.

    Retorna
    -------
    np.ndarray
        Imagen de salida con la misma forma que 'image'. Los valores dentro de rango
        se transforman mediante 'polinomio', y los fuera de rango se ponen a 0.
        El dtype es el mismo que el de 'image'.
    """

    # Verificamos que la imagen sea un array NumPy
    if not isinstance(image, np.ndarray):
        raise TypeError("La entrada 'image' debe ser un np.ndarray.")

    # Creamos una copia (en el MISMO dtype) para el resultado final.
    # Inicializamos con ceros para los valores fuera de rango.
    dose_result = np.zeros_like(image, dtype=image.dtype)

    # Creamos una máscara booleana para identificar píxeles dentro del rango válido
    in_range_mask = image <= max_intensity

    # Extraemos solo los valores en rango y convertimos a float para la evaluación del polinomio
    # (Se evita convertir TODA la imagen de una sola vez).
    in_range_values = image[in_range_mask].astype(np.float32)

    # Evaluamos el polinomio en esos valores
    evaluated_vals = np.polyval(polinomio, in_range_values)

    # Si el polinomio puede generar valores fuera del rango de nuestro dtype (por ejemplo, < 0
    # o > 65535 en uint16), podemos recortarlos (clamping). Ejemplo para uint16:
    if image.dtype == np.uint16:
        evaluated_vals = np.clip(evaluated_vals, 0, 65535)

    # Convertimos de nuevo al mismo tipo de la imagen original (puede causar redondeo)
    evaluated_vals = evaluated_vals.astype(image.dtype)

    # Asignamos los valores evaluados de vuelta al arreglo de salida en las posiciones válidas
    dose_result[in_range_mask] = evaluated_vals

    return dose_result