	# Practica1SistemasDistribuidos
Práctica centrada en middleware, donde se trabaja con gRPC.
Esta práctica se centra que a partir de un archivo con extensiçon 'proto' creamos una sería de ficheros que contendrán la información necesaria para poder crear y comunicar el servidor y cliente de manera optima. 
Actualmente se inicia el servidor en el localhost y el puerto 50051, y el cliente accede a este mismo a partir del stub.
Para poder ejecutar correctamente es necesario:
- Tener Python instalado en su equipo, la versión 3.X es la adecuada (https://www.python.org/downloads/).
- Instalar gRPC en su equipo (https://grpc.io/docs/languages/python/quickstart/).
- Instalar redis, tanto como server y cliente.
- Una vez instalado lo anterior, descargar el fichero zip que contiene los datos y descomprimirlo.
- Acceder a la carpeta descomprimida y ejecutar primeramente el servidor de redis, donde se deberá abrir un terminal y escribir 'redis-server'.
- A continuación ejecutar el 'server.py'.
- Después para hacer la ejecución del 'client.py', se deberá incorporar los siguientes argumentos:
	- python3 client.py nWorkers opcion idWorker/fichero1 fichero2 fichero3 fichero4 fichero5
	Donde:
		nWorkers --> cantidad de workers que se crearán por interacción con el servidor-
		opcion   --> 1 (analizar x ficheros con las palabras diferentes), 2 (analizar x ficheros con su concurrencia de palabras), 3 (mostrar Workers activos), 4 (añadir un nuevo Worker), 5(eliminar workers con un id predefinido)
		idWorker --> número de worker a borrar y eliminar de la lista de workers
		ficheroX --> puedes añadir todos los ficheros que existan en el directorio para analizar

La práctica esta realizada por Àlex Figueroa Boronat (alex.figueroa@estudiants.urv.cat), Juan Cigales de Padua (juan.cigales@estudiants.urv.cat) y Daniil Nikiforov (danil.nikiforov@estudiants.urv.cat).

El link del GitHub es el siguiente: https://github.com/DGallardoNiki/Practica1SistemasDistribuidos
