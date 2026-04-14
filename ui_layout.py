# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'layout.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTableView, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(740, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(740, 450))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(33, 0))
        self.centralwidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(10, -1, -1, -1)
        self.FileList = QListWidget(self.centralwidget)
        self.FileList.setObjectName(u"FileList")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.FileList.sizePolicy().hasHeightForWidth())
        self.FileList.setSizePolicy(sizePolicy1)
        self.FileList.setMinimumSize(QSize(500, 189))
        self.FileList.setMaximumSize(QSize(500, 189))

        self.horizontalLayout_3.addWidget(self.FileList)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.gridLayout_2.setContentsMargins(-1, -1, 13, -1)
        self.FileButton = QPushButton(self.centralwidget)
        self.FileButton.setObjectName(u"FileButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.FileButton.sizePolicy().hasHeightForWidth())
        self.FileButton.setSizePolicy(sizePolicy2)
        self.FileButton.setMinimumSize(QSize(163, 31))
        self.FileButton.setMaximumSize(QSize(195, 31))
        self.FileButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.FileButton.setStyleSheet(u"border-radius: 5px;\n"
"\n"
"\n"
"background-color: #00358F;\n"
"font-weight: bold;\n"
"color: white;")

        self.gridLayout_2.addWidget(self.FileButton, 0, 1, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.widget, 1, 0, 1, 1)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy3.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.widget_3, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 40, -1, -1)
        self.GenerateButton = QPushButton(self.centralwidget)
        self.GenerateButton.setObjectName(u"GenerateButton")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.GenerateButton.sizePolicy().hasHeightForWidth())
        self.GenerateButton.setSizePolicy(sizePolicy4)
        self.GenerateButton.setMinimumSize(QSize(163, 31))
        self.GenerateButton.setMaximumSize(QSize(163, 31))
        self.GenerateButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.GenerateButton.setStyleSheet(u"border-radius: 5px;\n"
"\n"
"\n"
"background-color: rgb(19, 140, 19);\n"
"font-weight: bold;\n"
"color: white;")
        self.GenerateButton.setCheckable(False)

        self.verticalLayout.addWidget(self.GenerateButton)


        self.gridLayout_2.addLayout(self.verticalLayout, 1, 1, 1, 1)


        self.horizontalLayout_3.addLayout(self.gridLayout_2)


        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 50, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 7, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, -1, 0, 0)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamilies([u"Yu Gothic UI Semibold"])
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)


        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, -1, 0, -1)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")

        self.gridLayout_6.addLayout(self.gridLayout_4, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, 20, -1)
        self.SaveButton = QPushButton(self.centralwidget)
        self.SaveButton.setObjectName(u"SaveButton")
        self.SaveButton.setMinimumSize(QSize(163, 31))
        self.SaveButton.setMaximumSize(QSize(163, 31))
        self.SaveButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.SaveButton.setStyleSheet(u"border-radius: 5px;\n"
"\n"
"\n"
"background-color: rgb(19, 140, 19);\n"
"font-weight: bold;\n"
"color: white;")

        self.verticalLayout_2.addWidget(self.SaveButton)


        self.gridLayout_6.addLayout(self.verticalLayout_2, 0, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_6, 0, 1, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")

        self.gridLayout_5.addWidget(self.widget_2, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_5, 0, 0, 1, 1)


        self.horizontalLayout_7.addLayout(self.gridLayout_3)


        self.gridLayout.addLayout(self.horizontalLayout_7, 8, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(10, -1, 10, -1)
        self.DataTable = QTableView(self.centralwidget)
        self.DataTable.setObjectName(u"DataTable")
        self.DataTable.setEnabled(True)
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.DataTable.sizePolicy().hasHeightForWidth())
        self.DataTable.setSizePolicy(sizePolicy5)
        self.DataTable.setMinimumSize(QSize(0, 24))
        self.DataTable.setMaximumSize(QSize(16777215, 300))
        self.DataTable.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.DataTable.setDragEnabled(True)
        self.DataTable.setShowGrid(True)
        self.DataTable.setGridStyle(Qt.PenStyle.SolidLine)
        self.DataTable.setSortingEnabled(True)
        self.DataTable.setCornerButtonEnabled(True)

        self.horizontalLayout_5.addWidget(self.DataTable)


        self.gridLayout.addLayout(self.horizontalLayout_5, 6, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(30, -1, -1, -1)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.verticalLayout_3.addWidget(self.label_3)


        self.gridLayout.addLayout(self.verticalLayout_3, 5, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(30, -1, -1, -1)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.verticalLayout_4.addWidget(self.label_2)


        self.gridLayout.addLayout(self.verticalLayout_4, 3, 0, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.FileList, self.DataTable)

        self.retranslateUi(MainWindow)

        self.GenerateButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Relat\u00f3rio DUIMP", None))
        self.FileButton.setText(QCoreApplication.translate("MainWindow", u"Selecionar Arquivos", None))
        self.GenerateButton.setText(QCoreApplication.translate("MainWindow", u"Gerar Relat\u00f3rio", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Relat\u00f3rio de DUIMP", None))
        self.SaveButton.setText(QCoreApplication.translate("MainWindow", u"Salvar em Excel", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Visualiza\u00e7\u00e3o do relat\u00f3rio:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"DUIMPs selecionadas:", None))
    # retranslateUi

