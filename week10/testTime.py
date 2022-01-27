# testTime v0.2
# Add restart funcion
# Francesco Esposito - Diciembre 2021

# Importo el modulo time
import time
# Capturo el tiempo al llamarse el modulo
start = time.time()

def restart(v=True):
    global start
    start = time.time()
    if v == True:
        print('Test time restart!')

def timer(v=True):
    '''
    Una función para calcular el tiempo de ejecución de un script.

    Args:
    v (bool) = Si activar la impresión en pantalla (por defecto True)

    Returns:
    float = el tiempo transcurrido en segundos

    '''

    # Capturo el tiempo de ejecución desde que se ha importado el módulo
    end = time.time() - start

    # Si Verbose está activo
    if v == True:
        # Lo muestra en segundos
        if end > 1:
            unit = 's'
            r = round(end, 2)
        else:
            # Lo muestra en milisegundos
            if end > 0.001:
                unit = 'ms'
                r = int(end * (10**3))
            else:
                # Lo muestra en microsegundos
                unit = 'μs'
                r = int(end * (10**6))
        # Imprimo el resultado
        print('Test time:', r, unit)

    # Devuelvo el resultado, siempre en segundos (s)
    return end

# For testing purposes
if __name__ == '__main__':
    timer()