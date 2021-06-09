import WordCount_pb2 as archivoClient
import WordCount_pb2_grpc as archivoServer
import ArchivoContador as archivoPython
import grpc
from concurrent import futures

class WordCount(archivoServer.WordCountServicer):
    def elContador(self, request, context):
        option = request.option
        files = request.fileName
        idWorker = request.idWorker
        contenido = archivoPython.WordCount(files, 1)
        return archivoClient.fileData(fileData=contenido)

def StartServer():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    archivoServer.add_WordCountServicer_to_server(WordCount(), server)
    server.add_insecure_port('[::]:50051')
    print("Servidor iniciado")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    StartServer()