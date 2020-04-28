#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
from pyModbusTCP.client import ModbusClient
import serial 
import os
import db
import Mode
ICPCON=""
PORT=502
myZwave="/dev/ttyACM0"

class MyModbus:
	def __init__(self,mode):
		if mode=="tcp":
			self.etat=mode
			self.client=ModbusClient(host=ICPCON,port=PORT,auto_open=True,auto_close=True)
			self.db=db.Mydb()
			print("---"+self.etat+" configuration---");
		else :
			self.etat=mode;
			self.client=serial.Serial(port=myZwave,baudrate=9600,parity=serial.PARITY_ODD);
			self.db=db.Mydb()
			print("---"+self.etat+" configuration---");
			if self.client.isOpen():
				os.system(r'echo -ne "\x01\x08\x00\xF2\x51\x01\x00\x05\x01\x51" > /dev/ttyACM0')
			else : 
				print("Didn't stop the light")
		return
			
	def readCoils(self,min=None,max=None):
		if self.etat=="tcp":
			coils=self.client.read_holding_registers(min,max)
			if coils:
				print(coils);
				self.db.insert(coils[0],coils[1]);
			else:
				print("error : read not ok")
		else:
			bits=self.client.read(max)
			if bits:
				print(bits);
				#self.db.insert(bits[0],bits[1]);
			else:
				print("error : read not ok")
		return

	def writeCoils(self,to,data):

		if self.client.write_multiple_registers(to,data): #write_single_coil
			print(" write done ")
		else :
			print("error : write not ok")		
		return

	

client=MyModbus("rtu");
print(client.client)
#client.readCoils(0,10);
#client.writeCoils(0,[0,0]);
#client.readCoils(0,10);



#print(client.client.is_open()) #false à cause de auto_close
