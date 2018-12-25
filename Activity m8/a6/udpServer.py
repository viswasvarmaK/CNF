import socket

def main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    print("Server Started.")

    while True:
        data, addr = s.recvfrom(1024)
        data = data.decode()
        if not data:
            break
        print("from connected user: " + str(data))
        data = str(data)
        con = data.upper()
        print("Sending data: " + str(con))
        s.sendto(str(con).encode(),addr)
    s.close()

if __name__ == "__main__":
    main()
