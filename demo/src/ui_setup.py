# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/setup.ui'
#
# Created: Tue Nov 19 18:33:45 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_Setup(object):
    def setupUi(self, Setup):
        Setup.setObjectName(_fromUtf8("Setup"))
        Setup.resize(501, 326)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(Setup)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(Setup)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.edit_host = QtGui.QLineEdit(Setup)
        self.edit_host.setObjectName(_fromUtf8("edit_host"))
        self.horizontalLayout.addWidget(self.edit_host)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(Setup)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.spinbox_port = QtGui.QSpinBox(Setup)
        self.spinbox_port.setMinimum(1)
        self.spinbox_port.setMaximum(65536)
        self.spinbox_port.setProperty("value", 4223)
        self.spinbox_port.setObjectName(_fromUtf8("spinbox_port"))
        self.horizontalLayout_3.addWidget(self.spinbox_port)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.button_reconnect = QtGui.QPushButton(Setup)
        self.button_reconnect.setObjectName(_fromUtf8("button_reconnect"))
        self.horizontalLayout_4.addWidget(self.button_reconnect)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.line = QtGui.QFrame(Setup)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_12 = QtGui.QLabel(Setup)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout.addWidget(self.label_12, 6, 0, 1, 1)
        self.label_multi_touch_found = QtGui.QLabel(Setup)
        self.label_multi_touch_found.setObjectName(_fromUtf8("label_multi_touch_found"))
        self.gridLayout.addWidget(self.label_multi_touch_found, 2, 1, 1, 1)
        self.label_9 = QtGui.QLabel(Setup)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 3, 0, 1, 1)
        self.label_10 = QtGui.QLabel(Setup)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 4, 0, 1, 1)
        self.label_4 = QtGui.QLabel(Setup)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_5 = QtGui.QLabel(Setup)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)
        self.label_6 = QtGui.QLabel(Setup)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)
        self.label_7 = QtGui.QLabel(Setup)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)
        self.label_8 = QtGui.QLabel(Setup)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)
        self.label_11 = QtGui.QLabel(Setup)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout.addWidget(self.label_11, 5, 0, 1, 1)
        self.label_led_strip_found = QtGui.QLabel(Setup)
        self.label_led_strip_found.setObjectName(_fromUtf8("label_led_strip_found"))
        self.gridLayout.addWidget(self.label_led_strip_found, 1, 1, 1, 1)
        self.label_dual_button1_found = QtGui.QLabel(Setup)
        self.label_dual_button1_found.setObjectName(_fromUtf8("label_dual_button1_found"))
        self.gridLayout.addWidget(self.label_dual_button1_found, 3, 1, 1, 1)
        self.label_dual_button2_found = QtGui.QLabel(Setup)
        self.label_dual_button2_found.setObjectName(_fromUtf8("label_dual_button2_found"))
        self.gridLayout.addWidget(self.label_dual_button2_found, 4, 1, 1, 1)
        self.label_piezo_speaker_found = QtGui.QLabel(Setup)
        self.label_piezo_speaker_found.setObjectName(_fromUtf8("label_piezo_speaker_found"))
        self.gridLayout.addWidget(self.label_piezo_speaker_found, 5, 1, 1, 1)
        self.label_segment_display_found = QtGui.QLabel(Setup)
        self.label_segment_display_found.setObjectName(_fromUtf8("label_segment_display_found"))
        self.gridLayout.addWidget(self.label_segment_display_found, 6, 1, 1, 1)
        self.label_led_strip_uid = QtGui.QLabel(Setup)
        self.label_led_strip_uid.setObjectName(_fromUtf8("label_led_strip_uid"))
        self.gridLayout.addWidget(self.label_led_strip_uid, 1, 2, 1, 1)
        self.label_multi_touch_uid = QtGui.QLabel(Setup)
        self.label_multi_touch_uid.setObjectName(_fromUtf8("label_multi_touch_uid"))
        self.gridLayout.addWidget(self.label_multi_touch_uid, 2, 2, 1, 1)
        self.label_dual_button1_uid = QtGui.QLabel(Setup)
        self.label_dual_button1_uid.setObjectName(_fromUtf8("label_dual_button1_uid"))
        self.gridLayout.addWidget(self.label_dual_button1_uid, 3, 2, 1, 1)
        self.label_dual_button2_uid = QtGui.QLabel(Setup)
        self.label_dual_button2_uid.setObjectName(_fromUtf8("label_dual_button2_uid"))
        self.gridLayout.addWidget(self.label_dual_button2_uid, 4, 2, 1, 1)
        self.label_piezo_speaker_uid = QtGui.QLabel(Setup)
        self.label_piezo_speaker_uid.setObjectName(_fromUtf8("label_piezo_speaker_uid"))
        self.gridLayout.addWidget(self.label_piezo_speaker_uid, 5, 2, 1, 1)
        self.label_segment_display_uid = QtGui.QLabel(Setup)
        self.label_segment_display_uid.setObjectName(_fromUtf8("label_segment_display_uid"))
        self.gridLayout.addWidget(self.label_segment_display_uid, 6, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Setup)
        QtCore.QMetaObject.connectSlotsByName(Setup)

    def retranslateUi(self, Setup):
        Setup.setWindowTitle(_translate("Setup", "Form", None))
        self.label.setText(_translate("Setup", "Host:", None))
        self.edit_host.setText(_translate("Setup", "localhost", None))
        self.label_2.setText(_translate("Setup", "Port:", None))
        self.button_reconnect.setText(_translate("Setup", "Reconnect", None))
        self.label_12.setText(_translate("Setup", "Segment Display 4x7", None))
        self.label_multi_touch_found.setText(_translate("Setup", "No", None))
        self.label_9.setText(_translate("Setup", "Dual Button 1", None))
        self.label_10.setText(_translate("Setup", "Dual Button 2", None))
        self.label_4.setText(_translate("Setup", "<html><head/><body><p><span style=\" font-weight:600;\">Bricklet</span></p></body></html>", None))
        self.label_5.setText(_translate("Setup", "<html><head/><body><p><span style=\" font-weight:600;\">Found</span></p></body></html>", None))
        self.label_6.setText(_translate("Setup", "<html><head/><body><p><span style=\" font-weight:600;\">UID</span></p></body></html>", None))
        self.label_7.setText(_translate("Setup", "LED Strip", None))
        self.label_8.setText(_translate("Setup", "Multi Touch", None))
        self.label_11.setText(_translate("Setup", "Piezo Speaker", None))
        self.label_led_strip_found.setText(_translate("Setup", "No", None))
        self.label_dual_button1_found.setText(_translate("Setup", "No", None))
        self.label_dual_button2_found.setText(_translate("Setup", "No", None))
        self.label_piezo_speaker_found.setText(_translate("Setup", "No", None))
        self.label_segment_display_found.setText(_translate("Setup", "No", None))
        self.label_led_strip_uid.setText(_translate("Setup", "None", None))
        self.label_multi_touch_uid.setText(_translate("Setup", "None", None))
        self.label_dual_button1_uid.setText(_translate("Setup", "None", None))
        self.label_dual_button2_uid.setText(_translate("Setup", "None", None))
        self.label_piezo_speaker_uid.setText(_translate("Setup", "None", None))
        self.label_segment_display_uid.setText(_translate("Setup", "None", None))

