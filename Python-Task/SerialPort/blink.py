import serial

port = serial.Serial("COM6",9600,timeout=2)

input = raw_input("insert value")
if input =='1':
    port.write('1')
elif input =='0':
    port.write('0')
