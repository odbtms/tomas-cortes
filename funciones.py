import random
import csv

def registrar(lista):
    cafevie=0
    cafesaba=0
    cafedom=0
    while True:
        nombre=input("ingrese su nombre: ")
        if nombre !="" and nombre.isalpha():
            break
        else:
            print("debe colocar un nombre y solo caracteres sin numeros")

    while True:
        edad= int(input("ingrese su edad: "))
        if edad>0 :
            break
        else:
            print("debe ingresar edad y debe ser mayor a 0")

    equipo=input("ingrese nombre de su equipo: ")
    print("tasa de cafe bebidas")
    while True:
        viernes=int(input("tazas de cafe bebidas el viernes: "))
        cafevie+=viernes
        sabado=int(input("tazas de cafe bebidas el sabado: "))
        cafesaba+=sabado
        domingo=int(input("tazas de cafe bebidas el domingo: "))
        cafedom+=domingo
        total= cafevie+cafesaba+cafedom
        if total>=3:
            id=random.randint(10000,99999)
            lista.append([id,nombre,edad,equipo,cafevie,cafesaba,cafedom])

            break
        else:
            print("debe haber bebido mas de 3 tazas de cafe entre viernes,sabado y domingo")
            continue

def listar_consumos(lista):
    print("id jugador   \tJugador\tedad\tequipo\t   viernes\tsabado\tdomingo")
    for i in lista:
        print(f" {i[0]}      \t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}\t{i[5]}\t{i[6]}\t")

def imprimir(lista):
    equip=input("ingrese el nombre de su equipo: ")
    archivo=open("hojaconsumo.csv","w")
    archivo.write("id jugador,Jugador,edad,equipo,viernes,sabado,domingo\n")
    for i in lista:
        if equip==i[3]:
            archivo.write(f"\n{i[0]},{i[1]},{i[2]},{i[3]},{i[4]},{i[5]},{i[6]}")
        else:
            print(f"{equip} no encontrado")


def buscarid(lista):
    id=int(input("ingrese su ID: "))
    for i in lista:
        if id==i[0]:
            print("id jugador   \tJugador\tedad\tequipo\t   viernes\tsabado\tdomingo")
            print(f" {i[0]}      \t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}\t{i[5]}\t{i[6]}\t")
        else:
            print("")



    

