import socket

def main():
    while True:
        #创建套接字
        tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #连接服务器
        server_ip = '192.168.108.29'
        server_port = 7890
        server_addr = (server_ip,server_port)
        tcp_socket.connect(server_addr)
        #发送数据
        send_data = input('发往服务器:')
        tcp_socket.send(send_data.encode('utf-8'))
        #/接收数据
        recv_data = tcp_socket.recv(1024)
        print(recv_data.decode('utf-8'))
        #关闭套接字
        tcp_socket.close()

if __name__ == '__main__':
    main()