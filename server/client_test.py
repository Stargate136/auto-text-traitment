import socket


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = '127.0.0.1'
    port = 65432

    client_socket.connect((host, port))

    try:
        while True:
            message = input("Entrez un message à envoyer (ou 'exit' pour quitter) : ")
            if message == "exit":
                break

            # Préfixe avec la longueur du message
            message_length = len(message.encode())
            client_socket.sendall(message_length.to_bytes(4, byteorder='big'))

            # Envoi du message
            client_socket.sendall(message.encode())

            data = client_socket.recv(1024)
            print(f"Reçu : {data.decode('utf-8')}")

    finally:
        client_socket.close()

if __name__ == "__main__":
    main()