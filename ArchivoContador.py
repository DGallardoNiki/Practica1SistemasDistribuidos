def WordCount(filename, opc):
	lisDif = []
	lisCo = []
	if filename != "":
		fileDa = readFile(filename)
		fileData = fileDa.splitlines()
		i = j = 0
		lines = len(fileData) - 1
		li = lines
		while (lines != -1):
			split = fileData[lines].split()
			for j in range(len(split)):
				split[j] = split[j].strip(".,;?!")
				if split[j] not in lisDif:
					lisDif.append(split[j])
			lines -= 1
		for i in range (len(lisDif)):
			lisCo.append(lisDif[i] + " " + (str)(fileDa.count(lisDif[i]))+ "\n")

		if opc == 1:
			return (str(len(lisDif)))
		else:
			strCon = " "
			return (strCon.join(lisCo))

def readFile(filename):
	file = open(filename, "r")
	data = (file.read()).lower()
	file.close
	return data