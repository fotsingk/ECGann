# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QSplitter, QStatusBar,
    QWidget)

class Ui_ECGann(object):
    def setupUi(self, ECGann):
        if not ECGann.objectName():
            ECGann.setObjectName(u"ECGann")
        ECGann.resize(1096, 600)
        self.centralwidget = QWidget(ECGann)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1000, 446))
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 0, -1, 0)
        self.splitter_2 = QSplitter(self.centralwidget)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setMinimumSize(QSize(870, 73))
        self.splitter_2.setOrientation(Qt.Orientation.Horizontal)
        self.dataGroup = QGroupBox(self.splitter_2)
        self.dataGroup.setObjectName(u"dataGroup")
        self.dataGroup.setMinimumSize(QSize(410, 73))
        self.dataGroup.setMaximumSize(QSize(700, 73))
        self.horizontalLayout = QHBoxLayout(self.dataGroup)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.loadButton = QPushButton(self.dataGroup)
        self.loadButton.setObjectName(u"loadButton")
        self.loadButton.setMaximumSize(QSize(150, 16777215))
        self.loadButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.loadButton.setStyleSheet(u"background-color: rgba(85, 85, 255, 50);\n"
"selection-color: rgba(255, 255, 0, 50);")

        self.horizontalLayout.addWidget(self.loadButton)

        self.continuButton = QPushButton(self.dataGroup)
        self.continuButton.setObjectName(u"continuButton")
        self.continuButton.setMaximumSize(QSize(150, 16777215))
        self.continuButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.continuButton.setStyleSheet(u"background-color: rgba(75, 226, 226, 50);")

        self.horizontalLayout.addWidget(self.continuButton)

        self.splitter_2.addWidget(self.dataGroup)
        self.modeGroupBox = QGroupBox(self.splitter_2)
        self.modeGroupBox.setObjectName(u"modeGroupBox")
        self.modeGroupBox.setMinimumSize(QSize(242, 73))
        self.horizontalLayout_4 = QHBoxLayout(self.modeGroupBox)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.exploRadioButton = QRadioButton(self.modeGroupBox)
        self.exploRadioButton.setObjectName(u"exploRadioButton")
        self.exploRadioButton.setChecked(True)

        self.horizontalLayout_4.addWidget(self.exploRadioButton)

        self.labRadioButton = QRadioButton(self.modeGroupBox)
        self.labRadioButton.setObjectName(u"labRadioButton")

        self.horizontalLayout_4.addWidget(self.labRadioButton)

        self.splitter_2.addWidget(self.modeGroupBox)
        self.saveGroupBox = QGroupBox(self.splitter_2)
        self.saveGroupBox.setObjectName(u"saveGroupBox")
        self.saveGroupBox.setMinimumSize(QSize(217, 73))
        self.horizontalLayout_5 = QHBoxLayout(self.saveGroupBox)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.checkButton = QPushButton(self.saveGroupBox)
        self.checkButton.setObjectName(u"checkButton")
        self.checkButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.checkButton.setStyleSheet(u"background-color: rgba(170, 85, 255, 100);")

        self.horizontalLayout_5.addWidget(self.checkButton)

        self.saveButton = QPushButton(self.saveGroupBox)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.saveButton.setStyleSheet(u"background-color: rgba(85, 85, 255, 55);\n"
"selection-color: rgba(255, 255, 0, 50);")

        self.horizontalLayout_5.addWidget(self.saveButton)

        self.splitter_2.addWidget(self.saveGroupBox)

        self.gridLayout.addWidget(self.splitter_2, 0, 0, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(900, 300))

        self.gridLayout.addWidget(self.widget, 1, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(9)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.plotControlGroup = QGroupBox(self.centralwidget)
        self.plotControlGroup.setStyleSheet('''
QGroupBox::disabled {
                background-color:rgba(10,10,10,10);
                color: rgb(100,100,100);
                border-radius: 10px;
                }
QPushButton::disabled {
                background-color: rgba(10,10,10,15);
                color: gray;
                height: 25px;
                }
                                                                                        
QPushButton {border-color: rgb(0, 0, 0);
        color: rgb(1, 2, 1);
        background-color: rgb(210, 230, 254);
        height: 25px;
                }
                                      ''')
        self.plotControlGroup.setObjectName(u"plotControlGroup")
        self.plotControlGroup.setMinimumSize(QSize(500, 60))
        self.plotControlGroup.setMaximumSize(QSize(500, 80))
        self.horizontalLayout_2 = QHBoxLayout(self.plotControlGroup)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.prevButton = QPushButton(self.plotControlGroup)
        self.prevButton.setObjectName(u"prevButton")
        self.prevButton.setMaximumSize(QSize(100, 16777215))
        self.prevButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
#         self.prevButton.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
# "color: rgb(1, 2, 1);\n"
# "background-color: rgb(210, 230, 254);")

        self.horizontalLayout_2.addWidget(self.prevButton)

        self.sigNumber = QLabel(self.plotControlGroup)
        self.sigNumber.setObjectName(u"sigNumber")
        self.sigNumber.setMaximumSize(QSize(200, 16777215))
        self.sigNumber.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.sigNumber.setStyleSheet(u"font: 900 9pt \"Segoe UI Black\";")
        self.sigNumber.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.sigNumber)

        self.nextButton = QPushButton(self.plotControlGroup)
        self.nextButton.setObjectName(u"nextButton")
        self.nextButton.setMaximumSize(QSize(100, 16777215))
        self.nextButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
 #       self.nextButton.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
#"color: rgb(1, 2, 1);\n"
#"background-color: rgb(210, 230, 254);")

        self.horizontalLayout_2.addWidget(self.nextButton)


        self.horizontalLayout_6.addWidget(self.plotControlGroup)

        self.labelGroupBox = QGroupBox(self.centralwidget)
        self.labelGroupBox.setObjectName(u"labelGroupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelGroupBox.sizePolicy().hasHeightForWidth())
        self.labelGroupBox.setSizePolicy(sizePolicy)
        self.labelGroupBox.setMinimumSize(QSize(0, 60))
        self.labelGroupBox.setMaximumSize(QSize(500, 80))
        self.labelGroupBox.setStyleSheet('''
QGroupBox::disabled {
                background-color:rgba(10,10,10,10);
                color: rgb(100,100,100);
                border-radius: 10px;
                }
QPushButton::disabled {
                background-color: rgba(10,10,10,15);
                color: gray;
                height: 25px;
                }
                                                                                        
QPushButton {border-color: rgb(0, 0, 0);
        color: rgb(1, 2, 1);
        background-color: rgb(210, 230, 254);
        height: 25px;
                }
                                      ''')
        self.horizontalLayout_3 = QHBoxLayout(self.labelGroupBox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.badButton = QPushButton(self.labelGroupBox)
        self.badButton.setObjectName(u"badButton")
        self.badButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.badButton.setStyleSheet("""
        QPushButton::enabled {
                height: 25px;
                color: rgb(255, 0, 0);
                background-color: rgba(255, 85, 0, 50);
                font: 700 9pt "Segoe UI\";
                border-color: rgb(170, 0, 0);
                        }
                                     """)

        self.horizontalLayout_3.addWidget(self.badButton)

        self.goodButton = QPushButton(self.labelGroupBox)
        self.goodButton.setObjectName(u"goodButton")
        self.goodButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.goodButton.setStyleSheet(u"QPushButton::enabled {color: rgb(0, 170, 0);\n"
"font: 700 9pt \"Segoe UI\";\n"
"border-color: rgb(0, 85, 0);\n"
"height: 25px;\n"
"background-color: rgba(0, 255, 127, 50);}")

        self.horizontalLayout_3.addWidget(self.goodButton)

        self.unknownButton = QPushButton(self.labelGroupBox)
        self.unknownButton.setObjectName(u"unknownButton")
        self.unknownButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.unknownButton.setStyleSheet(u"QPushButton::enabled {color: rgb(0, 0, 0);\n"
"font: 700 9pt \"Segoe UI\";\n"
"height: 25px;\n"
"background-color: rgba(255, 180, 0, 50);}")

        self.horizontalLayout_3.addWidget(self.unknownButton)


        self.horizontalLayout_6.addWidget(self.labelGroupBox)


        self.gridLayout.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)

        ECGann.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ECGann)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1096, 33))
        ECGann.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ECGann)
        self.statusbar.setObjectName(u"statusbar")
        ECGann.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.loadButton, self.nextButton)
        QWidget.setTabOrder(self.nextButton, self.prevButton)
        QWidget.setTabOrder(self.prevButton, self.continuButton)

        self.retranslateUi(ECGann)

        QMetaObject.connectSlotsByName(ECGann)
    # setupUi

    def retranslateUi(self, ECGann):
        ECGann.setWindowTitle(QCoreApplication.translate("ECGann", u"ECGann", None))
        self.dataGroup.setTitle(QCoreApplication.translate("ECGann", u"Load Databases", None))
        self.loadButton.setText(QCoreApplication.translate("ECGann", u"Load", None))
        self.continuButton.setText(QCoreApplication.translate("ECGann", u"Continue", None))
        self.modeGroupBox.setTitle(QCoreApplication.translate("ECGann", u"Mode", None))
        self.exploRadioButton.setText(QCoreApplication.translate("ECGann", u"Exploration", None))
        self.labRadioButton.setText(QCoreApplication.translate("ECGann", u"Labelization", None))
        self.saveGroupBox.setTitle(QCoreApplication.translate("ECGann", u"Save", None))
        self.checkButton.setText(QCoreApplication.translate("ECGann", u"Info", None))
        self.saveButton.setText(QCoreApplication.translate("ECGann", u"Save & Exit", None))
        self.plotControlGroup.setTitle(QCoreApplication.translate("ECGann", u"plot control", None))
        self.prevButton.setText(QCoreApplication.translate("ECGann", u"<< Previous", None))
        self.sigNumber.setText(QCoreApplication.translate("ECGann", u"plot number xxxx", None))
        self.nextButton.setText(QCoreApplication.translate("ECGann", u"Next >>", None))
        self.labelGroupBox.setTitle(QCoreApplication.translate("ECGann", u"Label", None))
        self.badButton.setText(QCoreApplication.translate("ECGann", u"Bad", None))
        self.goodButton.setText(QCoreApplication.translate("ECGann", u"Good", None))
        self.unknownButton.setText(QCoreApplication.translate("ECGann", u"unknown", None))
    # retranslateUi

