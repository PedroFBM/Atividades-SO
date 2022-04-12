import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9875

server.bind((host, port))
server.listen()
print("Aguardando Conexão...")
cliente, addr = server.accept()

def enviar(valor):
    cliente.send(str(valor).encode('UTF-8'))
    print(valor)

while True:

    try:
        print("Conexão estabelecida em %s" % str(addr))

        a = cliente.recv(1024)
        a = str(a.decode('utf-8'))
        print(a + ": identificação de tipo de operação recebido com sucesso")
        a = int(a)

        b = cliente.recv(1024)
        b = str(b.decode('utf-8'))
        print(b + ": identificação de tipo de grandeza recebido com sucesso")
        b = int(b)

        c = cliente.recv(1024)
        c = str(c.decode('utf-8'))
        print(c + ": identificação de tipo de calculo recebido com sucesso")
        c = int(c)

        if a == 1:
            if b == 1:
                if c == 1:
                    valor = cliente.recv(1024)
                    valor = float(valor.decode('UTF-8'))
                    print(str(valor) + ": valor em celsius recebido com sucesso")
                    valor += 273
                    enviar(valor)

                elif c == 2:
                    valor = cliente.recv(1024)
                    valor = float(valor.decode('UTF-8'))
                    print(str(valor) + ": valor em Kelvin recebido com sucesso")
                    valor -= 273
                    enviar(valor)

            elif b == 2:
                if c == 1:
                    valor = cliente.recv(1024)
                    valor = float(valor.decode('utf-8'))
                    print(str(valor) + ": valor em Kelvin recebido com sucesso")
                    valor = valor / 1000
                    enviar(valor)

                elif c == 2:
                    valor = cliente.recv(1024)
                    valor = float(valor.decode('utf-8'))
                    print(str(valor) + ": o valor em Km recebido com sucesso")
                    valor = valor * 1000
                    enviar(valor)


    except:
        print("saindo")
        cliente, addr = server.accept()
