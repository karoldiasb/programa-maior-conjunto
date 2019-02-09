import time 

lista_arquivos = ['dataset-2-a', 'dataset-2-b', 'dataset-2-c', 'dataset-2-d', 'dataset-2-e']
lista_tempo =[]

####ARQUIVO A######
tempo_ini_a = time.time()
arquivoA = open('dataset-2-a.csv','r')
readA = arquivoA.read()
listaA = readA.split("\n")
listaA.remove('')
listaA.sort()
ultimoA = listaA[-1]
tempo_fim_a = time.time()
exeA = tempo_fim_a - tempo_ini_a
lista_tempo.append(exeA)
a = open('resposta-dataset-2-a.txt','w')
a.write(str(ultimoA))
a.write("\n"+str(exeA))
a.close()
arquivoA.close()

####ARQUIVO B######
tempo_ini_b = time.time()
arquivoB = open('dataset-2-b.csv','r')
readB = arquivoB.read()
listaB = readB.split("\n")
listaB.remove('')
listaB.sort()
ultimoB = listaB[-1]
tempo_fim_b = time.time()
exeB = tempo_fim_b - tempo_ini_b
lista_tempo.append(exeB)
b = open('resposta-dataset-2-b.txt','w')
b.write(str(ultimoB))
b.write("\n"+str(exeB))
b.close()
arquivoB.close()

####ARQUIVO C######
tempo_ini_c = time.time()
arquivoC = open('dataset-2-c.csv','r')
readC = arquivoC.read()
listaC = readC.split("\n")
listaC.remove('')
listaC.sort()
ultimoC = listaC[-1]
tempo_fim_c = time.time()
exeC = tempo_fim_c - tempo_ini_c
lista_tempo.append(exeC)
c = open('resposta-dataset-2-c.txt','w')
c.write(str(ultimoC))
c.write("\n"+str(exeC))
c.close()
arquivoC.close()


####ARQUIVO D######
tempo_ini_d = time.time()
arquivoD = open('dataset-2-d.csv','r')
readD = arquivoD.read()
listaD = readD.split("\n")
listaD.remove('')
listaD.sort()
ultimoD = listaD[-1]
tempo_fim_d = time.time()
exeD = tempo_fim_d - tempo_ini_d
lista_tempo.append(exeD)
d = open('resposta-dataset-2-d.txt','w')
d.write(str(ultimoD))
d.write("\n"+str(exeD))
d.close()
arquivoD.close()

####ARQUIVO E######
tempo_ini_e = time.time()
arquivoE = open('dataset-2-e.csv','r')
readE = arquivoE.read()
listaE = readE.split("\n")
listaE.remove('')
listaE.sort()
ultimoE = listaE[-1]
tempo_fim_e = time.time()
exeE = tempo_fim_e - tempo_ini_e
lista_tempo.append(exeE)
e = open('resposta-dataset-2-e.txt','w')
e.write(str(ultimoE))
e.write("\n"+str(exeE))
e.close()
arquivoE.close()


print(lista_tempo)

