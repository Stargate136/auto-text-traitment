import socket
import threading
import logging

LOGGER = logging.getLogger(__name__)


def recv_all(sock, n):
    # Helper function to recv n bytes or return None if EOF is hit
    data = bytearray()
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data.extend(packet)
    return data


def handle_client(conn, addr):
    with conn:
        print(f"Connexion de {addr}")

        while True:
            # Récupération de la longueur du message (par exemple, 4 octets pour un int)
            length_header = recv_all(conn, 4)
            if not length_header:
                break

            # Conversion en int
            message_length = int.from_bytes(length_header, byteorder='big')

            # Récupération du message complet
            data = recv_all(conn, message_length)
            if not data:
                break

            print(f"Reçu de {addr}: {data.decode('utf-8')}")
            conn.sendall(b'Message du serveur: J\'ai bien recu votre message!')

    print(f"Connexion de {addr} fermée.")
    conn.close()


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = '127.0.0.1'  # Adresse locale
    port = 65432  # Port

    server_socket.bind((host, port))
    server_socket.listen()

    print("Serveur en écoute...")

    while True:
        conn, addr = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()


if __name__ == "__main__":
    main()
