import WordCount_pb2 as archivoClient
import WordCount_pb2_grpc as archivoServer
import ArchivoContador as archivoPython
import grpc
from concurrent import futures
from multiprocessing import Process
import redis
from os import system

WORKERS = []
WORKERS_ID = 0
suma_palabras = 0
concurrenciaPalabras = ""
ficherosRedis = redis.StrictRedis(host='localhost', port=6379, db=0)
option = 0
responseContenido = ""
class WordCount(archivoServer.WordCountServicer):
    # Add nombre de los ficheros a la cola del redis
    def crearContenido(self, request, context):
        global ficherosRedis
        option = request.option
        ficherosRedis.flushall()
        files = request.files
        files = files.split(" ")
        i = 0
        while i < len(files):
            if files[i] != "None" and files[i] != "NoneType":
                if option == 1:
                    mensaje = "CW "+files[i]
                    ficherosRedis.rpush('Fichero', mensaje)
                if option == 2:
                    mensaje = "WC "+files[i]
                    ficherosRedis.rpush('Fichero', mensaje)
                i += 1
        return archivoClient.fileData(fileData=str(len(files)))

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
        while ficherosRedis.llen('Resultados') > 0:
            resultado = ficherosRedis.lpop('Resultados')
            if resultado != None and resultado != "":
                resultado = resultado.decode("utf-8")
                resultados += resultado
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
    while True:
        i = 0
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
        if ficherosRedis.llen('Ficheros') < 1 and ficherosRedis.llen('Resultados') > 0 and option == 1 and ficherosRedis.llen('Respuestas') > 1:
            lista = ""
            while i < ficherosRedis.llen('Resultados'):
                lista = ficherosRedis.lrange('Resultados', 0, -1)
                bytesObj = lista[i]
                cadena = bytesObj.decode("utf-8")
                suma += int(cadena)
                i += 1
            ficherosRedis.rpush('Resultados', suma)


def showWorkers():
    wActivos = ""
    for i in range(len(Workers)):
        wActivos += "Worker --> " + str(Workers[i]) + "\n"
    return wActivos


if __name__ == '__main__':
    StartServer()