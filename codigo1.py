#Codigo, organização das filas (Noção da menor fila)....
fila1 = list()
fila2 = list()
fila3 = list()
fila4 = list()
while True:
    while True:
        for f1 in range(1):
            fila1.append(int(input('N: ')))
    
        for f2 in range(1):
            fila2.append(int(input('N: ')))
    
        for f3 in range(1):
            fila3.append(int(input('N: ')))
        
        for f4 in range(1):
            fila4.append(int(input('N: ')))
            
        if len(fila1) == 3:
            break    
    if len(fila1) == 3:
        break
print(fila1)
print(fila2)
print(fila3)
print(fila4)