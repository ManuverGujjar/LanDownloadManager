import socket
from PDDownloader import downloadFile

class PDClient():
    def __init__(self, IP = '127.0.0.1' , PORT=1111):
        self.PORT = PORT
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((IP, PORT))
        print(f"[+] Connected to {IP}:{PORT}")
        self.start = -1
        self.end = -1
        super().__init__()
    
    def recv(self):
        data = ""
        c = self.socket.recv(1).decode()
        data += c
        while c != '\r':
            c = self.socket.recv(1).decode()
            data += c
        print(data)
        return data

    def reciveDownloadRequest(self):
        data = self.recv().split('\n')
        start = 0
        end = 0
        url = ''
        print(data)
        input()
        try:
            if int(data[0]) == 0:
                start = int(data[1])
                end = int(data[2])
                url = data[3][:-1]
        except:
            print("Error")
        print(start, end, url)
        input()
        return (start, end, url)

    def sendFile(self, fileName):
        with open(fileName, 'rb') as f:
            data = f.read()
            self.socket.send(f'1\n{len(data)}\r'.encode())
            self.socket.send(data)


from Info import PORT, IP

if __name__ == '__main__':
    pdClient = PDClient(PORT=PORT, IP=IP)
    start, end, url = pdClient.reciveDownloadRequest()
    downloadFile(url, f'{start}', headers={'Range' : f'bytes={start}-{end}'})
    # inp = input("Send File Now ? y/n : ")
    # if inp == 'y':
    #     start = input('File : ')
    #     pdClient = PDClient(PORT=5555)
    #     pdClient.sendFile(f'{start}')