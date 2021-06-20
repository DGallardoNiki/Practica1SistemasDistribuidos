# Librerias generadas o implementadas por nosotors
import WordCount_pb2 as archivoStub
import WordCount_pb2_grpc as archivoServer
import archivoContador as contador

# Librerias para la ejecucion del programa
import grpc
import sys
# Variables globales
def startClient():
    with grpc.insecure_channel('localhost:50051') as channel:
        files = ""
        stop = False
        stub = archivoServer.WordCountStub(channel)
        #print("Opciones: 1. Palabras diferentes 2. Concurrencia palabras 3. Mostrar Workers 4. Crear Worker 5. Eliminar Worker")
        #print("Si se escoge la opcion --> 1/2: ficheros a pasar 3/4: nada mas 5: idWorker")
        #print("parametros: 1: nWorkers 2: opcion 3: idWorker/ficheros 4..n: ficheron")
        nWorkers = sys.argv[1]
        resultadoWorkers = stub.createWorkers(archivoStub.returnsString(cadena=nWorkers))
        option = int(sys.argv[2])
        if option == 3 or option == 4:
            respuesta = stub.someOpc(archivoStub.noCount(opc=option, idW=0))
            print(respuesta.cadena)
        if option == 5:
            idW = int(sys.argv[3])
            respuesta =  stub.someOpc(archivoStub.noCount(opc=option, idW=idW))
            print(respues.cadena)
        if option == 1 or option == 2:
            i = 3
            cantidadArchivos = len(sys.argv)
            while i < cantidadArchivos:
                files += sys.argv[i]+" "
                i += 1
            if cantidadArchivos == 0:
                print("No se han introducido fichero para analizar")
            else:
                if cantidadArchivos == 1:
                    insertarRespuesta = stub.createQueue(archivoStub.yesCount(files=files, option=option))
                    resultadoFichero = stub.popResponse(archivoStub.returnsString(cadena=""))
                    print("El resultado de el fichero unico {file} es {resultadoFichero.cadena}")
                if cantidadArchivos > 1:
                    files = files[:-1]
                    insertarRespuesta = stub.createQueue(archivoStub.yesCount(files=files, option=option))
                    aux = stub.checkQueue(archivoStub.returnsString(cadena=""))
                    while aux.cadena != "1":
                        aux = stub.checkQueue(archivoStub.returnsString(cadena=""))
                    while aux.cadena != "3":
                        resultadoFichero =  stub.popResponse(archivoStub.returnsString(cadena=""))
                        aux = stub.checkQueue(archivoStub.returnsString(cadena=""))
                    print(resultadoFichero.cadena)
        

if __name__ == '__main__':
    startClient()
