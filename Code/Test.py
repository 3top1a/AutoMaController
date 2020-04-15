import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.close()
    s.bind(("127.0.0.1", 6667))
    s.close()
    s.listen()
    s.close()
    conn, addr = s.accept()
    with conn:
        print(addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(data)