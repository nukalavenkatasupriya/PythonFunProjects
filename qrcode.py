import pyqrcode

def qrcode():
    q=pyqrcode.create(input())
    q.svg('qrcode.png',scale=6)
    print('QR Generated')
if __name__=='__main__':
    qrcode()