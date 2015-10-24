# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AVR_Serial.ui'
#
# Created: Thu Jun  4 00:33:21 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from AVR_Serial import AvrSerial
import serial

byte_size_list = [serial.FIVEBITS, serial.SIXBITS, serial.SEVENBITS, serial.EIGHTBITS]
stop_bits_list = [serial.STOPBITS_ONE, serial.STOPBITS_TWO]
parity_bits_list = [serial.PARITY_NONE, serial.PARITY_EVEN, serial.PARITY_ODD]

avr = AvrSerial()

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(798, 354)
        self.connection_grp = QtGui.QGroupBox(Form)
        self.connection_grp.setGeometry(QtCore.QRect(0, 0, 781, 106))
        self.connection_grp.setObjectName(_fromUtf8("connection_grp"))
        self.layoutWidget = QtGui.QWidget(self.connection_grp)
        self.layoutWidget.setGeometry(QtCore.QRect(250, 60, 294, 29))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_9.setMargin(0)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.connect_btn = QtGui.QPushButton(self.layoutWidget)
        self.connect_btn.setObjectName(_fromUtf8("connect_btn"))
        self.horizontalLayout_9.addWidget(self.connect_btn)
        self.connect_status_lbl = QtGui.QLabel(self.layoutWidget)
        self.connect_status_lbl.setObjectName(_fromUtf8("connect_status_lbl"))
        self.horizontalLayout_9.addWidget(self.connect_status_lbl)
        self.disconnect_btn = QtGui.QPushButton(self.layoutWidget)
        self.disconnect_btn.setEnabled(False)
        self.disconnect_btn.setObjectName(_fromUtf8("disconnect_btn"))
        self.horizontalLayout_9.addWidget(self.disconnect_btn)
        self.port_sel = QtGui.QComboBox(self.connection_grp)
        self.port_sel.setGeometry(QtCore.QRect(54, 31, 121, 27))
        self.port_sel.setObjectName(_fromUtf8("port_sel"))

        self.port_sel.addItem(_fromUtf8(""))
        self.port_sel.setItemText(0, _fromUtf8("/dev/ttyACM0"))
        self.port_sel.addItem(_fromUtf8(""))
        self.port_sel.setItemText(1, _fromUtf8("/dev/ttyACM1"))
        self.port_sel.addItem(_fromUtf8(""))
        self.port_sel.setItemText(2, _fromUtf8("/dev/ttyACM2"))
        self.port_sel.addItem(_fromUtf8(""))
        self.port_sel.setItemText(3, _fromUtf8("/dev/ttyACM3"))
        self.port_sel.addItem(_fromUtf8(""))
        self.port_sel.setItemText(4, _fromUtf8("/dev/ttyACM4"))
        self.port_sel.addItem(_fromUtf8(""))
        self.port_sel.setItemText(5, _fromUtf8("/dev/ttyACM5"))
        self.port_sel.addItem(_fromUtf8(""))
        self.port_sel.setItemText(6, _fromUtf8("/dev/ttyACM6"))
        self.port_sel.addItem(_fromUtf8(""))
        self.port_sel.setItemText(7, _fromUtf8("/dev/ttyACM7"))
        self.port_sel.addItem(_fromUtf8(""))
        self.port_sel.setItemText(8, _fromUtf8("/dev/ttyACM8"))
        self.port_sel.addItem(_fromUtf8(""))
        self.port_sel.setItemText(9, _fromUtf8("/dev/ttyUSB0"))
        self.layoutWidget1 = QtGui.QWidget(self.connection_grp)
        self.layoutWidget1.setGeometry(QtCore.QRect(340, 31, 146, 29))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.layoutWidget1)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.bits_per_frame_sel = QtGui.QComboBox(self.layoutWidget1)
        self.bits_per_frame_sel.setObjectName(_fromUtf8("bits_per_frame_sel"))
        self.bits_per_frame_sel.addItem(_fromUtf8(""))
        self.bits_per_frame_sel.setItemText(0, _fromUtf8("5"))
        self.bits_per_frame_sel.addItem(_fromUtf8(""))
        self.bits_per_frame_sel.setItemText(1, _fromUtf8("6"))
        self.bits_per_frame_sel.addItem(_fromUtf8(""))
        self.bits_per_frame_sel.setItemText(2, _fromUtf8("7"))
        self.bits_per_frame_sel.addItem(_fromUtf8(""))
        self.bits_per_frame_sel.setItemText(3, _fromUtf8("8"))
        self.bits_per_frame_sel.addItem(_fromUtf8(""))

        self.horizontalLayout_2.addWidget(self.bits_per_frame_sel)
        self.layoutWidget2 = QtGui.QWidget(self.connection_grp)
        self.layoutWidget2.setGeometry(QtCore.QRect(650, 30, 128, 29))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_4 = QtGui.QLabel(self.layoutWidget2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        self.parity_sel = QtGui.QComboBox(self.layoutWidget2)
        self.parity_sel.setObjectName(_fromUtf8("parity_sel"))
        self.parity_sel.addItem(_fromUtf8(""))
        self.parity_sel.setItemText(0, _fromUtf8("NONE"))
        self.parity_sel.addItem(_fromUtf8(""))
        self.parity_sel.setItemText(1, _fromUtf8("EVEN"))
        self.parity_sel.addItem(_fromUtf8(""))
        self.parity_sel.setItemText(2, _fromUtf8("ODD"))
        self.horizontalLayout_3.addWidget(self.parity_sel)
        self.label = QtGui.QLabel(self.connection_grp)
        self.label.setGeometry(QtCore.QRect(10, 36, 40, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.layoutWidget3 = QtGui.QWidget(self.connection_grp)
        self.layoutWidget3.setGeometry(QtCore.QRect(490, 30, 146, 29))
        self.layoutWidget3.setObjectName(_fromUtf8("layoutWidget3"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_5 = QtGui.QLabel(self.layoutWidget3)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout.addWidget(self.label_5)
        self.stop_bits_sel = QtGui.QComboBox(self.layoutWidget3)
        self.stop_bits_sel.setObjectName(_fromUtf8("stop_bits_sel"))
        self.stop_bits_sel.addItem(_fromUtf8(""))
        self.stop_bits_sel.setItemText(0, _fromUtf8("1"))
        self.stop_bits_sel.addItem(_fromUtf8(""))
        self.stop_bits_sel.setItemText(1, _fromUtf8("2"))
        self.horizontalLayout.addWidget(self.stop_bits_sel)
        self.layoutWidget4 = QtGui.QWidget(self.connection_grp)
        self.layoutWidget4.setGeometry(QtCore.QRect(180, 30, 155, 29))
        self.layoutWidget4.setObjectName(_fromUtf8("layoutWidget4"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_2 = QtGui.QLabel(self.layoutWidget4)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_4.addWidget(self.label_2)
        self.baudrate_sel = QtGui.QComboBox(self.layoutWidget4)
        self.baudrate_sel.setObjectName(_fromUtf8("baudrate_sel"))
        self.baudrate_sel.addItem(_fromUtf8(""))
        self.baudrate_sel.setItemText(0, _fromUtf8("300"))
        self.baudrate_sel.addItem(_fromUtf8(""))
        self.baudrate_sel.setItemText(1, _fromUtf8("1200"))
        self.baudrate_sel.addItem(_fromUtf8(""))
        self.baudrate_sel.setItemText(2, _fromUtf8("2400"))
        self.baudrate_sel.addItem(_fromUtf8(""))
        self.baudrate_sel.setItemText(3, _fromUtf8("4800"))
        self.baudrate_sel.addItem(_fromUtf8(""))
        self.baudrate_sel.setItemText(4, _fromUtf8("9600"))
        self.baudrate_sel.addItem(_fromUtf8(""))
        self.baudrate_sel.setItemText(5, _fromUtf8("14400"))
        self.baudrate_sel.addItem(_fromUtf8(""))
        self.baudrate_sel.setItemText(6, _fromUtf8("19200"))
        self.baudrate_sel.addItem(_fromUtf8(""))
        self.baudrate_sel.setItemText(7, _fromUtf8("28800"))
        self.baudrate_sel.addItem(_fromUtf8(""))
        self.baudrate_sel.setItemText(8, _fromUtf8("38400"))
        self.baudrate_sel.addItem(_fromUtf8(""))
        self.baudrate_sel.setItemText(9, _fromUtf8("57600"))
        self.baudrate_sel.addItem(_fromUtf8(""))
        self.baudrate_sel.setItemText(10, _fromUtf8("115200"))
        self.horizontalLayout_4.addWidget(self.baudrate_sel)
        self.tx_rx_grp = QtGui.QGroupBox(Form)
        self.tx_rx_grp.setEnabled(False)
        self.tx_rx_grp.setGeometry(QtCore.QRect(10, 120, 771, 91))
        self.tx_rx_grp.setObjectName(_fromUtf8("tx_rx_grp"))
        self.layoutWidget5 = QtGui.QWidget(self.tx_rx_grp)
        self.layoutWidget5.setGeometry(QtCore.QRect(230, 30, 311, 56))
        self.layoutWidget5.setObjectName(_fromUtf8("layoutWidget5"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.layoutWidget5)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_6 = QtGui.QLabel(self.layoutWidget5)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_11.addWidget(self.label_6)
        self.send_char = QtGui.QLineEdit(self.layoutWidget5)
        self.send_char.setObjectName(_fromUtf8("send_char"))
        self.send_char.setMaxLength(1)  # my code send single character :SUCCESS
        self.horizontalLayout_11.addWidget(self.send_char)
        self.send_btn = QtGui.QPushButton(self.layoutWidget5)
        self.send_btn.setEnabled(False)
        self.send_btn.setObjectName(_fromUtf8("send_btn"))
        self.horizontalLayout_11.addWidget(self.send_btn)
        self.verticalLayout_5.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.label_7 = QtGui.QLabel(self.layoutWidget5)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_12.addWidget(self.label_7)
        self.received_AVR_lbl = QtGui.QLabel(self.layoutWidget5)
        self.received_AVR_lbl.setText(_fromUtf8(""))
        self.received_AVR_lbl.setObjectName(_fromUtf8("received_AVR_lbl"))
        self.horizontalLayout_12.addWidget(self.received_AVR_lbl)
        self.verticalLayout_5.addLayout(self.horizontalLayout_12)
        self.commander_grp = QtGui.QGroupBox(Form)
        self.commander_grp.setEnabled(False)
        self.commander_grp.setGeometry(QtCore.QRect(10, 220, 781, 121))
        self.commander_grp.setObjectName(_fromUtf8("commander_grp"))
        self.layoutWidget6 = QtGui.QWidget(self.commander_grp)
        self.layoutWidget6.setGeometry(QtCore.QRect(300, 30, 180, 54))
        self.layoutWidget6.setObjectName(_fromUtf8("layoutWidget6"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.layoutWidget6)
        self.verticalLayout_6.setMargin(0)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.commander_status_lbl = QtGui.QLabel(self.layoutWidget6)
        self.commander_status_lbl.setText(_fromUtf8(""))
        self.commander_status_lbl.setObjectName(_fromUtf8("commander_status_lbl"))
        self.verticalLayout_6.addWidget(self.commander_status_lbl)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.on_btn = QtGui.QPushButton(self.layoutWidget6)
        self.on_btn.setObjectName(_fromUtf8("on_btn"))
        self.horizontalLayout_13.addWidget(self.on_btn)
        self.off_btn = QtGui.QPushButton(self.layoutWidget6)
        self.off_btn.setObjectName(_fromUtf8("off_btn"))
        self.horizontalLayout_13.addWidget(self.off_btn)
        self.verticalLayout_6.addLayout(self.horizontalLayout_13)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.connect_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.serialConnect)
        QtCore.QObject.connect(self.disconnect_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.serialDisconnect)
        QtCore.QObject.connect(self.send_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.serialSend)
        QtCore.QObject.connect(self.on_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.ledOn)
        QtCore.QObject.connect(self.off_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.ledOff)
        QtCore.QObject.connect(self.send_char, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.send_btn.animateClick)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def serialConnect(self):
        print 'Connect pressed'
        print self.port_sel.currentText()
        print self.baudrate_sel.currentText()
        print byte_size_list[self.bits_per_frame_sel.currentIndex()]
        print stop_bits_list[self.stop_bits_sel.currentIndex()]
        print parity_bits_list[self.parity_sel.currentIndex()]
        status = avr.connect(str(self.port_sel.currentText()), int(self.baudrate_sel.currentText()), byte_size_list[self.bits_per_frame_sel.currentIndex()], stop_bits_list[self.stop_bits_sel.currentIndex()], parity_bits_list[self.parity_sel.currentIndex()])
        if status is True:
            self.disconnect_btn.setEnabled(True)
            self.tx_rx_grp.setEnabled(True)
            self.commander_grp.setEnabled(True)
            self.send_btn.setEnabled(True)
            self.on_btn.setEnabled(True)
            self.off_btn.setEnabled(False)
            self.connect_status_lbl.setText('Connected')
            print status
            self.connect_btn.setEnabled(False)
        else:
            self.connect_status_lbl.setText('Failed')
            print status

    def serialDisconnect(self):
        print 'Disconnect pressed'
        status = avr.disconnect()
        if status is True:
            self.disconnect_btn.setEnabled(False)
            self.tx_rx_grp.setEnabled(False)
            self.commander_grp.setEnabled(False)
            self.connect_btn.setEnabled(True)

            self.connect_status_lbl.setText('Disconnected')
        else:
            self.connect_status_lbl.setText('failed')
            print status

    def serialSend(self):
        print 'Sending something'

        status = avr.send(str(self.send_char.text()))
        if status is True:
            self.send_char.clear()
            char = avr.receive()
            if char is not False:
                self.received_AVR_lbl.setText('Received '+char)
            else:
                self.received_AVR_lbl.setText('Failed')

    def ledOn(self):
        print 'LED ON'
        status = avr.send('1')
        if status is True:
            self.on_btn.setEnabled(False)
            self.off_btn.setEnabled(True)
        else:
            self.received_AVR_lbl.setText('Failed')
        pass

    def ledOff(self):
        print 'LED OFF'
        status = avr.send('0')
        if status is True:
            self.on_btn.setEnabled(True)
            self.off_btn.setEnabled(False)
        else:
            self.received_AVR_lbl.setText('Failed')
        pass

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "AVR Serial", None))
        self.connection_grp.setTitle(_translate("Form", "Connection Parameters", None))
        self.connect_btn.setText(_translate("Form", "Connect", None))
        self.connect_status_lbl.setText(_translate("Form", "NO Connection", None))
        self.disconnect_btn.setText(_translate("Form", "Disconnect", None))
        self.label_3.setText(_translate("Form", "Data bits", None))
        self.label_4.setText(_translate("Form", "Parity", None))
        self.label.setText(_translate("Form", "PORT", None))
        self.label_5.setText(_translate("Form", "Stop bits", None))
        self.label_2.setText(_translate("Form", "Baud Rate", None))
        self.tx_rx_grp.setTitle(_translate("Form", "Serial Communication", None))
        self.label_6.setText(_translate("Form", "SEND", None))
        self.send_btn.setText(_translate("Form", "SEND", None))
        self.label_7.setText(_translate("Form", "Received", None))
        self.commander_grp.setTitle(_translate("Form", "Commander", None))
        self.on_btn.setText(_translate("Form", "ON", None))
        self.off_btn.setText(_translate("Form", "OFF", None))


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
