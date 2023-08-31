import socket
import threading


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))

    def _handle_client(self, conn, addr):
        with conn:
            while True:
                length_header = self._recv_all(conn, 4)
                if not length_header:
                    break

                message_length = int.from_bytes(length_header, byteorder='big')
                data = self._recv_all(conn, message_length)
                if not data:
                    break

                print(f"Reçu de {addr}: {data.decode('utf-8')}")
                conn.sendall(b'Message du serveur: J\'ai bien recu votre message!')

        print(f"Connexion de {addr} fermée.")

    def _recv_all(self, sock, n):
        data = bytearray()
        while len(data) < n:
            packet = sock.recv(n - len(data))
            if not packet:
                return None
            data.extend(packet)
        return data

    def start(self):
        self.server_socket.listen()
        print("Serveur en écoute...")
        while True:
            conn, addr = self.server_socket.accept()
            client_thread = threading.Thread(target=self._handle_client, args=(conn, addr))
            client_thread.start()

    def stop(self):
        self.server_socket.close()