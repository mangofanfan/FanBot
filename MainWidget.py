# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWidget(object):
    def setupUi(self, MainWidget):
        if not MainWidget.objectName():
            MainWidget.setObjectName(u"MainWidget")
        MainWidget.resize(857, 567)
        MainWidget.setMinimumSize(QSize(600, 400))
        icon = QIcon()
        icon.addFile(u"resources/FB-logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWidget.setWindowIcon(icon)
        self.formLayout = QFormLayout(MainWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_avatar = QLabel(MainWidget)
        self.label_avatar.setObjectName(u"label_avatar")
        self.label_avatar.setMinimumSize(QSize(160, 160))
        self.label_avatar.setMaximumSize(QSize(160, 160))
        self.label_avatar.setPixmap(QPixmap(u"resources/image.jpg"))
        self.label_avatar.setScaledContents(True)

        self.verticalLayout.addWidget(self.label_avatar)

        self.label_name = QLabel(MainWidget)
        self.label_name.setObjectName(u"label_name")

        self.verticalLayout.addWidget(self.label_name)

        self.pushButton_config = QPushButton(MainWidget)
        self.pushButton_config.setObjectName(u"pushButton_config")
        self.pushButton_config.setMinimumSize(QSize(0, 30))

        self.verticalLayout.addWidget(self.pushButton_config)

        self.pushButton_about = QPushButton(MainWidget)
        self.pushButton_about.setObjectName(u"pushButton_about")
        self.pushButton_about.setMinimumSize(QSize(0, 30))

        self.verticalLayout.addWidget(self.pushButton_about)


        self.formLayout.setLayout(0, QFormLayout.LabelRole, self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.textBrowser = QTextBrowser(MainWidget)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout_2.addWidget(self.textBrowser)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit_input = QLineEdit(MainWidget)
        self.lineEdit_input.setObjectName(u"lineEdit_input")
        self.lineEdit_input.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.lineEdit_input)

        self.pushButton_send = QPushButton(MainWidget)
        self.pushButton_send.setObjectName(u"pushButton_send")
        self.pushButton_send.setMinimumSize(QSize(0, 30))
        self.pushButton_send.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_send)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.verticalLayout_2)


        self.retranslateUi(MainWidget)

        QMetaObject.connectSlotsByName(MainWidget)
    # setupUi

    def retranslateUi(self, MainWidget):
        MainWidget.setWindowTitle(QCoreApplication.translate("MainWidget", u"FanBot - \u5e06\u5f0f\u804a\u5929\u673a\u5668\u4eba", None))
        self.label_avatar.setText("")
        self.label_name.setText(QCoreApplication.translate("MainWidget", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">\u804a\u5929\u673a\u5668\u4eba</span></p><p><span style=\" font-size:10pt;\">\u4ece\u53f3\u4fa7\u7684\u804a\u5929\u6846\u4e2d</span></p><p><span style=\" font-size:10pt;\">\u8f93\u5165\u5185\u5bb9</span></p><p><span style=\" font-size:10pt;\">\u6765\u4e0e\u6211\u804a\u5929\u5427\uff01</span></p></body></html>", None))
        self.pushButton_config.setText(QCoreApplication.translate("MainWidget", u"\u8bbe\u7f6e \u00b7 \u64cd\u4f5c", None))
#if QT_CONFIG(tooltip)
        self.pushButton_about.setToolTip(QCoreApplication.translate("MainWidget", u"<html><head/><body><p>\u5c06\u5728<span style=\" font-weight:600;\">\u6d4f\u89c8\u5668</span>\u4e2d\u6253\u5f00\u7f51\u9875\u3002</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_about.setText(QCoreApplication.translate("MainWidget", u"\u5173\u4e8e \u00b7 \u4ecb\u7ecd", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_input.setToolTip(QCoreApplication.translate("MainWidget", u"<html><head/><body><p>\u8f93\u5165\u5bf9\u8bdd\u5185\u5bb9\uff0c\u7136\u540e\u70b9\u6309\u53f3\u8fb9\u7684\u6309\u94ae\uff0c\u6216\u6572\u51fb\u56de\u8f66\u5373\u53ef\u53d1\u9001\uff01</p><p>\u731c\u731c\u770b\u673a\u5668\u4eba\u4f1a\u5982\u4f55\u56de\u590d\u4f60\uff1f</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_send.setText(QCoreApplication.translate("MainWidget", u"<<", None))
    # retranslateUi

