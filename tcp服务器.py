import socket
def main():
    while True:
        #1.创建套接字
        tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #2.绑定端口
        tcp_server_socket.bind(('',7890))
        #3.设置监听
        tcp_server_socket.listen(128)
        #4.等待客户端的链接
        new_client_socket,client_addr = tcp_server_socket.accept()
        print(client_addr)
        #接收客户端发过来的请求
        recv_data = new_client_socket.recv(1024)
        print(recv_data.decode('utf-8'))
        #回复客户端信息
        new_client_socket.send(input('回复客户端:').encode('utf-8'))
        #关闭套接字
        new_client_socket.close()
        tcp_server_socket.close()

if __name__ == '__main__':
    main()