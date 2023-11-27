from scapy.all import *

def getPackets():
    capture = sniff(count=20)
    capture.show()
    capture.plot(lambda x:len(x))
    
#getPackets()