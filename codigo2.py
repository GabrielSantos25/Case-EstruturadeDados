from datetime import datetime
import time
fila = list()
for c in range(3):
    # Gera o código do cliente q chega na fila.
    cliente = int(input('N: '))
    # A variavel "horai" tem a função de pegar a hora que o cliente chega na fila, após gerar o código!
    horai = time.strftime('%H:%M:%S', time.localtime())
    # A variavel "time_1" tem a função de transformar a hora inicial em str na biblioteca datetime para permitir a manipulão das horas (calcular).
    time_1 = datetime.strptime(horai, "%H:%M:%S")

    aten = str(input('Foi atendido (S): ')).upper()
    if aten == 'S':
            horaf = time.strftime('%H:%M:%S', time.localtime())
            time_2 = datetime.strptime(horaf,"%H:%M:%S")
            time_interval = time_2 - time_1
            fila.append([cliente, str(time_interval)])
    else:
        print('Não foi aten')
print(horai)
print(fila)