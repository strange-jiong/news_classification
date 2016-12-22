# -*- coding: utf-8 -*-
##########################
# author:zhicheng liu
# Date	:2016-12-06
##########################

from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
# from tkinter import *
# from PyQt4.QtCore import QString as QString

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# sys.path.append('../backup/')
# from dealFile import DealFile

QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))


class StandardDialog(QDialog):

    def __init__(self, parent=None):
        super(StandardDialog, self).__init__(parent)

        self.setWindowTitle(u"信息检索大作业分类")
        self.setMinimumSize(500, 500)

        self.setWindowIcon(QtGui.QIcon('souhu.jpg'))

        # self.a=DealFile()

        filePushButton = QPushButton(self.tr("文件对话框"))
        urlPushButton = QPushButton(self.tr("url对话框"))
        okPushButton = QPushButton(self.tr("分类"))

        self.fileLineEdit1 = QLineEdit()
        self.fileLineEdit2 = QLineEdit()
        self.fileLineEdit3 = QLineEdit()

        self.cbw1 = QComboBox()
        self.cbw1.addItem(u"选择分类算法")
        self.cbw1.addItem("NB")
        self.cbw1.addItem("KNN")
        self.cbw1.addItem("SVM")
        # self.cbw1.addItem("algorithm4")

        self.cbw2 = QComboBox()
        self.cbw2.setEditable(True)
        # self.cbw2.insertItem(0, QIcon("souhu.jpg"), u"MI")
        self.cbw2.addItem(u"选择特征选择算法")
        self.cbw2.addItem(u"MI")
        self.cbw2.addItem(u"IG")
        self.cbw2.addItem(u"WLLR")
        # self.cbw2.addItem(u"特征选择算法3")
        # self.cbw2.addItem(u"特征选择算法4")

        self.cbw3 = QComboBox()
        self.cbw3.addItem(u"选择特征数")
        self.cbw3.addItem("10000")
        self.cbw3.addItem("20000")
        self.cbw3.addItem("30000")
        self.cbw3.addItem("40000")

        layout = QGridLayout()
        layout.addWidget(filePushButton, 0, 0)
        layout.addWidget(self.fileLineEdit1, 0, 1)
        layout.addWidget(urlPushButton, 1, 0)
        layout.addWidget(self.fileLineEdit2, 1, 1)
        layout.addWidget(self.cbw1, 2, 0)
        layout.addWidget(self.cbw2, 2, 1)
        layout.addWidget(self.cbw3, 2, 2)
        layout.addWidget(okPushButton, 3, 0)
        layout.addWidget(self.fileLineEdit3, 3, 1)

        self.setLayout(layout)

        self.connect(filePushButton, SIGNAL("clicked()"), self.openFile)
        self.connect(urlPushButton, SIGNAL("clicked()"), self.get_url)
        self.connect(okPushButton, SIGNAL("clicked()"), self.classfiy)
        self.connect(self.cbw1, SIGNAL(
            "currentIndexChanged(int)"), self.chose_algorithm)
        self.connect(self.cbw2, SIGNAL("activated(int)"), self.chose_feature)

        self.connect(self.cbw3, SIGNAL("activated(int)"),
                     self.chose_feature_num)

    def openFile(self):

        # s=QFileDialog.getOpenFileName(self,"Open file dialog","/","url txt files(*.txt)")
        s = QFileDialog.getOpenFileName(
            self, "Open file dialog", "/", "url all files(*)")
        self.fileLineEdit1.setText(str(s))
        if s == "":
            return
        for ss in self.get_fromfile1(s):
            print(ss)

        # print(s)

    def get_fromfile1(self, file11):
        fin = open(file11, 'r')
        i = 0
        while True:
            line = fin.readline()
            if not line:
                break
            ss = line.strip()
            yield ss
        fin.close()

    def get_url(self):
        url = self.fileLineEdit2.text()
        if url != "":
            print(url)
        pass

    def chose_algorithm(self):
        # print("algorithm")
        # feature2 = self.cbw1.currentIndex()
        # print(feature2)
        # feature3 = self.cbw1.currentText()
        # print(feature3)
        # pass

        self.classify_method = self.cbw1.currentText()
        print self.classify_method

    def chose_feature(self):
        # feature=self.cbw2.itemText(int(1))
        # print(feature)
        # feature2 = self.cbw2.currentIndex()
        # print(feature2)
        # feature3 = self.cbw2.currentText()
        # print(feature3)

        self.fs_method = self.cbw2.currentText()
        print self.fs_method

        pass

    def chose_feature_num(self):
        print("choice featrue num")

        pass
        # feature=self.cbw2.itemText(int(1))

    def classfiy(self):
        from test import news_classify

        cla = news_classify(data_path='./test2', stop_path='./stop_words.dat',
                            test_size=0.1,)
        cla.feature_processing(fs_method='MI', fs_num=20000)
        if self.classify_method == 'NB':
            cla.NB()
            cla.test_news()
        elif self.classify_method == 'KNN':
            cla.KNN()
            cla.test_news()
        elif self.classify_method == 'SVM':
            cla.SVM()
            cla.test_news()

        pass

app = QApplication(sys.argv)
form = StandardDialog()
form.show()
app.exec_()
