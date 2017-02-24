from socket import socket, AF_INET, SOCK_STREAM


server_port = 12000
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', server_port))
server_socket.listen(1)
print('The server is ready to receive')
while True:
    connection_socket, client_address = server_socket.accept()
    sentence = connection_socket.recv(2048)
    modified_sentence = sentence.upper()
    connection_socket.send(modified_sentence)
    connection_socket.close()
