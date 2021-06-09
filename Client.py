import WordCount_pb2 as archivoCliente
import WordCount_pb2_grpc as archivoServer
import ArchivoContador as archivoPython
import grpc
from concurrent import futures

def runClient():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = archivoServer.WordCountStub(channel)
        response = stub.elContador(archivoCliente.getInformation(fileName="Client.py", option=0, idWorker=0))
        print(response.fileData)

if __name__ == "__main__":
    runClient()
