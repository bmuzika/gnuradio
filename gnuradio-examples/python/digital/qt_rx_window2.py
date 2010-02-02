# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_rx_window2.ui'
#
# Created: Sat Jan  2 12:54:51 2010
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DigitalWindow(object):
    def setupUi(self, DigitalWindow):
        DigitalWindow.setObjectName("DigitalWindow")
        DigitalWindow.resize(1000, 816)
        self.centralwidget = QtGui.QWidget(DigitalWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rxBox = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rxBox.sizePolicy().hasHeightForWidth())
        self.rxBox.setSizePolicy(sizePolicy)
        self.rxBox.setMinimumSize(QtCore.QSize(250, 190))
        self.rxBox.setMaximumSize(QtCore.QSize(250, 250))
        self.rxBox.setObjectName("rxBox")
        self.formLayout = QtGui.QFormLayout(self.rxBox)
        self.formLayout.setObjectName("formLayout")
        self.freqLabel = QtGui.QLabel(self.rxBox)
        self.freqLabel.setObjectName("freqLabel")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.freqLabel)
        self.freqEdit = QtGui.QLineEdit(self.rxBox)
        self.freqEdit.setObjectName("freqEdit")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.freqEdit)
        self.gainLabel = QtGui.QLabel(self.rxBox)
        self.gainLabel.setObjectName("gainLabel")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.gainLabel)
        self.gainEdit = QtGui.QLineEdit(self.rxBox)
        self.gainEdit.setObjectName("gainEdit")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.gainEdit)
        self.decimLabel = QtGui.QLabel(self.rxBox)
        self.decimLabel.setObjectName("decimLabel")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.decimLabel)
        self.decimEdit = QtGui.QLineEdit(self.rxBox)
        self.decimEdit.setObjectName("decimEdit")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.decimEdit)
        self.gainClockLabel = QtGui.QLabel(self.rxBox)
        self.gainClockLabel.setObjectName("gainClockLabel")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.gainClockLabel)
        self.gainClockEdit = QtGui.QLineEdit(self.rxBox)
        self.gainClockEdit.setObjectName("gainClockEdit")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.gainClockEdit)
        self.gainPhaseLabel = QtGui.QLabel(self.rxBox)
        self.gainPhaseLabel.setObjectName("gainPhaseLabel")
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.gainPhaseLabel)
        self.gainPhaseEdit = QtGui.QLineEdit(self.rxBox)
        self.gainPhaseEdit.setObjectName("gainPhaseEdit")
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.gainPhaseEdit)
        self.gainFreqEdit = QtGui.QLineEdit(self.rxBox)
        self.gainFreqEdit.setObjectName("gainFreqEdit")
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.gainFreqEdit)
        self.gainFreqLabel = QtGui.QLabel(self.rxBox)
        self.gainFreqLabel.setObjectName("gainFreqLabel")
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.gainFreqLabel)
        self.horizontalLayout.addWidget(self.rxBox)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.rxPacketBox = QtGui.QGroupBox(self.centralwidget)
        self.rxPacketBox.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rxPacketBox.sizePolicy().hasHeightForWidth())
        self.rxPacketBox.setSizePolicy(sizePolicy)
        self.rxPacketBox.setMinimumSize(QtCore.QSize(250, 130))
        self.rxPacketBox.setMaximumSize(QtCore.QSize(250, 130))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.rxPacketBox.setFont(font)
        self.rxPacketBox.setObjectName("rxPacketBox")
        self.pktsRcvdEdit = QtGui.QLineEdit(self.rxPacketBox)
        self.pktsRcvdEdit.setGeometry(QtCore.QRect(120, 30, 113, 23))
        self.pktsRcvdEdit.setObjectName("pktsRcvdEdit")
        self.pktsRcvdLabel = QtGui.QLabel(self.rxPacketBox)
        self.pktsRcvdLabel.setGeometry(QtCore.QRect(10, 30, 111, 20))
        self.pktsRcvdLabel.setObjectName("pktsRcvdLabel")
        self.pktsCorrectEdit = QtGui.QLineEdit(self.rxPacketBox)
        self.pktsCorrectEdit.setGeometry(QtCore.QRect(120, 60, 113, 23))
        self.pktsCorrectEdit.setObjectName("pktsCorrectEdit")
        self.pktsCorrectLabel = QtGui.QLabel(self.rxPacketBox)
        self.pktsCorrectLabel.setGeometry(QtCore.QRect(10, 60, 111, 20))
        self.pktsCorrectLabel.setObjectName("pktsCorrectLabel")
        self.perLabel = QtGui.QLabel(self.rxPacketBox)
        self.perLabel.setGeometry(QtCore.QRect(10, 90, 111, 20))
        self.perLabel.setObjectName("perLabel")
        self.perEdit = QtGui.QLineEdit(self.rxPacketBox)
        self.perEdit.setGeometry(QtCore.QRect(120, 90, 113, 23))
        self.perEdit.setObjectName("perEdit")
        self.verticalLayout_3.addWidget(self.rxPacketBox)
        spacerItem = QtGui.QSpacerItem(20, 60, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.closeButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closeButton.sizePolicy().hasHeightForWidth())
        self.closeButton.setSizePolicy(sizePolicy)
        self.closeButton.setMinimumSize(QtCore.QSize(80, 30))
        self.closeButton.setMaximumSize(QtCore.QSize(80, 30))
        self.closeButton.setObjectName("closeButton")
        self.verticalLayout_5.addWidget(self.closeButton)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.sinkFrame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.sinkFrame.sizePolicy().hasHeightForWidth())
        self.sinkFrame.setSizePolicy(sizePolicy)
        self.sinkFrame.setMinimumSize(QtCore.QSize(800, 500))
        self.sinkFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.sinkFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.sinkFrame.setObjectName("sinkFrame")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.sinkFrame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.sinkLayout = QtGui.QHBoxLayout()
        self.sinkLayout.setObjectName("sinkLayout")
        self.horizontalLayout_2.addLayout(self.sinkLayout)
        self.gridLayout.addWidget(self.sinkFrame, 0, 0, 1, 1)
        DigitalWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(DigitalWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 24))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        DigitalWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(DigitalWindow)
        self.statusbar.setObjectName("statusbar")
        DigitalWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(DigitalWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(DigitalWindow)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL("triggered()"), DigitalWindow.close)
        QtCore.QObject.connect(self.closeButton, QtCore.SIGNAL("clicked()"), DigitalWindow.close)
        QtCore.QMetaObject.connectSlotsByName(DigitalWindow)

    def retranslateUi(self, DigitalWindow):
        DigitalWindow.setWindowTitle(QtGui.QApplication.translate("DigitalWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.rxBox.setTitle(QtGui.QApplication.translate("DigitalWindow", "Receiver Parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.freqLabel.setText(QtGui.QApplication.translate("DigitalWindow", "Frequency (Hz)", None, QtGui.QApplication.UnicodeUTF8))
        self.gainLabel.setText(QtGui.QApplication.translate("DigitalWindow", "Gain (dB)", None, QtGui.QApplication.UnicodeUTF8))
        self.decimLabel.setText(QtGui.QApplication.translate("DigitalWindow", "Decimation", None, QtGui.QApplication.UnicodeUTF8))
        self.gainClockLabel.setText(QtGui.QApplication.translate("DigitalWindow", "Clock Loop Gain", None, QtGui.QApplication.UnicodeUTF8))
        self.gainPhaseLabel.setText(QtGui.QApplication.translate("DigitalWindow", "Phase Loop Gain", None, QtGui.QApplication.UnicodeUTF8))
        self.gainFreqLabel.setText(QtGui.QApplication.translate("DigitalWindow", "Freq. Loop Gain", None, QtGui.QApplication.UnicodeUTF8))
        self.rxPacketBox.setTitle(QtGui.QApplication.translate("DigitalWindow", "Received Packet Info", None, QtGui.QApplication.UnicodeUTF8))
        self.pktsRcvdLabel.setText(QtGui.QApplication.translate("DigitalWindow", "Packets Rcvd.", None, QtGui.QApplication.UnicodeUTF8))
        self.pktsCorrectLabel.setText(QtGui.QApplication.translate("DigitalWindow", "Packets Correct", None, QtGui.QApplication.UnicodeUTF8))
        self.perLabel.setText(QtGui.QApplication.translate("DigitalWindow", "PER", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("DigitalWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("DigitalWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("DigitalWindow", "E&xit", None, QtGui.QApplication.UnicodeUTF8))

