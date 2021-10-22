print("La salida será un archivo llamado output.txt")

orig_stdout = sys.stdout #guarda console original

file_path = 'output.txt'
sys.stdout = open(file_path, "w") #imprime a archivo

for x in range(len(file1)-1):
    
    file1[x] = convert(file1[x])
    if (file1[x] != None):
    	print (file1[x])
    #print("-------------------------------------")

sys.stdout.close()
sys.stdout = orig_stdout #revierte a imprimir en consola

