import socket

def main():
    while True:
        tcp_client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #服务器地址端口
        server_ip = '192.168.108.29'
        server_port = 7788
        server_addr = (server_ip,server_port)

        tcp_client_socket.connect(server_addr)
        file_name = input('请输入需要下载的文件名:')
        tcp_client_socket.send(file_name.encode('utf-8'))
        recv_data = tcp_client_socket.recv(1024)
        # print(recv_data.decode('utf-8'))
        if recv_data:
            with open('新'+ file_name,'wb') as f:
                f.write(recv_data)
        tcp_client_socket.close()

if __name__ == '__main__':
    main()