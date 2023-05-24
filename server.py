import socket
import threading
import telnetlib

HOST = 'localhost'
PORT = 23

def handle_client(conn):
    tn = telnetlib.Telnet()
    tn.sock = conn
    while True:
        data = tn.read_some()
        if data.decode() == "exit":
            break
        tn.write(data)


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f'Server started on {HOST}:{PORT}')

    while True:
        conn, addr = server_socket.accept()
        print(f'Connected by {addr}')
        client_handler = threading.Thread(target=handle_client, args=(conn,))
        client_handler.start()

if __name__ == '__main__':
    main()
