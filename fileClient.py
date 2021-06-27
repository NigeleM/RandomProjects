import socket                   # Import socket module

s = socket.socket()             # Create a socket object
host = '10.0.0.16'     # Get local machine name
port = 60000                  # Reserve a port for your service.

# get hostname and ip address
host = socket.gethostname()
ip = socket.gethostbyname(host)
print(host)
print(ip)
s.connect((host, port))
s.send(bytes("Hello server!","utf-8"))

with open('key.txt', 'wb') as f:
    print('file opened')
    while True:
        print('receiving data...')
        data = s.recv(1024)
        print('data=%s', (data))
        if not data:
            break
        # write data to a file
        f.write(data)

f.close()
print('Successfully get the file')
s.bind
print('connection closed')
