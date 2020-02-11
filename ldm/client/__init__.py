import socket

class LDMClient():
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



from .. import requests
from ldm.config import MEDIA_DIR
import os


def downloadFile(url, localName, headers={}, chunksize = 1024*1024):
    localName = os.path.join(MEDIA_DIR, localName)
    r = requests.get(url, stream=True)
    f = open(localName, 'wb')
    print(r.headers)
    file_size = int(r.headers['Content-Length'])
    # print(file_size)
    # num_bars = file_size / chunksize
    # bar =  progressbar.ProgressBar(maxval=num_bars).start()
    i = 0
    downloadedSize = 0
    prePer = -1
    for chunk in r.iter_content(chunk_size=chunksize):
        f.write(chunk)
        f.close()
        f = open(localName, 'ab')
        downloadedSize += len(chunk)
        log = open('log', 'w')
        log.write(str(downloadedSize))
        log.close()
        i+=(chunksize)
        try:
            
            per = int((i/file_size)*100)
            if per != prePer:
                print(per if per <= 100 else 100)
            prePer = per
        except:
            pass
    print(100 if per < 100 else '')
    f.close()
    return

    # inp = input("Send File Now ? y/n : ")
    # if inp == 'y':
    #     start = input('File : ')
    #     pdClient = PDClient(PORT=5555)
    #     pdClient.sendFile(f'{start}')