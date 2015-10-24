
import serial
import time



class AvrSerial(object):
    def __init__(self):
        self.device = None

    def connect(self, _port='/dev/ttyACM0', _baud=9600, _byte_size=serial.EIGHTBITS, _stopbits = serial.STOPBITS_ONE, _parity = serial.PARITY_NONE):
        try:
            print 'trying...', _port
            self.device = serial.Serial(port=_port, baudrate=_baud, bytesize=_byte_size, parity=_parity, stopbits=_stopbits)

            # self.device.setDTR(level=False) # set the reset signal
            #time.sleep(2)  # wait two seconds, an Arduino needs some time to really reset
            #               # don't do anything here which might overwrite the Arduino's program
            # self.device.setDTR(level=True)  # remove the reset signal, the Arduino will restart
            # selfdevice.flush()
            print self.device.getBaudrate()

            self.device.flushInput()
            return True
        except:
            print "failed to connect on", _port
            return False

    def disconnect(self):
        try:
            self.device.close()
            return True
        except:
            return False

    def send(self, command='String\r\n'):
        try:
            # command += '\r\n'
            print 'from send_command'
            print command
            self.device.flushOutput()
            if self.device.writable():
                self.device.write(command)
            return True
        except:
            print 'failed to send'
            return False

    def receive(self):
        try:
            read = self.device.read()
            self.device.flushInput()
            return read
        except:
            print 'failed to read'
            return False
