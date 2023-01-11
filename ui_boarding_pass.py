# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'boarding_pass.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Main_page = QStackedWidget(self.centralwidget)
        self.Main_page.setObjectName(u"Main_page")
        self.Main_page.setGeometry(QRect(40, 10, 731, 531))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Main_page.sizePolicy().hasHeightForWidth())
        self.Main_page.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(18)
        self.Main_page.setFont(font)
        self.Main_page.setFrameShape(QFrame.Box)
        self.Main_page.setFrameShadow(QFrame.Plain)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout = QGridLayout(self.page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.id_name = QLabel(self.page)
        self.id_name.setObjectName(u"id_name")
        font1 = QFont()
        font1.setFamily(u"Sans Serif")
        font1.setPointSize(18)
        self.id_name.setFont(font1)
        self.id_name.setFrameShape(QFrame.NoFrame)

        self.gridLayout.addWidget(self.id_name, 0, 0, 1, 2)

        self.fligh_nr = QLabel(self.page)
        self.fligh_nr.setObjectName(u"fligh_nr")

        self.gridLayout.addWidget(self.fligh_nr, 0, 3, 1, 1)

        self.seat_class = QLabel(self.page)
        self.seat_class.setObjectName(u"seat_class")
        font2 = QFont()
        font2.setPointSize(15)
        self.seat_class.setFont(font2)

        self.gridLayout.addWidget(self.seat_class, 1, 0, 1, 1)

        self.flight_destination = QLabel(self.page)
        self.flight_destination.setObjectName(u"flight_destination")
        self.flight_destination.setFont(font2)

        self.gridLayout.addWidget(self.flight_destination, 1, 3, 1, 1)

        self.gate = QLabel(self.page)
        self.gate.setObjectName(u"gate")

        self.gridLayout.addWidget(self.gate, 2, 0, 1, 1)

        self.time_of_departue = QLabel(self.page)
        self.time_of_departue.setObjectName(u"time_of_departue")

        self.gridLayout.addWidget(self.time_of_departue, 2, 3, 1, 1)

        self.seat_nr = QLabel(self.page)
        self.seat_nr.setObjectName(u"seat_nr")
        self.seat_nr.setFont(font2)

        self.gridLayout.addWidget(self.seat_nr, 1, 1, 1, 1)

        self.Main_page.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.Main_page.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 20))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.id_name.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.fligh_nr.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.seat_class.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.flight_destination.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.gate.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.time_of_departue.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.seat_nr.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

