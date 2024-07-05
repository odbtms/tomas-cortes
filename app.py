import funciones
lista=[]
while True:
    print("""
1. Registrar consumo
2. Listar consumos
3. Imprimir hoja consumo
4. Buscar consumo por id
5. Salir del programa
          """)
    opc=input("ingrese una opcion: ")

    if opc=="1":
        funciones.registrar(lista)
    elif opc=="2":
        funciones.listar_consumos(lista)
    elif opc=="3":
        funciones.imprimir(lista)
    elif opc=="4":
        funciones.buscarid(lista)
    elif opc=="5":
        break
    else:
        print("opcion incorrecta")