class PartGenerator():
    def __init__(self, downloadSize, numberOfComputers):
        self.numberOfComputers = numberOfComputers
        self.part = []
        self.downloadSize = downloadSize
        self.generateParts()
        super().__init__()

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
        
# p = PartGenerator(100, 3)
# for i in p.getNextRange():
#     print(i)

import socket
class Request():
    def __init__(self, host):
        self.host = host
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((host, 80))
        super().__init__()
    def get(self, path, headers={}):
        req = f"GET HTTP/1.1\r\nHost: {self.host}\r\n"
        for key, val in headers.items():
            req = req + f'{key}: {val}\r\n'
        print(req)
        input()
        self.s.send(str(req + '\n').encode())
        return self.s.recv(300).decode()

def fetchFileSize(fileUrl):
    import requests
    crange = requests.get(fileUrl, headers={'Range': 'bytes=0-1000'}).headers.get('Content-Range')
#     import  urllib.parse
#     import http.client
#     URL = urllib.parse.urlparse(fileUrl)

#     # conn = http.client.HTTPSConnection(URL.netloc, timeout=10)
#     print(URL.netloc)
#     print(URL.path)
#     input()
#     print(Request(URL.netloc).get(URL.path, headers={'User-Agent' : 'Mozilla/5.0', 'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
# 'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.4 Safari/605.1.15',
# 'Accept-Language' : 'en-gb',
# 'Accept-Encoding' : 'gzip, deflate',
# 'Connection' : 'keep-alive'}))
    # res = conn.getresponse()
    # crange =  res.getheader('Content-Range')
    size = 0
    i = 0
    while crange[i] != '/':
        i += 1
    i += 1
    while i < len(crange):
        size = (size * 10) + int(crange[i])
        i += 1
    return size

# fileSize = fetchFileSize("http://dl5.jiocloud.link/Movies/Taylor.Swift.Miss.Americana.2020.720p.NF.WEB-DL.x264-KatmovieHD.nl.mkv")
# print(fileSize)
# p = PartGenerator(fileSize, 3)
# for i in p.getNextRange():
#     print(i)

import progressbar
import requests

url = "http://stackoverflow.com/"


def download_file(url, localName, headers={}):
    local_filename = localName
    r = requests.get(url, stream=True, headers=headers)
    f = open(local_filename, 'wb')
    file_size = int(r.headers['Content-Length'])
    chunksize = 1024*1024
    num_bars = file_size / chunksize
    bar =  progressbar.ProgressBar(maxval=num_bars).start()
    i = 0
    downloadedSize = 0
    for chunk in r.iter_content(chunk_size=chunksize):
        f.write(chunk)
        f.close()
        f = open(localName, 'ab')
        downloadedSize += len(chunk)
        log = open('log', 'w')
        log.write(str(downloadedSize))
        log.close()
        try:
            bar.update(i)
        except:
            pass
        i+=(len(chunk)/chunksize)
    f.close()
    return
url = 'http://9092.ultratv100.com:9090/movies/Batch219/The%20Amazing%20Spider%20Man%202%20%282014%29/The%20Amazing%20Spider%20Man%202%20%282014%29.mp4'
download_file("http://www.xiaoguo.net/~books/Program/You_Dont_Know_JS_Up_and_Going.pdf", 'ydkjs.pdf')

(488974648, 733461971)
(733461972, 977949299)
