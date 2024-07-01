def crear_rectangulo(mensaje):
    lineas = mensaje.split('\n')
    ancho = max(len(linea) for linea in lineas) + 4  
    rectangulo = []
    rectangulo.append('+' + '-' * (ancho - 2) + '+')
        
    for linea in lineas:
        rectangulo.append('| ' + linea.ljust(ancho - 4) + ' |')
            
    rectangulo.append('+' + '-' * (ancho - 2) + '+')

    return '\n'.join(rectangulo)

texto = """ - - - - - - - - - - - - - - - - - - - -  -  MENÚ   - - - - -  - - - - - - - - - - - - - - - - - - - 
    1_Devolver todas las películas.
    2_BUSCAR por palabra clave en el título.
    3_FILTRAR por etiqueta.
    4_FILTRAR por año.
    5_ORDENAR según propiedad.
    6_SALIR.
    """
bienvenida = "- - - - - - - - - - - - - - - - - - -   BUSCADOR DE PELÍCULAS   - - - - - - - - - - - - - - - - - - "


def menu():
    print(crear_rectangulo(bienvenida))
    print(crear_rectangulo(texto))
    
    