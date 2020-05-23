# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pcb_rc
class Ui_image2textWidget(object):
    def setupUi(self, image2textWidget):
        image2textWidget.setObjectName("MainWindow")
        image2textWidget.setFixedSize(726, 480)
        self.graphicsView = QtWidgets.QGraphicsView(image2textWidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 725, 479))
        self.graphicsView.setStyleSheet("border-image: url(:/pcb_jiemian/2.jpg);")
        self.graphicsView.setObjectName("graphicsView")
        self.centralwidget = QtWidgets.QWidget(image2textWidget)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 10, 401, 61))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 70, 191, 31))
        self.label_2.setStyleSheet("font: 87 14pt \"Arial Black\;border-color: rgb(255, 255, 0);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 100, 181, 31))
        self.label_3.setStyleSheet("font: 13pt \"宋体\";")
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(90, 130, 561, 201))
        self.textEdit.setObjectName("textEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 340, 91, 31))
        self.label_4.setStyleSheet("font: 13pt \"宋体\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 420, 171, 31))
        self.label_5.setStyleSheet("font: 13pt \"宋体\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(70, 380, 221, 31))
        self.label_6.setStyleSheet("font: 10pt \"宋体\";")
        self.label_6.setObjectName("label_6")
        self.pushButtonOpen = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonOpen.setGeometry(QtCore.QRect(230, 420, 31, 31))
        self.pushButtonOpen.setMinimumSize(QtCore.QSize(31, 31))
        self.pushButtonOpen.setMaximumSize(QtCore.QSize(31, 31))
        self.pushButtonOpen.setObjectName("pushButtonOpen")
        self.pushButtonCapture = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonCapture.setGeometry(QtCore.QRect(160, 340, 31, 31))
        self.pushButtonCapture.setMinimumSize(QtCore.QSize(31, 31))
        self.pushButtonCapture.setMaximumSize(QtCore.QSize(31, 31))
        self.pushButtonCapture.setObjectName("pushButtonCapture")
        #image2textWidget.setCentralWidget(self.centralwidget)

        self.retranslateUi(image2textWidget)
        QtCore.QMetaObject.connectSlotsByName(image2textWidget)

    def retranslateUi(self, image2textWidget):
        _translate = QtCore.QCoreApplication.translate
        image2textWidget.setWindowTitle(_translate("image2textWidget", "MainWindow"))
        image2textWidget.setToolTip(_translate("image2textWidget", "<html><head/><body><p><img src=\":/newPrefix/2.jpeg\"/></p></body></html>"))
        image2textWidget.setWhatsThis(_translate("image2textWidget", "<html><head/><body><p><img src=\":/newPrefix/2.jpeg\"/></p></body></html>"))
        self.label.setText(_translate("image2textWidget", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600; color:#ffffff;\">欢迎进入图形文字提取系统</span></p></body></html>"))
        self.label_2.setText(_translate("image2textWidget", "<html><head/><body><p><span style=\" font-size:16pt; color:#000000;\">请选择获取图像方式</span></p></body></html>"))
        self.label_3.setText(_translate("image2textWidget","<html><head/><body><p><span style=\" font-size:13pt; color:#000000;\">1.拖拽上传</span></p></body></html>"))
        self.label_4.setText(_translate("image2textWidget","<html><head/><body><p><span style=\" font-size:13pt; color:#000000;\">2.截屏识图</span></p></body></html>"))
        self.label_5.setText(_translate("image2textWidget","<html><head/><body><p><span style=\" font-size:13pt; color:#000000;\">3.从电脑上搜索图片</span></p></body></html>"))
        self.label_6.setText(_translate("image2textWidget","<html><head/><body><p><span style=\" font-size:12pt; color:#aaaa7f;\">快捷键为：ctrl+shift+alt+f8</span></p></body></html>"))
        self.pushButtonOpen.setText(_translate("image2textWidget", "Open"))
        self.pushButtonCapture.setText(_translate("image2textWidget", "cap"))

#import 1_rc
