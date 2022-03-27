from datetime import datetime
import time
fila1 = list()
fila2 = list()
fila3 = list()
fila4 = list()

while True:
    while True:  
        for f1 in range(1):
            cliente = int(input('N: '))
            horai = time.strftime('%H:%M:%S', time.localtime())
            time_1 = datetime.strptime(horai, "%H:%M:%S")
            aten = str(input('Foi atendido [S/N]: ')).upper() 
            if aten in 'Ss':
                horaf = time.strftime('%H:%M:%S', time.localtime())
                time_2 = datetime.strptime(horaf,"%H:%M:%S")
                time_interval = time_2 - time_1
                fila1.append([cliente, str(time_interval)])
            else:
                if aten in 'Ff':
                    print('Esperando na fila')
                    
        for f2 in range(1):
            cliente = int(input('N: '))
            horai = time.strftime('%H:%M:%S', time.localtime())
            time_1 = datetime.strptime(horai, "%H:%M:%S")
            aten = str(input('Foi atendido [S/N]: ')).upper() 
            if aten in 'Ss':
                horaf = time.strftime('%H:%M:%S', time.localtime())
                time_2 = datetime.strptime(horaf,"%H:%M:%S")
                time_interval = time_2 - time_1
                fila2.append([cliente, str(time_interval)])
            else:
                if aten in 'Ff':
                    print('Esperando na fila')
    
        for f3 in range(1):
            cliente = int(input('N: '))
            horai = time.strftime('%H:%M:%S', time.localtime())
            time_1 = datetime.strptime(horai, "%H:%M:%S")
            aten = str(input('Foi atendido [S/N]: ')).upper() 
            if aten in 'Ss':
                horaf = time.strftime('%H:%M:%S', time.localtime())
                time_2 = datetime.strptime(horaf,"%H:%M:%S")
                time_interval = time_2 - time_1
                fila3.append([cliente, str(time_interval)])
            else:
                if aten in 'Ff':
                    print('Esperando na fila')
                    
        for f4 in range(1):
            cliente = int(input('N: '))
            horai = time.strftime('%H:%M:%S', time.localtime())
            time_1 = datetime.strptime(horai, "%H:%M:%S")
            aten = str(input('Foi atendido [S/N]: ')).upper() 
            if aten in 'Ss':
                horaf = time.strftime('%H:%M:%S', time.localtime())
                time_2 = datetime.strptime(horaf,"%H:%M:%S")
                tempo2 = float(time.strftime('%H.%M', time.localtime()))
                time_interval = time_2 - time_1
                fila4.append([cliente, str(time_interval)])
            else:
                if aten in 'Ff':
                    print('Esperando na fila')
                    
        if len(fila1) == 3:
            break    
    if len(fila1) == 3:
        break

fila1.reverse()
fila2.reverse()
fila3.reverse()
fila4.reverse()

# FILA 1 (Saida)
print('-='*10)
print('FILA 1')
print('-='*10)
for a in range(1):
    print(fila1)
print(f'Total de atendimentos: {len(fila1)}')

# FILA 2 (Saida)
print('-='*10)
print('FILA 2')
print('-='*10)
for b in range(1):
    print(fila2)
print(f'Total de atendimentos: {len(fila2)}')

#FILA 3 (Saida)
print('-='*10)
print('FILA 3')
print('-='*10)
for c in range(1):
    print(fila3)
print(f'Total de atendimentos: {len(fila3)}')

# FILA 4 (Saida)
print('-='*10)
print('FILA 4')
print('-='*10)
for d in range(1):
    print(fila4)
print(f'Total de atendimentos: {len(fila4)}')