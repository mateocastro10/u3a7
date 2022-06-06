from Manejador import Manejador
from objectencoder import ObjectEncoder
from menu import Menu
if __name__=='__main__':
    menu=Menu()
    jsonF=ObjectEncoder()
    maneja = Manejador()
    diccionario=jsonF.leerJSONArchivo('personal.json')
    maneja=jsonF.decodificarDiccionario(diccionario)
    print('archivo leido!')
    salir=False
    while not salir:
        print('------------------------------------------')
        print('1.Insertar un agente')
        print('2.Agregar agente')
        print('3.Dada una posicion, mostrar')
        print('4.ingresar carrera y generar lista')
        print('5.ingresar area y mostrar docentes investigadores')
        print('6.recorrer lista y mostrar lista ordenada')
        print('7.ingresar categoria y mostrar extras que debe pagar la secretaria')
        print('8.generar JSON')
        print('------------------------------------------')
        op=input('->')
        menu.opcion(op,maneja,jsonF)
        salir = op =='9'
