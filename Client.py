import WordCount_pb2 as archivoCliente
import WordCount_pb2_grpc as archivoServer
import ArchivoContador as archivoPython
import grpc
from concurrent import futures

file = ""
workerID = 0
def runClient():
    with grpc.insecure_channel('localhost:50051') as channel:
        global workerID
        global file
        stub = archivoServer.WordCountStub(channel)
        suma = 0
        valor = 0
        option = menuSelect()
        while option != 6:
            files = file.split(" ")
            i = 0
            for i in range (i, len(files)-1):
                response = stub.elContador(archivoCliente.getInformation(fileName=files[i], option=option, idWorker=workerID))
                if option == 2:
                    print(f"\n\n\nEl contenido del fichero {files[i]} es: \n\n{response.fileData}")
                    print(f"{50*'*'}")
                if option == 1:
                    valor = int(response.fileData)
                    print(f"\n\n\nEl fichero {files[i]} tiene un total de {valor} palabras diferentes")
                    suma += valor
            if option==1:
                print(f"\n\n\nSe han analizado en total {len(files)-1} y tienen un total de {suma} palabras diferentes")
            print(f"{50*'*'}")
            option = menuSelect()


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
