import requests

def downloadFile(url, localName, headers={}, chunksize = 1024):
    local_filename = localName
    r = requests.get(url, stream=True)
    f = open(local_filename, 'wb')
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