# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VastusgiyZlp.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDoubleSpinBox, QFrame,
    QLCDNumber, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(610, 355)
        font = QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(280, 10, 141, 121))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.forwardVoltageLabel = QLabel(self.layoutWidget)
        self.forwardVoltageLabel.setObjectName(u"forwardVoltageLabel")
        self.forwardVoltageLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.forwardVoltageLabel)

        self.forwardVoltageLcd = QLCDNumber(self.layoutWidget)
        self.forwardVoltageLcd.setObjectName(u"forwardVoltageLcd")
        self.forwardVoltageLcd.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"background-color: rgb(0, 0, 0);")

        self.verticalLayout.addWidget(self.forwardVoltageLcd)

        self.forwardVoltage = QDoubleSpinBox(self.layoutWidget)
        self.forwardVoltage.setObjectName(u"forwardVoltage")
        self.forwardVoltage.setFont(font)
        self.forwardVoltage.setDecimals(1)
        self.forwardVoltage.setMaximum(10.000000000000000)
        self.forwardVoltage.setSingleStep(0.100000000000000)
        self.forwardVoltage.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)

        self.verticalLayout.addWidget(self.forwardVoltage)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(430, 10, 161, 121))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.currentLabel = QLabel(self.layoutWidget1)
        self.currentLabel.setObjectName(u"currentLabel")
        self.currentLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.currentLabel)

        self.forwardCurrendLcd = QLCDNumber(self.layoutWidget1)
        self.forwardCurrendLcd.setObjectName(u"forwardCurrendLcd")
        self.forwardCurrendLcd.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"background-color: rgb(0, 0, 0);")

        self.verticalLayout_2.addWidget(self.forwardCurrendLcd)

        self.forwardCurrent = QDoubleSpinBox(self.layoutWidget1)
        self.forwardCurrent.setObjectName(u"forwardCurrent")
        self.forwardCurrent.setFont(font)
        self.forwardCurrent.setDecimals(0)
        self.forwardCurrent.setMaximum(1000.000000000000000)

        self.verticalLayout_2.addWidget(self.forwardCurrent)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(270, 0, 331, 141))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(270, 150, 331, 131))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.strip5 = QFrame(self.frame_2)
        self.strip5.setObjectName(u"strip5")
        self.strip5.setGeometry(QRect(290, 20, 16, 41))
        self.strip5.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.strip5.setFrameShape(QFrame.Shape.StyledPanel)
        self.strip5.setFrameShadow(QFrame.Shadow.Raised)
        self.strip4 = QFrame(self.frame_2)
        self.strip4.setObjectName(u"strip4")
        self.strip4.setGeometry(QRect(270, 20, 16, 41))
        self.strip4.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.strip4.setFrameShape(QFrame.Shape.StyledPanel)
        self.strip4.setFrameShadow(QFrame.Shadow.Raised)
        self.strip3 = QFrame(self.frame_2)
        self.strip3.setObjectName(u"strip3")
        self.strip3.setGeometry(QRect(250, 20, 16, 41))
        self.strip3.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.strip3.setFrameShape(QFrame.Shape.StyledPanel)
        self.strip3.setFrameShadow(QFrame.Shadow.Raised)
        self.strip2 = QFrame(self.frame_2)
        self.strip2.setObjectName(u"strip2")
        self.strip2.setGeometry(QRect(230, 20, 16, 41))
        self.strip2.setStyleSheet(u"background-color: rgb(170, 85, 0);")
        self.strip2.setFrameShape(QFrame.Shape.StyledPanel)
        self.strip2.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 101, 21))
        font1 = QFont()
        font1.setPointSize(18)
        self.label.setFont(font1)
        self.calculatePushButton = QPushButton(self.frame_2)
        self.calculatePushButton.setObjectName(u"calculatePushButton")
        self.calculatePushButton.setGeometry(QRect(170, 80, 151, 41))
        self.calculatePushButton.setFont(font1)
        self.calculatePushButton.setStyleSheet(u"background-color: rgb(255, 255, 127);")
        self.resistanceLcd = QLCDNumber(self.frame_2)
        self.resistanceLcd.setObjectName(u"resistanceLcd")
        self.resistanceLcd.setGeometry(QRect(10, 50, 141, 71))
        self.resistanceLcd.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"background-color: rgb(0, 0, 0);")
        self.strip1 = QFrame(self.frame_2)
        self.strip1.setObjectName(u"strip1")
        self.strip1.setGeometry(QRect(210, 20, 16, 41))
        self.strip1.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.strip1.setFrameShape(QFrame.Shape.StyledPanel)
        self.strip1.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 0, 251, 281))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.layoutWidget2 = QWidget(self.frame_3)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 10, 231, 201))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.supplyVoltageLabel = QLabel(self.layoutWidget2)
        self.supplyVoltageLabel.setObjectName(u"supplyVoltageLabel")
        font2 = QFont()
        font2.setPointSize(16)
        self.supplyVoltageLabel.setFont(font2)
        self.supplyVoltageLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.supplyVoltageLabel)

        self.supplyVoltageLcd = QLCDNumber(self.layoutWidget2)
        self.supplyVoltageLcd.setObjectName(u"supplyVoltageLcd")
        self.supplyVoltageLcd.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"background-color: rgb(0, 0, 0);")
        self.supplyVoltageLcd.setSmallDecimalPoint(True)
        self.supplyVoltageLcd.setDigitCount(3)
        self.supplyVoltageLcd.setProperty(u"value", 0.000000000000000)

        self.verticalLayout_3.addWidget(self.supplyVoltageLcd)

        self.supplyVoltage = QDoubleSpinBox(self.layoutWidget2)
        self.supplyVoltage.setObjectName(u"supplyVoltage")
        font3 = QFont()
        font3.setPointSize(22)
        self.supplyVoltage.setFont(font3)
        self.supplyVoltage.setDecimals(1)
        self.supplyVoltage.setMaximum(30.000000000000000)
        self.supplyVoltage.setSingleStep(0.100000000000000)
        self.supplyVoltage.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)

        self.verticalLayout_3.addWidget(self.supplyVoltage)

        MainWindow.setCentralWidget(self.centralwidget)
        self.frame_3.raise_()
        self.frame_2.raise_()
        self.frame.raise_()
        self.layoutWidget2.raise_()
        self.layoutWidget2.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 610, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.supplyVoltage.valueChanged.connect(self.supplyVoltageLcd.display)
        self.forwardVoltage.valueChanged.connect(self.forwardVoltageLcd.display)
        self.forwardCurrent.valueChanged.connect(self.forwardCurrendLcd.display)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.forwardVoltageLabel.setText(QCoreApplication.translate("MainWindow", u"Kynnysj\u00e4nnite", None))
        self.forwardVoltage.setSuffix(QCoreApplication.translate("MainWindow", u"V", None))
        self.currentLabel.setText(QCoreApplication.translate("MainWindow", u"Virta", None))
        self.forwardCurrent.setSuffix(QCoreApplication.translate("MainWindow", u"mA", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Etuvastus", None))
        self.calculatePushButton.setText(QCoreApplication.translate("MainWindow", u"Laske", None))
        self.supplyVoltageLabel.setText(QCoreApplication.translate("MainWindow", u"Sy\u00f6tt\u00f6j\u00e4nnite", None))
        self.supplyVoltage.setSuffix(QCoreApplication.translate("MainWindow", u"V", None))
    # retranslateUi

