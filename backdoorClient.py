import socket

SRV_ADDR = input("IP: ")
SRV_PORT = int(input("puerto: "))

def print_menu():
    print("""\n\n0) Cierra la conexion
     1) obtiene informacion del sistema
     2) lista el contenido del directorio""")

print_menu()
my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_sock.connect((SRV_ADDR, SRV_PORT))
while 1:
    message = input("\n-Selecciona una opcion: ")
    if(message == "0"):
        my_sock.sendall(message.encode())
        my_sock.close()
        break
    elif(message =="1"):
        my_sock.sendall(message.encode())
        data = my_sock.recv(1024)
        if not data: break
        print(data.decode('utf-8'))
    elif(message =="2"):
        path = input("inserta la ruta: ")
        my_sock.sendall(message.encode())
        my_sock.sendall(path.encode())
        data = my_sock.recv(1024)
        data = data.decode('utf-8').split(",")
        print("*"*40)
        for x in data:
            print(x)
        print("*"*40)

