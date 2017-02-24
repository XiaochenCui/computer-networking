from socket import socket, AF_INET, SOCK_STREAM


server_name = '121.42.62.137'
server_port = 12000
client_socket = socket(AF_INET, SOCK_STREAM)

client_socket.connect((server_name, server_port))
sentence = input('Input lowercase sentence:')
client_socket.send(sentence.encode('utf-8'))

modified_sentence = client_socket.recv(2048)
print('From server:', modified_sentence)
client_socket.close()
