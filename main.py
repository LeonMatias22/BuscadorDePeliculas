from menu import menu, crear_rectangulo
from funciones import filtrarPorAnio, filtrarPorEtiqueta, buscarPalabraTitulo, ordenar, mostrarTodas
import os

def limpiar_consola():
    os.system('clear')

def main():
    
    while True:
        
        menu()
        
        opcion = input("Ingrese una opción: ")
        
         
        
        if opcion == "1":
            mostrarTodas()
            pausa = input("Pulsa ENTER para continuar")
            limpiar_consola()
            
        elif opcion == "2":
            palabra = input("ingrese la palabra que desea buscar: ").lower()
            print(buscarPalabraTitulo(palabra))
            pausa = input("Pulsa ENTER para continuar")
            limpiar_consola()
            
        elif opcion == "3":
            etiqueta = input("Ingrese la etiqueta: ").lower()
            print(filtrarPorEtiqueta(etiqueta))
            pausa = input("Pulsa ENTER para continuar")
            limpiar_consola()
            
        elif opcion == "4":
            anio = input("Ingrese el año: ")
            if anio.isnumeric() == False:
                print("Debe ingresar un valor numérico")
                pausa = input("Pulsa ENTER para continuar")
                limpiar_consola()
                continue
            else:
                anioNum = int(anio)
                print(filtrarPorAnio(anioNum))
                pausa = input("Pulsa ENTER para continuar")
                limpiar_consola()
                
               
        elif opcion == "5":
            propiedad = input("Ingrese la propiedad: ").lower()
            ordenar(propiedad)
            pausa = input("Pulsa ENTER para continuar")
            limpiar_consola()
            
        elif opcion == "6":
            confirmar = """
            ¿Está seguro que desea salir?
            1_SI
            2_NO
            """
            print(crear_rectangulo(confirmar))
            opcionSalida = input("Elija una opcion: ")
            
            if opcionSalida == "2":
                pausa = input("Pulsa ENTER para continuar")
                limpiar_consola()
            elif opcionSalida == "1":
                mensajeDeSalida = """
                Gacias por tu visita!! Adios!!
                """
                # time.sleep(1)
                print(crear_rectangulo(mensajeDeSalida))
                limpiar_consola()
                break
            else:
                print("Opción inválida")
                pausa = input("Pulsa ENTER para continuar")
                limpiar_consola()
            
                
            
            
        else:
            print("Opción inválida")
            pausa = input("Pulsa ENTER para continuar")
            limpiar_consola()
        
    
if __name__ == "__main__":
    main()