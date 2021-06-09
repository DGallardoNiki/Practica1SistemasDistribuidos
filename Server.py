import WordCount_pb2 as archivoClient
import WordCount_pb2_grpc as archivoServer
import ArchivoContador as archivoPython
import grpc
from concurrent import futures
from multiprocessing import Process

WORKERS = []
WORKERS_ID = 0
class WordCount(archivoServer.WordCountServicer):
    def elContador(self, request, context):
        option = request.option
        files = request.fileName
        idWorker = request.idWorker
        if 0 < option < 3:
            contenido = archivoPython.WordCount(files, option)
            return archivoClient.fileData(fileData=contenido)
        if option == 3:
            contenido = showWorkers()
            return archivoClient.fileData(fileData=contenido)
        if option == 4:
            createWorker()
            return archivoClient.fileData(fileData="Worker creado con exito")
        if option == 5:
            deleteWorker(idWorker)
            return archivoClient.fileData(fileData="Worker eliminado correctamente")

def StartServer():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    createWorker()
    archivoServer.add_WordCountServicer_to_server(WordCount(), server)
    server.add_insecure_port('[::]:50051')
    print("Servidor iniciado")
    server.start()
    server.wait_for_termination()

def createWorker():
    global WORKERS
    global WORKERS_ID
    proc = Process(target=startWorker, args=(WORKERS_ID,))
    proc.start()
    WORKERS.append(WORKERS_ID)
    print(WORKERS[WORKERS_ID])
    WORKERS_ID += 1

def startWorker():
    return;
def deleteWorker(idWorker):
    global WORKERS
    WORKERS.remove(idWorker)
def showWorkers():
    wActivos = ""
    for i in range(len(WORKERS)):
        wActivos += "Worker --> " + str(WORKERS[i]) + " activo\n"
    return wActivos


if __name__ == '__main__':
    StartServer()