import requests
import socket
import os
MEDIA_DIR = ''


class PartGenerator():
    def __init__(self, url, numberOfComputers):
        self.numberOfComputers = numberOfComputers
        self.part = []
        self.downloadSize = self.fetchFileSize(url)
        self.generateParts()
        super().__init__()

    def fetchFileSize(self, url):
        r = requests.get(url, stream=True)
        return int(r.headers['Content-Length'])

    def generateParts(self):
        partSize = self.downloadSize//self.numberOfComputers
        reminder = self.downloadSize % self.numberOfComputers

        start = 0
        end = partSize - 1
        for _ in range(self.numberOfComputers - 1):
            self.part.append((start, end))
            end = end + partSize
            start = end - partSize + 1
        
        self.part.append((start, end + reminder + 1))

    def getNextRange(self):
        for start, end in self.part:
            yield (start, end)





class PDServer():
    def __init__(self, url, numberOfComputers = 3, PORT=1111):
        self.PORT = PORT
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(('0.0.0.0', PORT))
        self.socket.listen(10)
        self.url = url
        self.partGenerator = PartGenerator(url, numberOfComputers)
        self.totalPart = 0
        self.logFile = open(os.path.join(MEDIA_DIR, 'parts.txt'), 'w')
        super().__init__()


    def sendRequestToClients(self):
        for start, end in self.partGenerator.getNextRange():
            self.totalPart += 1
            client, addr = self.socket.accept()      
            print("[+] Sending download request to %s" % str(addr))
            client.send(f"0\n{start}\n{end}\n{self.url}\r".encode())
            self.logFile.write(f'{start}-{end}\n')

    def recv(self):
        data = ""
        c = self.client.recv(1).decode()
        data += c
        while c != '\r':
            c = self.client.recv(1).decode()
            data += c
        print(data)
        return data

    def reciveDownloadParts(self):
        part = 0
        self.totalPart = 3
        while part < self.totalPart:
            client, addr = self.socket.accept() 
            self.client = client     
            print("[+] reciving downloaded part from %s" % str(addr))
            data = self.recv()
            data = data.split('\n')
            size = -1
            try:
                if int(data[0]) == 1:
                    size = int(data[1])
            except:
                print("Error Occured")

            if size == -1:
                continue
            
            with open(os.path.join(MEDIA_DIR, f'{part}'), 'wb') as f:
                f.write(self.client.recv(size))
                f.close()
            part += 1

    def close(self):
        self.logFile.close()
        self.socket.close()
if __name__ == '__main__':
    fileDownloadUrl = 'http://dl176.zlibcdn.com/dtoken/be626fe13dfe585329ef41974856527d'
    server = PDServer(fileDownloadUrl, PORT=5555)
    try:
        print("[+] Waiting for clients to connect....")
        server.sendRequestToClients()
    except:
        print("ERROR OCCURED 97")
    finally:
        server.close()
    
    
    # server = PDServer(fileDownloadUrl, PORT=5555)
    # try:
    #     server.reciveDownloadParts()
    # except Exception as e:
    #     server.close()
    #     raise e
    # finally:
    #     server.close()
    




























# import socket
# PORT = 1111

# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# sock.bind(('0.0.0.0', PORT))
# sock.listen(5)

# while True:
#     clientsocket,addr = sock.accept()      
#     print("[+] a connection from %s" % str(addr))
#     data = ""
#     c = clientsocket.recv(1).decode()
#     data += c
#     while c != '\r':
#         c = clientsocket.recv(1).decode()
#         data += c
#     print(data)











# import socket
# class Request():
#     def __init__(self, host):
#         self.host = host
#         self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         self.s.connect((host, 80))
#         super().__init__()
#     def get(self, path, headers={}):
#         req = f"GET HTTP/1.1\r\nHost: {self.host}\r\n"
#         for key, val in headers.items():
#             req = req + f'{key}: {val}\r\n'
#         print(req)
#         input()
#         self.s.send(str(req + '\n').encode())
#         return self.s.recv(300).decode()
