import socket

def send_file_2_client(new_client_socket,client_addr):
    file_name = new_client_socket.recv(1024).decode('utf-8')
    print('客户端(%s)请求的文件名:%s'%(str(client_addr),file_name))

    file_content = None
    try:
        f = open(file_name,'rb')
        file_content = f.read()
    except:
        print('没有此文件:%s！'%file_name)

    if file_content:
        # new_client_socket.send('123'.encode('utf-8'))
        new_client_socket.send(file_content)

def main():
    tcp_client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_client_socket.bind(('',7788))
    tcp_client_socket.listen(128)

    while True:
        new_client_socket,client_addr = tcp_client_socket.accept()
        send_file_2_client(new_client_socket,client_addr)

        new_client_socket.close()

    tcp_client_socket.close()

if __name__ == '__main__':
    main()