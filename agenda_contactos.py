def mostrar_menu():
    print("\nAgenda de contactos:")
    print("1. Agregar nuevo contacto")
    print("2. Eliminar contacto existente")
    print("3. Buscar contacto")
    print("4. Lista de contactos")
    print("5. Salir del programa")
    
    

    print("\n")


def agregar_contacto(agenda):
    nombre = input("Por favor introduzca el nombre completo del contacto:").strip().lower()
    telefono = input("Por favor introduzca el telefono del contacto:")
    email = input("Por favor introduzca el email del contacto:")
    agenda[nombre] = {"telefono": telefono, "email": email}
    print(f"¡Se ha agregado el contacto {nombre.title()} exitosamente\n")


def eliminar_contacto(agenda):
    nombre = input("Ingrese el nombre de la agenda que desea elminar: ").strip().lower()
    if nombre in agenda:     
        del agenda[nombre]
        print(f"El contacto de {nombre.title()} ha sido eliminado")
        if not agenda:
            print("La agenda esta vacia.")
    else:
        print(f"No se ha encontrado un contacto con el nombre {nombre.title()}.")


def buscar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto  que desea buscar: ").strip().lower()
    if nombre in agenda:
        print(f"Nombre: {nombre.title()}")
        print(f"Telefono: {agenda[nombre]["telefono"]}")
        print(f"Email: {agenda[nombre]["email"]}")
    else:
        print(f"El contacto {nombre.title()} no ha sido encontrado en la agenda")

 
def listar_contactos(agenda):
    if agenda:
        print("Lista de contactos:\n")
        for nombre, info in agenda.items():
            print(f"Nombre : {nombre.title()}")
            print(f"Telefono : {info["telefono"]}")
            print(f"Email : {info["email"]}\n")
    else:
        print("\n")
        print("La agenda aun esta vacia")


def agenda_contacto():
    agenda = {}

    listar_contactos(agenda)
    
    while True:
        mostrar_menu()
        opcion = input("Por favor elija una opcion: ")
        print("\n")

        if opcion == "1":
            agregar_contacto(agenda)
        elif opcion == "2":
            eliminar_contacto(agenda)
        elif opcion == "3":
            buscar_contacto(agenda)
        elif opcion == "4":
            listar_contactos(agenda)
        elif opcion == "5":
            print("Saliendo de la agenda de contactos ¡Hasta luego!")
            break
        else:
            print("Por favor seleccion una opcion valida (del 1 al 5)")


agenda_contacto()
