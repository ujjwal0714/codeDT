# cmd : pip install pyqrcode
# cmd : pip install pypng

import pyqrcode as qr
from pyqrcode import QRCode
import png
import os

def file_name():
    l=[]
    for i in os.listdir():
        if i.endswith(".png"):
            l.append(int(i.replace(".png","")))
    if l==[]:
        return(1)
    else:
        return(max(l)+1)
    
def create_qr():
    _=input("Enter Text: \n")
    url=qr.create(str(_))
    url.png("{}.png".format(str(file_name())),scale=5)
    os.startfile("{}.png".format(str(file_name()-1)))

while True:
    create_qr()
