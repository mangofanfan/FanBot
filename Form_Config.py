# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Form_Config.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form_Config(object):
    def setupUi(self, Form_Config):
        if not Form_Config.objectName():
            Form_Config.setObjectName(u"Form_Config")
        Form_Config.resize(600, 380)
        Form_Config.setMinimumSize(QSize(600, 380))
        Form_Config.setMaximumSize(QSize(600, 380))
        icon = QIcon()
        icon.addFile(u"resources/FB-logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        Form_Config.setWindowIcon(icon)
        self.groupBox = QGroupBox(Form_Config)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 10, 561, 151))
        self.lineEdit_botName = QLineEdit(self.groupBox)
        self.lineEdit_botName.setObjectName(u"lineEdit_botName")
        self.lineEdit_botName.setGeometry(QRect(120, 30, 421, 31))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 30, 71, 31))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 90, 71, 31))
        self.checkBox_stopLearn = QCheckBox(self.groupBox)
        self.checkBox_stopLearn.setObjectName(u"checkBox_stopLearn")
        self.checkBox_stopLearn.setGeometry(QRect(130, 70, 401, 71))
        self.groupBox_2 = QGroupBox(Form_Config)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(20, 170, 561, 101))
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 40, 71, 31))
        self.lineEdit_userName = QLineEdit(self.groupBox_2)
        self.lineEdit_userName.setObjectName(u"lineEdit_userName")
        self.lineEdit_userName.setGeometry(QRect(120, 40, 421, 31))
        self.pushButton_clearChatBox = QPushButton(Form_Config)
        self.pushButton_clearChatBox.setObjectName(u"pushButton_clearChatBox")
        self.pushButton_clearChatBox.setGeometry(QRect(20, 330, 111, 31))
        self.pushButton_rollback = QPushButton(Form_Config)
        self.pushButton_rollback.setObjectName(u"pushButton_rollback")
        self.pushButton_rollback.setGeometry(QRect(140, 330, 111, 31))
        self.label_4 = QLabel(Form_Config)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 280, 151, 31))
        self.line = QFrame(Form_Config)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(20, 306, 561, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.pushButton_save = QPushButton(Form_Config)
        self.pushButton_save.setObjectName(u"pushButton_save")
        self.pushButton_save.setGeometry(QRect(170, 280, 81, 28))

        self.retranslateUi(Form_Config)

        QMetaObject.connectSlotsByName(Form_Config)
    # setupUi

    def retranslateUi(self, Form_Config):
        Form_Config.setWindowTitle(QCoreApplication.translate("Form_Config", u"\u5e06\u5f0f\u804a\u5929\u673a\u5668\u4eba - \u8bbe\u7f6e", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form_Config", u"\u673a\u5668\u4eba\u8bbe\u7f6e", None))
        self.label.setText(QCoreApplication.translate("Form_Config", u"<html><head/><body><p align=\"center\">\u540d\u79f0</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Form_Config", u"<html><head/><body><p align=\"center\">\u505c\u6b62\u5b66\u4e60</p></body></html>", None))
        self.checkBox_stopLearn.setText(QCoreApplication.translate("Form_Config", u"\u52fe\u9009\u6b64\u9879\u540e\uff0c\n"
"\u673a\u5668\u4eba\u5c06\u4e0d\u518d\u901a\u8fc7\u4e0e\u7528\u6237\u7684\u5bf9\u8bdd\u8bb0\u5f55\u6765\u66f4\u65b0\u8bed\u6599\u5e93", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form_Config", u"\u7528\u6237\u8d44\u6599", None))
        self.label_3.setText(QCoreApplication.translate("Form_Config", u"<html><head/><body><p align=\"center\">\u540d\u79f0</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.pushButton_clearChatBox.setToolTip(QCoreApplication.translate("Form_Config", u"<html><head/><body><p>\u4e0d\u5f71\u54cd\u673a\u5668\u4eba\u5df2\u7ecf\u83b7\u5f97\u7684\u8bed\u6599\u8d44\u6599\u3002</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_clearChatBox.setText(QCoreApplication.translate("Form_Config", u"\u6e05\u7a7a\u804a\u5929\u6846", None))
#if QT_CONFIG(tooltip)
        self.pushButton_rollback.setToolTip(QCoreApplication.translate("Form_Config", u"<html><head/><body><p>\u5c06\u673a\u5668\u4eba\u6062\u590d\u5230\u521d\u59cb\u72b6\u6001\uff0c\u5373\u6e05\u7a7a\u4e00\u5207\u5df2\u5b58\u5728\u7684\u8bed\u6599\u8d44\u6599\uff0c\u4e0b\u6b21\u542f\u52a8\u65f6\u9700\u8981\u91cd\u65b0\u8bad\u7ec3\u3002</p><p><span style=\" font-weight:600; color:#ff0000;\">\u6b64\u64cd\u4f5c\u4e0d\u53ef\u64a4\u9500\uff01</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_rollback.setText(QCoreApplication.translate("Form_Config", u"\u6062\u590d\u81f3\u521d\u59cb", None))
        self.label_4.setText(QCoreApplication.translate("Form_Config", u"\u5173\u95ed\u672c\u7a97\u53e3\u524d\uff0c\u8bf7\u70b9\u51fb", None))
        self.pushButton_save.setText(QCoreApplication.translate("Form_Config", u"\u4fdd\u5b58\u66f4\u6539", None))
    # retranslateUi

