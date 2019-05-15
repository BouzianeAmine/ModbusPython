from interface import implements, Interface
from pyModbusTCP.client import ModbusClient
import serial 

ICPCON="192.168.2.250"
PORT=502
myZwave="/dev/ttyACM0"

class Connect(Interface):

    def connection(self):
        pass



class Tcp(implements(Connect)):

    def connection(self):
        return ModbusClient(host=ICPCON,port=PORT,auto_open=True,auto_close=True)


class Serial(implements(Connect)):

    def connection(self):
        return serial.Serial(port=myZwave,baudrate=9600,parity=serial.PARITY_ODD);
    



print(Tcp().connection())
