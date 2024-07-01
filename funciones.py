from db import peliculas
from tabulate import tabulate


def tablas(lista):
    table = []
    for elemento in lista:
        table.append([elemento['titulo'], elemento['autor'], elemento['anio'], elemento['genero'], elemento['rating'], ", ".join(elemento['etiquetas'])])
    headers = ["Título", "Autor", "Año", "Género", "Rating", "Etiquetas"]
    return tabulate(table, headers, tablefmt="pretty")

     
def mostrarTodas():
    print(tablas(peliculas))


def filtrarPorAnio(anio):
    porAnio = list(filter(lambda pelicula: pelicula["anio"] == anio, peliculas))
    if len(porAnio) == 0:
        return "No se encontraron coincidencias"
    return tablas(porAnio)

def buscarPalabraTitulo(palabra):
    porPalabraTitulo = list(filter(lambda pelicula: palabra in pelicula["titulo"].lower(), peliculas))
    if len(porPalabraTitulo) == 0:
        return "No se encontraron coincidencias"
    return tablas(porPalabraTitulo)
    

def filtrarPorEtiqueta(etiqueta):
    porEtiquetas = list(filter(lambda pelicula:etiqueta in pelicula["etiquetas"], peliculas))
    if len(porEtiquetas) == 0:
        return "No se encontraron coincidencias"
    return tablas(porEtiquetas)
    
    
def ordenar(propiedad):
    if propiedad != "autor" and propiedad != "anio" and propiedad != "genero" and propiedad != "rating" and propiedad != "etiquetas" and propiedad != "titulo":
        print("La propiedad NO existe")
    else:
        peliculas.sort(key=lambda x: x[propiedad])
        print(tablas(peliculas))



# if __name__=="__main__":
    
#     anioUsuario = int(input("Ingrese un anio: "))
#     print(filtrarPorAnio(anioUsuario))