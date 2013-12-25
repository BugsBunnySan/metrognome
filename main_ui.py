# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Wed Dec 25 23:02:38 2013
#      by: pyside-uic 0.2.8 running on PySide 1.0.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(184, 114)
        MainWindow.setStyleSheet("color:rgb(45, 145, 45);\n"
"background-color:rgb(0, 0, 0);\n"
"outline: 1px solid rgb(45, 145, 45);")
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.play_button = QtGui.QPushButton(self.centralwidget)
        self.play_button.setMinimumSize(QtCore.QSize(0, 32))
        self.play_button.setMaximumSize(QtCore.QSize(16777215, 32))
        self.play_button.setBaseSize(QtCore.QSize(0, 32))
        self.play_button.setStyleSheet("")
        self.play_button.setObjectName("play_button")
        self.verticalLayout.addWidget(self.play_button)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.f_spin = QtGui.QSpinBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.f_spin.sizePolicy().hasHeightForWidth())
        self.f_spin.setSizePolicy(sizePolicy)
        self.f_spin.setMinimumSize(QtCore.QSize(0, 32))
        self.f_spin.setMaximumSize(QtCore.QSize(16777215, 32))
        self.f_spin.setBaseSize(QtCore.QSize(0, 32))
        self.f_spin.setStyleSheet("selection-color: rgb(0, 0, 0);\n"
"selection-background-color: rgb(45,145,45);\n"
"")
        self.f_spin.setPrefix("")
        self.f_spin.setMinimum(1)
        self.f_spin.setMaximum(300)
        self.f_spin.setObjectName("f_spin")
        self.horizontalLayout.addWidget(self.f_spin)
        self.speaker_button = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.speaker_button.sizePolicy().hasHeightForWidth())
        self.speaker_button.setSizePolicy(sizePolicy)
        self.speaker_button.setMinimumSize(QtCore.QSize(32, 32))
        self.speaker_button.setMaximumSize(QtCore.QSize(32, 32))
        self.speaker_button.setBaseSize(QtCore.QSize(32, 32))
        self.speaker_button.setText("")
        self.speaker_button.setObjectName("speaker_button")
        self.horizontalLayout.addWidget(self.speaker_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.ping_icon = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ping_icon.sizePolicy().hasHeightForWidth())
        self.ping_icon.setSizePolicy(sizePolicy)
        self.ping_icon.setMinimumSize(QtCore.QSize(64, 64))
        self.ping_icon.setMaximumSize(QtCore.QSize(64, 64))
        self.ping_icon.setBaseSize(QtCore.QSize(64, 64))
        self.ping_icon.setObjectName("ping_icon")
        self.horizontalLayout_2.addWidget(self.ping_icon)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.play_button, QtCore.SIGNAL("pressed()"), MainWindow.toggle_play)
        QtCore.QObject.connect(self.f_spin, QtCore.SIGNAL("valueChanged(int)"), MainWindow.set_frequency)
        QtCore.QObject.connect(self.speaker_button, QtCore.SIGNAL("pressed()"), MainWindow.toggle_play_sound)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Metrognome", None, QtGui.QApplication.UnicodeUTF8))
        self.play_button.setText(QtGui.QApplication.translate("MainWindow", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.ping_icon.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

