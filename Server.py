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

    def popResponse(self, request, context):
        global colaRedis
        auxString = ""
        print(colaRedis.llen('keyResultado'))
        while colaRedis.llen('keyResultado') > 0:
            print(f"Antes del pop --> {colaRedis.lrange('keyResultado', 0, -1)}")
            auxResultado = colaRedis.lpop('keyResultado')           
            if auxResultado != None and auxResultado != "":
                auxResultado = auxResultado.decode("utf-8")
                auxString += auxResultado + " "
        if auxString != "":
           auxString = auxString[:-1]
        print(f"Despues del pop --> {colaRedis.lrange('keyResultado', 0, -1)}")
        colaRedis.flushall()
        colaRedis.flushdb()
        return archivoStub.returnsString(cadena=auxString)
    # Servicio que se encarga de realizar las opciones 3, 4 y 5 que pueda pedir realizar
    #   el cliente. Se retornará el resultado generado
    def someOpc(self, request, context):
        option = request.opc
        id = request.idW
        auxString = ""
        if option == 3:
            auxString = showWorkers()
        if option == 4:
            auxString = createWorker()
        if option == 5:
            auxString = killWorker(id)
        return archivoStub.returnsString(cadena=auxString)

    #Servicio que permite averiguar como se encuentras las diferentes colas
    def checkQueue(self, request, context):
        act = "-1"
        if colaRedis.llen('keyFichero') > 0 and colaRedis.llen('keyResultado') > 0:
            act = "0"
        if colaRedis.llen('keyFichero') == 0 and colaRedis.llen('keyResultado') > 0:
            act = "1"
        if colaRedis.llen('keyFichero') > 0 and colaRedis.llen('keyResultado') == 0:
            act = "2"
        if colaRedis.llen('keyFichero') == 0 and colaRedis.llen('keyResultado') == 0:
            act = "3"
        return archivoStub.returnsString(cadena=act)
           

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

def createWorker():
    global listaWorkers
    global idWorker
    aux = ""
    worker = Process(target=workerLogic)
    worker.start()
    listaWorkers.append(worker)
    idWorker += 1

def killWorker(idW):
    global idWorker
    global listaWorkers
    listaWorkers[idW].kill() 

def workerLogic():
    global colaRedis
    option = 0
    suma = 0
    stop = False
    cadena = 0
    i = 0
    while True:
        if colaRedis.llen('keyFichero') > 0:
            i = 0
            stop = False
            auxNombre = colaRedis.lpop('keyFichero')           
            if auxNombre != None and auxNombre != "":
                auxNombre = (auxNombre.decode("utf-8")).split(" ")
                cantidad = int(auxNombre[2])
                if auxNombre[0] == "WC":
                    option = 2
                else:
                    option = 1
                datosAnalisis = contador.WordCount(auxNombre[1], option)
                colaRedis.rpush('keyResultado', datosAnalisis)
        if colaRedis.llen('keyFichero') == 0 and option == 1 and colaRedis.llen('keyResultado') == cantidad and stop != True and cantidad > 1:#and cadena != -1 
            stop = True
            lista = colaRedis.lrange('keyResultado', 0, -1)
            i=0
            while i<cantidad:
                objBytes = lista[i]
                if objBytes != None and objBytes != "":
                    cadena = int(objBytes.decode("utf-8"))
                    suma += cadena
                i += 1
            if int((colaRedis.lindex('keyResultado', -1).decode("utf-8"))) != suma:
                colaRedis.rpush('keyResultado', suma)
                suma=0
                cadena=0
        option = 0

def showWorkers():
    wActivos = ""
    for i in range(len(listaWorkers)):
        wActivos += "Worker --> " + str(listaWorkers[i]) + "\n"
    return wActivos


if __name__ == '__main__':
    StartServer()