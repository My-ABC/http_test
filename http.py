import socket
import threading
import os

def handle_client(c, addr):
    print(addr, "connected.")
    
    with c:
        request = c.recv(1024)
        
        headers = request.split(b"\r\n")
        file = headers[0].split()[1].decode()
        
        if file == "/":
            file = "index.html"
        elif file == "/a":
            file = "a.html"
        elif file == "/a/b.html":
            file = "a/b.html"
        elif file == "/a/c.html":
            file = "a/c.html"
        
        try:
            with open(file, "rb") as f:
                content = f.read()
            response = b"HTTP/1.0 200 OK\r\n\r\n" + content

        except FileNotFoundError:
            response = b"HTTP/1.0 404 Not Found\r\n\r\n"
        
        c.sendall(response)
        
if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 81))
        s.listen()
        
        while True:
            c, addr = s.accept()
            
            t = threading.Thread(target=handle_client, args=(c, addr))
            t.start()