import os
PORT = 1111
IP = '127.0.0.1'
URL = 'http://dl176.zlibcdn.com/dtoken/be626fe13dfe585329ef41974856527d'
MEDIA_DIR = os.path.join(os.getcwd(), 'temp')
if not os.path.exists(MEDIA_DIR):
    os.makedirs(MEDIA_DIR)
FILE_NAME = 'Nothing'