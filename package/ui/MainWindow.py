# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PIL import Image, ImageQt
from package.Transform import BufferedImage
from package.ui import MainWindow_rc


class Ui_MainWindow(object):
    def __init__(self):
        self.Kiwi = BufferedImage()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Preset/kiwi.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.imageLabel = QtWidgets.QLabel(self.centralwidget)
        self.imageLabel.setText("")
        self.imageLabel.setPixmap(QtGui.QPixmap(":/Preset/test.png"))
        self.imageLabel.setObjectName("imageLabel")
        self.horizontalLayout.addWidget(self.imageLabel)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem = QtWidgets.QSpacerItem(500, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.mask_red = QtWidgets.QLineEdit(self.centralwidget)
        self.mask_red.setAlignment(QtCore.Qt.AlignCenter)
        self.mask_red.setObjectName("mask_red")
        self.horizontalLayout_3.addWidget(self.mask_red)
        self.mask_green = QtWidgets.QLineEdit(self.centralwidget)
        self.mask_green.setAlignment(QtCore.Qt.AlignCenter)
        self.mask_green.setObjectName("mask_green")
        self.horizontalLayout_3.addWidget(self.mask_green)
        self.mask_blue = QtWidgets.QLineEdit(self.centralwidget)
        self.mask_blue.setAlignment(QtCore.Qt.AlignCenter)
        self.mask_blue.setObjectName("mask_blue")
        self.horizontalLayout_3.addWidget(self.mask_blue)
        self.mask_alpha = QtWidgets.QLineEdit(self.centralwidget)
        self.mask_alpha.setAlignment(QtCore.Qt.AlignCenter)
        self.mask_alpha.setObjectName("mask_alpha")
        self.horizontalLayout_3.addWidget(self.mask_alpha)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_mask_XOR = QtWidgets.QPushButton(self.centralwidget)
        self.btn_mask_XOR.setObjectName("btn_mask_XOR")
        self.horizontalLayout_4.addWidget(self.btn_mask_XOR)
        self.btn_mask_OR = QtWidgets.QPushButton(self.centralwidget)
        self.btn_mask_OR.setObjectName("btn_mask_OR")
        self.horizontalLayout_4.addWidget(self.btn_mask_OR)
        self.btn_mask_AND = QtWidgets.QPushButton(self.centralwidget)
        self.btn_mask_AND.setObjectName("btn_mask_AND")
        self.horizontalLayout_4.addWidget(self.btn_mask_AND)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_randomMap = QtWidgets.QPushButton(self.centralwidget)
        self.btn_randomMap.setObjectName("btn_randomMap")
        self.horizontalLayout_2.addWidget(self.btn_randomMap)
        self.btn_ctrlZ = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ctrlZ.setObjectName("btn_ctrlZ")
        self.horizontalLayout_2.addWidget(self.btn_ctrlZ)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.btn_return = QtWidgets.QPushButton(self.centralwidget)
        self.btn_return.setObjectName("btn_return")
        self.verticalLayout.addWidget(self.btn_return)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        self.menu_F = QtWidgets.QMenu(self.menubar)
        self.menu_F.setObjectName("menu_F")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.btn_fileOpen = QtWidgets.QAction(MainWindow)
        self.btn_fileOpen.setObjectName("btn_fileOpen")
        self.btn_fileOpen.triggered.connect(self.onClicked_btn_fileOpen)
        self.btn_fileSave = QtWidgets.QAction(MainWindow)
        self.btn_fileSave.setObjectName("btn_fileSave")
        self.btn_fileSave.triggered.connect(self.onClicked_btn_fileSave)
        self.btn_logMenu = QtWidgets.QAction(MainWindow)
        self.btn_logMenu.setObjectName("btn_logMenu")
        self.btn_logMenu.triggered.connect(self.onClicked_btn_logMenu)
        self.btn_exit = QtWidgets.QAction(MainWindow)
        self.btn_exit.setObjectName("btn_exit")
        self.btn_exit.triggered.connect(self.onClicked_btn_exit)
        self.menu_F.addAction(self.btn_fileOpen)
        self.menu_F.addAction(self.btn_fileSave)
        self.menu_F.addSeparator()
        self.menu_F.addAction(self.btn_logMenu)
        self.menu_F.addAction(self.btn_exit)
        self.menubar.addAction(self.menu_F.menuAction())

        self.retranslateUi(MainWindow)
        self.connectEventHandler()
        self.enableUI(False)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Kiwi-Steganography"))
        self.label_2.setText(_translate("MainWindow", "Masking"))
        self.label_3.setText(_translate("MainWindow", "RGBA Mask"))
        self.mask_red.setText(_translate("MainWindow", "255"))
        self.mask_green.setText(_translate("MainWindow", "255"))
        self.mask_blue.setText(_translate("MainWindow", "255"))
        self.mask_alpha.setText(_translate("MainWindow", "255"))
        self.btn_mask_XOR.setText(_translate("MainWindow", "XOR"))
        self.btn_mask_OR.setText(_translate("MainWindow", "OR"))
        self.btn_mask_AND.setText(_translate("MainWindow", "AND"))
        self.btn_randomMap.setText(_translate("MainWindow", "Random Mapping"))
        self.btn_ctrlZ.setText(_translate("MainWindow", "Ctrl+Z"))
        self.btn_return.setText(_translate("MainWindow", "Return To Original Image"))
        self.menu_F.setTitle(_translate("MainWindow", "파일"))
        self.btn_fileOpen.setText(_translate("MainWindow", "파일 열기"))
        self.btn_fileOpen.setToolTip(_translate("MainWindow", "분석할 파일을 선택합니다"))
        self.btn_fileOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.btn_fileSave.setText(_translate("MainWindow", "파일 저장"))
        self.btn_fileSave.setToolTip(_translate("MainWindow", "열린 파일을 저장합니다"))
        self.btn_fileSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.btn_logMenu.setText(_translate("MainWindow", "로그 보기"))
        self.btn_logMenu.setToolTip(_translate("MainWindow", "이미지 조작 로그를 확인합니다"))
        self.btn_logMenu.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.btn_exit.setText(_translate("MainWindow", "종료"))
        self.btn_exit.setToolTip(_translate("MainWindow", "kiwi-steg를 종료합니다"))
        self.btn_exit.setShortcut(_translate("MainWindow", "Ctrl+Q"))

    def connectEventHandler(self):
        self.btn_mask_AND.clicked.connect(self.onClicked_btn_mask_AND)
        self.btn_mask_OR.clicked.connect(self.onClicked_btn_mask_OR)
        self.btn_mask_XOR.clicked.connect(self.onClicked_btn_mask_XOR)
        self.btn_ctrlZ.clicked.connect(self.onClicked_btn_ctrlZ)
        self.btn_return.clicked.connect(self.onClicked_btn_return)
        self.btn_randomMap.clicked.connect(self.onClicked_btn_randomMap)

    def enableUI(self, state):
        self.btn_mask_AND.setEnabled(state)
        self.btn_mask_OR.setEnabled(state)
        self.btn_mask_XOR.setEnabled(state)
        self.btn_ctrlZ.setEnabled(state)
        self.btn_return.setEnabled(state)
        self.btn_randomMap.setEnabled(state)
        self.mask_red.setEnabled(state)
        self.mask_green.setEnabled(state)
        self.mask_blue.setEnabled(state)
        self.mask_alpha.setEnabled(state)

    def loadImage(self, img):
        self.imageLabel.setPixmap(
            QtGui.QPixmap.fromImage(ImageQt.ImageQt(img))
        )

    def onClicked_btn_mask_AND(self):
        qmask = (
            int(self.mask_red.text()),
            int(self.mask_green.text()),
            int(self.mask_blue.text()))
        self.loadImage(self.Kiwi.rgb_and(mask=qmask))

    def onClicked_btn_mask_OR(self):
        qmask = (
            int(self.mask_red.text()),
            int(self.mask_green.text()),
            int(self.mask_blue.text()))
        self.loadImage(self.Kiwi.rgb_or(mask=qmask))

    def onClicked_btn_mask_XOR(self):
        qmask = (
            int(self.mask_red.text()),
            int(self.mask_green.text()),
            int(self.mask_blue.text()))
        self.loadImage(self.Kiwi.rgb_xor(mask=qmask))

    def onClicked_btn_randomMap(self):
        self.loadImage(self.Kiwi.randomMap())

    def onClicked_btn_ctrlZ(self):
        self.loadImage(self.Kiwi.getPreviousImage())

    def onClicked_btn_return(self):
        self.loadImage(self.Kiwi.getOriginalImage())

    def onClicked_btn_fileOpen(self):
        path, _filter = QFileDialog.getOpenFileName(
            None, "Open Image", "C:\\", "Image Files (*.png *.jpg *.bmp)")
        if path is not '':
            self.Kiwi.initialize(path)
            self.loadImage(self.Kiwi.getOriginalImage())
            self.enableUI(True)
        else:
            pass

    def onClicked_btn_fileSave(self):
        path, _filter = QFileDialog.getSaveFileName(
            None, "Save Image", "C:\\", "Image Files (*.png *.jpg *.bmp)")
        if path is not '':
            buf = self.Kiwi.getCurrentImage()
            buf.save(path)
        else:
            pass

    def onClicked_btn_logMenu(self):
        pass

    def onClicked_btn_exit(self):
        exit()
        pass
