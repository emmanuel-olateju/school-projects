import oscpy
from oscpy.server import OSCThreadServer
from time import sleep

osc=OSCThreadServer()
sock=osc.listen(address='127.0.0.1', port=9002, default=True)

@osc.address(b'/data')
def callback(A1A,A2A,A3A,A4A,A4B,A3B,A2B,A1B,B1A,B2A,B3A,B4A,B4B,B3B,B2B,B1B):
    data=[A1A,A2A,A3A,A4A,A4B,A3B,A2B,A1B,B1A,B2A,B3A,,B4A,,B4B,B3B,B2B,B1B]

sleep(1000)
osc.stop()



