import socket, sys, time

#TODO: server connection timeout, TLS/SSL, shell argument support

INET = '192.168.0.27'
PORT = 13337

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (INET, PORT)
print('Connecting to %s:%s' %server_address)
sock.connect(server_address)

try:
    while True:# Send data
        message = input("Enter input: ")
        print('sending...')
        b = message.encode('utf-8')
        sock.sendall(b)

        # Look for the response
        amount_received = 0
        amount_expected = len(message)
        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print('Received "%s"' % data)

finally:
    print('Closing socket')
    sock.close()
