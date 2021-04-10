
# python imports
import time
import socket

header = b'''\
HTTP/1.1 200 OK\r\n\
Connection: keep-alive\r\n\
Content-Type: text/html\r\n\
Content-Length: 600\r\n\
\r\n\
''' 
data = bytes('<h1>Welcome To The Web Server<h1>', 'utf-8')

#----------------------------
# Set Your Own IP & Port
IP = '192.168.43.39'
port = 8000
#----------------------------

if __name__ == '__main__':
    print(f'\n\t\t Web Server is Running at   {IP}:{port}')
    server_address = (IP, port)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    server.bind(server_address)
    server.listen(5)
    while True:
        try:
            client, client_address = server.accept()
            with client:
                msg = client.recv(1024)
                try:    filename = msg.split()[1][1:]
                except: filename = 'None'
                try:
                    msg = msg.decode('utf-8')
                    msg = str(msg).split('\r\n')
                    print('\n ------------ Client Request ------------')
                    for m in msg: print(m)
                    print('\t----------------------------')
                except: pass
                try:
                    f = open(filename)
                    outputdata = f.read()
                    data = bytes(outputdata, 'utf-8')
                    f.close()
                    print('Filename: ', filename)
                except Exception:   pass
                client.sendall(header + data)
                time.sleep(5)  # To Keep the socket open for a little longer.
                client.shutdown(socket.SHUT_RDWR)
        except KeyboardInterrupt:   break

