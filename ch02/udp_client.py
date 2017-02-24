from socket import socket, AF_INET, SOCK_DGRAM


server_name = '121.42.62.137'
server_port = 12000
client_socket = socket(AF_INET, SOCK_DGRAM)
message = input('Input lowercase sentence:')
client_socket.sendto(message.encode('utf-8'), (server_name, server_port))

modified_message, server_address = client_socket.recvfrom(2048)
print(modified_message)
client_socket.close()
