import WordCount_pb2 as archivoCliente
import WordCount_pb2_grpc as archivoServer
import ArchivoContador as archivoPython
import grpc
from concurrent import futures
import redis
file = ""
workerID = 0
primeraInt = True
ficheroRedis = redis.StrictRedis(host='localhost', port=6379, db=0)

def runClient():
    with grpc.insecure_channel('localhost:50051') as channel:
        global workerID
        global file
        global ficheroRedis
        stub = archivoServer.WordCountStub(channel)
        suma = 0
        valor = 0
        nWorkers = 0
        option = 0
        #print(ficheroRedis.lrange('Resultados', 0, -1)

        if primeraInt:
            nWorkers = workerSelect()
            response = stub.crearWorkers(archivoCliente.ctosWorkers(nWorkers=nWorkers))
            print(response.fileData)
        option = menuSelect()
        while option != 6:
            if 0 < option < 3:
                file = file[:-1]
                response = stub.crearContenido(archivoCliente.filesAndOptions(files=file, option=option))
            if option == 3:
                response = stub.elContador(archivoCliente.getInformation(fileName="", option=option, idWorker=0))
                print(response.fileData)
            contenidoFichero = stub.response(archivoCliente.fileData(fileData=""))
            file = ""
            option = menuSelect()



def workerSelect():
    global primeraInt
    primeprimeraInt = False
    return int(input("Introduzca el numero de Workers que se crearan: "))

def menuSelect():
    global file
    global workerID
    print("1. Contar palabras diferentes")
    print("2. Contar la concurrencias de las diferentes palabras")
    print("3. Mostrar Workers activos")
    print("4. Add worker")
    print("5. Eliminar workers")
    print("6. Salir del servidor")

    option = int(input("Introduza una opcion: "))
    if option > 0 and option < 3:
        cantidad = int(input("Cuantos ficheros analizara?: "))
        i = 0
        for i in range (i, cantidad):
            file += input(f"Introduzca el nombre del fichero {i+1}:") + " "
    if option == 5:
        workerID = int(input("Introduzca el ID del worker a borrar: "))

    return option

if __name__ == "__main__":
    runClient()
