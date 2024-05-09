def recibirDatos():
    ciclistas = []
    
    print("Introduce los datos de los ciclistas o escribe 'ingreso' para finalizar la entrada de datos y acceder al menú.")
    while True:
        dijito = input("dijite 'ingreso' para ingresar al siclista: ")
        if dijito.lower() == 'ingreso':
            codigo = input("dijite codigo del siclista: ")
            nombre = input("Ingresa el nombre del ciclista: ")
            edad = input("Ingresa la edad del ciclista: ")
            pais = input("Ingresa el país del ciclista: ")
            equipo = input("Ingresa el equipo del ciclista: ")
            tiempo = float(input("Ingresa el tiempo (en minutos) de la última prueba: "))
            ciclistas.append((codigo, nombre, edad, pais, equipo, tiempo))
            return ciclistas
        #main()
        break

def mostrarTabla(ciclistas):
    print("Tabla de Posiciones:")
    for ciclistas in sorted(ciclistas, key=lambda x: x[5]):  # Ordena por tiempo
        print(f"Código: {ciclistas[0]}, Nombre: {ciclistas[1]}, Edad: {ciclistas[2]}, País: {ciclistas[3]}, Equipo: {ciclistas[4]}, Tiempo: {ciclistas[5]} min")

def corregirTiempo(ciclistas, codigo, nuevoTiempo):
    for i in range(len(ciclistas)):
        if ciclistas[i][0] == codigo:
            ciclistas[i] = ciclistas[i][:5] + (nuevoTiempo,)
            print("Tiempo actualizado correctamente.")
            return
    print("Código no encontrado.")

def retirarCiclista(ciclistas, codigo):
    for i in range(len(ciclistas)):
        if ciclistas[i][0] == codigo:
            del ciclistas[i]
            print("Ciclista retirado correctamente.")
            return
    print("Código no encontrado.")

def main():
    ciclistas = recibirDatos()
    while (ciclistas != 'salir' ):
        accion = input("¿Qué deseas hacer? (mostrar, corregir, retirar, salir): ")
        if accion.lower() == 'mostrar':
            mostrarTabla(ciclistas)
        elif accion.lower() == 'corregir':
            codigo = input("Ingresa el código del ciclista a corregir: ")
            nuevoTiempo = float(input("Ingresa el nuevo tiempo (minutos): "))
            corregirTiempo(ciclistas, codigo, nuevoTiempo)
        elif accion.lower() == 'retirar':
            codigo = input("Ingresa el código del ciclista a retirar: ")
            retirarCiclista(ciclistas, codigo)
        elif accion.lower() == 'salir':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, intenta nuevamente.")



main()