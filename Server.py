# Librerias para la ejecucion del programa
import grpc
import redis
from concurrent import futures
from multiprocessing import Process
# Librerias generadas o implementadas por nosotors
import WordCount_pb2 as archivoStub
import WordCount_pb2_grpc as archivoServer
import archivoContador as contador

# Variables globales
listaWorkers = []
idWorker = 0
colaRedis = redis.StrictRedis(host='localhost', port=6379, db=0)


class WordCount(archivoServer.WordCountServicer):
    # Servicio que permite adjuntar diferentes ficheros a la cola de estos
    def createQueue(self, request, context):
        global colaRedis
        colaRedis.flushdb()
        cantidadFicheros = 0
        files = request.files
        option = request.option
        files = files.split(" ")
        cantidadFicheros = len(files)
        i = 0
        for i in range(cantidadFicheros):
            if option == 1:
                aux = "CW "+files[i]+" "+str(len(files))
            else:
                aux = "WC "+files[i]+" "+str(len(files))
            colaRedis.rpush('keyFichero', aux)
        files = ""
        return archivoStub.returnsString(cadena=str(cantidadFicheros))
    # Servicio que permite crear una cantidad de workers especificada por el usuario
    def createWorkers(self, request, context):
        global colaRedis
        nWorkers = request.cadena
        nWorkers = int(nWorkers)
        for i in range(nWorkers):
            createWorker()
        return archivoStub.returnsString(cadena=str(nWorkers))

    def reponseData (self, request, context):
        parar = "1"
        #print(f"-----> Ficheros {ficherosRedis.llen('Fichero')}")
        #print(f"-----> Resultados {ficherosRedis.llen('Resultados')}")
        if ficherosRedis.llen('Fichero') == 0 and ficherosRedis.llen('Resultados') == (int(request.fileData) + 1):
            parar = "0"
            print("Hey guapo desde el server")
        return archivoClient.fileData(fileData=parar)

    # Add nombre de los ficheros a la cola del redis
    def crearContenido(self, request, context):
        global ficherosRedis
        option = request.option
        ficherosRedis.flushall()
        files = request.files
        files = files.split(" ")
        i = 0
        cantidad = len(files)
        while i < cantidad:
            if files[i] != "None" and files[i] != "NoneType":
                if option == 1:
                    mensaje = "CW "+files[i]
                    ficherosRedis.rpush('Fichero', mensaje)
                if option == 2:
                    mensaje = "WC "+files[i]
                    ficherosRedis.rpush('Fichero', mensaje)
                i += 1
        return archivoClient.fileData(fileData=str(cantidad))

    def crearWorkers(self, request, context):
        idWorker = request.nWorkers
        i = 0
        for i in range(i, idWorker):
                crearWorker()
        return archivoClient.fileData(fileData="He creado los workers que se me han pedido, jeje xD")

    def elContador(self, request, context):
        global option
        option = request.option
        idWorker = request.idWorker
        i=0         
        if option == 3:
            contenido = showWorkers()
            return archivoClient.fileData(fileData=contenido)
        else:
            return archivoClient.fileData(fileData="Nada")

    def response(self, request, context):
        global ficherosRedis
        resultados = ""
        cantidad = int(request.fileData)
        print(f"Me llega un total de --> {cantidad}")
        valores = False
        i = 0
        while ficherosRedis.llen('Resultados') > 0 and ficherosRedis.llen('Fichero') == 0 and i < cantidad:
            print("Hola, hay resultados y no hay tareas")
            valores = True
            resultado = ficherosRedis.lpop('Resultados')
            if resultado != None and resultado != "":
                resultado = resultado.decode("utf-8")
                resultados += resultado + " "
            i += 1
        if valores:
            resultados = resultados[:-1]
        return archivoClient.fileData(fileData=resultados)



def StartServer():
    global ficherosRedis
    ficherosRedis.flushall()
    #ficherosRedis.rpush('Fichero', "")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    archivoServer.add_WordCountServicer_to_server(WordCount(), server)
    server.add_insecure_port('[::]:50051')
    print("Servidor iniciado")
    server.start()
    server.wait_for_termination()
Workers = []
idWorker = 0
def crearWorker():
    global Worker
    global idWorker
    procesoWorker = Process(target=iniciarWorker, args=(idWorker, ))
    procesoWorker.start()
    Workers.append(procesoWorker)
    idWorker += 1

def iniciarWorker(idWorker):
    global responseContenido
    global resultadoRedis
    option = 0
    suma = 0
    i = 0
    stop = False
    while True:
        i = 0
        #print("Entro cola Ficheros")
        if ficherosRedis.llen('Fichero') > 0:
            nombreFichero = (ficherosRedis.lpop('Fichero'))#.decode("utf-8")
            if nombreFichero != None and nombreFichero != "":
                nombreFichero = (nombreFichero.decode("utf-8")).split(" ")
                if nombreFichero[0] == "WC":
                    option = 2
                else:
                    option = 1
                
                responseContenido = archivoPython.WordCount(nombreFichero[1], option)
                ficherosRedis.rpush('Resultados', responseContenido)
        ficherosRedis.rpush('Resultados', -1)
        if ficherosRedis.llen('Fichero') == 0 and option == 1 and ficherosRedis.llen('Resultados') > 0:
            lista = ""
            cadena = 0
            while stop != True:
                lista = ficherosRedis.lrange('Resultados', 0, -1)
                bytesObj = lista[i]
                cadena = int(bytesObj.decode("utf-8"))
                if cadena == -1:
                    stop = True
                else: 
                    suma += cadena
                    i += 1
                    print(f"----> {type(cadena)} +++++> {suma}")
                print(i)
            #print("No bucle infinito")
            ficherosRedis.rpush('Resultados', suma)


def showWorkers():
    wActivos = ""
    for i in range(len(Workers)):
        wActivos += "Worker --> " + str(Workers[i]) + "\n"
    return wActivos


if __name__ == '__main__':
    StartServer()