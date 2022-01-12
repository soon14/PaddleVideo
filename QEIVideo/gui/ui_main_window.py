# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from QEIVideo.widget.PaintBoard import PaintBoard



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("EIVideo")
        MainWindow.resize(1101, 751)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 20, 1271, 771))
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.cap = []
        self.all_frames = []

        self.fps = None
        self.timer = QTimer(self.frame)
        self.time_label = QLabel('--/--', self.frame)

        self.progress_slider = QSlider(self.frame)
        self.progress_slider.setEnabled(True)
        self.progress_slider.setOrientation(Qt.Horizontal)
        self.progress_slider.setFixedWidth(710)
        self.progress_slider.setFixedHeight(20)
        self.progress_slider.setSingleStep(1)  # 设置变化步长
        self.progress_slider.setValue(0)
        self.progress_slider.sliderReleased.connect(self.update_video_position_func)  # 拖拽进度条

        self.picturelabel = QtWidgets.QLabel(self.frame)
        self.picturelabel.setGeometry(30, 30, 810, 458)
        self.picturelabel.setText("")
        self.picturelabel.setObjectName("picturelabel")

        self.paintBoard = PaintBoard(self.frame)
        self.paintBoard.setGeometry(30, 30, 810, 458)

        self.cbtn_Eraser = QCheckBox("橡皮擦")
        self.cbtn_Eraser.setParent(self.frame)
        self.cbtn_Eraser.move(950, 40)
        self.cbtn_Eraser.clicked.connect(self.on_cbtn_eraser_clicked)
        self.btn_Clear = QPushButton("清空画板")
        self.btn_Clear.setParent(self.frame)  # 设置父对象为本界面
        self.btn_Clear.move(950, 60)
        self.btn_Clear.clicked.connect(self.paintBoard.clear)
        self.label_penColor = QLabel(self.frame)
        self.label_penColor.setText("画笔颜色")
        self.label_penColor.move(990, 100)
        # 获取颜色列表(字符串类型)
        self.colorList = QColor.colorNames()
        self.comboBox_penColor = QComboBox(self.frame)
        self.fill_color_list(self.comboBox_penColor)  # 用各种颜色填充下拉列表
        self.comboBox_penColor.move(1080, 80)
        self.comboBox_penColor.currentIndexChanged.connect(
            self.on_pen_color_change)  # 关联下拉列表的当前索引变更信号与函数on_PenColorChange

        self.helplabel = QLabel()
        self.helplabel.setText("Hi,Welcome to use EIVideo\n"
                               "This is a guide for EIVideo,\n"
                               "please check\n"
                               "1. Choose 'Add' for a video\n"
                               "2. Click 'Play' to start playing\n"
                               "3. At this point, all functions \n"
                               "are unlocked\n"
                               "4. Paint and enjoy it!\n")

        self.widget2 = QtWidgets.QWidget(self.frame)
        self.widget2.setGeometry(860, 60, 200, 300)
        self.widget2.setObjectName("widget2")
        self.rightLayout = QtWidgets.QVBoxLayout(self.widget2)
        self.rightLayout.setContentsMargins(0, 0, 0, 0)
        self.rightLayout.setObjectName("rightLayout")
        self.rightLayout.addWidget(self.helplabel)
        self.rightLayout.addSpacing(50)
        self.rightLayout.addWidget(self.cbtn_Eraser)
        self.rightLayout.addWidget(self.btn_Clear)
        self.colorLayout = QtWidgets.QHBoxLayout(self.widget2)
        self.colorLayout.setContentsMargins(0, 0, 0, 0)
        self.colorLayout.setObjectName('colorLayout')
        self.colorLayout.addWidget(self.label_penColor)
        self.colorLayout.addWidget(self.comboBox_penColor)
        self.rightLayout.addLayout(self.colorLayout)



        # pushButton_6 -> GO
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(870, 600, 150, 90)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.infer)

        self.widget1 = QtWidgets.QWidget(self.frame)
        self.widget1.move(60, 520)
        self.widget1.setObjectName("widget1")
        self.barLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.barLayout.setContentsMargins(0, 0, 0, 0)
        self.barLayout.setObjectName("barLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.timeLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.timeLayout.setContentsMargins(0, 0, 0, 0)
        self.timeLayout.setObjectName("horizontalLayout")

        self.playbtn = QtWidgets.QPushButton(self.widget1)
        self.playbtn.setObjectName("playbtn")
        self.playbtn.clicked.connect(lambda: self.btn_func(self.playbtn))
        self.horizontalLayout.addWidget(self.playbtn)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda: self.btn_func(self.pushButton_2))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(lambda: self.btn_func(self.pushButton_4))
        self.horizontalLayout.addWidget(self.pushButton_4)

        self.timeLayout.addWidget(self.progress_slider)
        self.timeLayout.addWidget(self.time_label)
        self.barLayout.addSpacing(20)
        self.barLayout.addLayout(self.timeLayout)
        self.barLayout.addSpacing(30)
        self.barLayout.addLayout(self.horizontalLayout)

        self.splitter = QtWidgets.QSplitter(self.frame)
        self.splitter.setGeometry(QtCore.QRect(71, 670, 750, 20))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(self.splitter)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1327, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_6.setText(_translate("MainWindow", "GO"))
        self.playbtn.setText(_translate("MainWindow", "Play"))
        self.pushButton_2.setText(_translate("MainWindow", "Stop"))
        self.pushButton_4.setText(_translate("MainWindow", "Add"))
        self.label.setText(_translate("MainWindow", "Hi, This is EIVideo"))


