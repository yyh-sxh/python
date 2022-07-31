import socket
if __name__ == '__main__':
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
    tcp_server_socket.bind(("",8000))
    tcp_server_socket.listen(128)

    while True:
        new_socket,ip_prot = tcp_server_socket.accept()

        recv_data = new_socket.recv(4096)

        print(recv_data)


        with open('dist/index.html','r') as file:
            file_data = file.read()

        resp_line = "HTTP/101 200 OK \r\n"
        resp_header = "Server: PWS/1.0\r\n"
        resp_body = file_data

        resp = resp_line + resp_header + '\r\n' + resp_body

        resp_data = resp.encode('gbk')
        new_socket.send(resp_data)
        new_socket.close()
