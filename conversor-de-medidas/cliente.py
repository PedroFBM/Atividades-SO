import socket

#configurando o cliente

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9875

#inicializando o cliente

cliente.connect((host, port))

def receber(valor):
    valor = valor.decode('utf-8')
    print("O resultado da sua conversão é:", valor)

a = 0 #define a variavel do primeiro menu como 0
while a != 2:   #define todas as situações em que o programa deve rodar
    try:
        a = input('\nDigite 1 para escolher sua grandeza ou 2 para sair\n') #caso o usuário queira encerrar a operação, 2 fará com que
        a = int(a)
        cliente.send(str(a).encode('utf-8'))                                                                #o programa quebre sem que o servidor quebre junto
    except ValueError as e:
        print("Valor inválido:", e) #trata o erro de entrada inválida
        continue

    if a == 1:
        try:
            b = int(input("1-temperatura\n2-comprimento\n"))
            cliente.send(str(b).encode('utf-8'))
            print(b)
        except ValueError as e:
            print("Valor inválido:", e)
            continue

        if b == 1:
            try:
                c=int(input("1-Celsius para Kelvin\n2-Kelvin para Celsius\n"))
                cliente.send(str(c).encode('utf-8'))
            except ValueError as e:
                print("Valor inválido:", e)

            if c == 1:
                celsius = int(input("Digite o valor em ºC:\n"))
                print("enviando Celcius")
                cliente.send(str(celsius).encode('UTF-8'))
                valor = cliente.recv(1024)
                receber(valor)

            elif c == 2:
                kelvin = int(input("Digite o valor em °K:\n"))
                cliente.send(str(kelvin).encode('UTF-8'))
                valor = cliente.recv(1024)
                receber(valor)

        if b == 2:
            c = int(input("1-Metros para Quilômetro\n2-Quilômetros para Metros\n"))
            cliente.send(str(c).encode('utf-8'))
            print(c)

            if c == 1:
                metros = int(input("Digite o valor em M:\n"))
                cliente.send(str(metros).encode('utf-8'))
                valor = cliente.recv(1024)
                receber(valor)

            elif c == 2:
                km = int(input("Digite o valor em Km:\n"))
                cliente.send(str(km).encode('utf-8'))
                valor = cliente.recv(1024)
                receber(valor)



print("saindo..")
a = str(a)
cliente.send(a.encode('utf-8'))
cliente.close()
