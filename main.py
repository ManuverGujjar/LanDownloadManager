import sys

from ldm.config import PORT, URL, IP
from ldm.server import LDMServer
from ldm.client import LDMClient, downloadFile

if len(sys.argv) == 1:
    pdClient = PDClient(PORT=PORT, IP=IP)
    start, end, url = pdClient.reciveDownloadRequest()
    downloadFile(url, f'{start}', headers={'Range' : f'bytes={start}-{end}'})



if len(sys.argv) > 1:
    server = LDMServer(URL, PORT=PORT)
    try:
        print("[+] Waiting for clients to connect....")
        server.sendRequestToClients()
    except:
        print("ERROR OCCURED 97")
    finally:
        server.close()