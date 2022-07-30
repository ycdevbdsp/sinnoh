# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'collision.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CollisionEditor(object):
    def setupUi(self, CollisionEditor):
        CollisionEditor.setObjectName("CollisionEditor")
        CollisionEditor.resize(1097, 941)
        self.uiColHeightSB = QtWidgets.QSpinBox(CollisionEditor)
        self.uiColHeightSB.setGeometry(QtCore.QRect(70, 170, 42, 22))
        self.uiColHeightSB.setObjectName("uiColHeightSB")
        self.colValueLabel = QtWidgets.QLabel(CollisionEditor)
        self.colValueLabel.setGeometry(QtCore.QRect(10, 30, 81, 16))
        self.colValueLabel.setObjectName("colValueLabel")
        self.colHeightLabel = QtWidgets.QLabel(CollisionEditor)
        self.colHeightLabel.setGeometry(QtCore.QRect(30, 160, 47, 31))
        self.colHeightLabel.setObjectName("colHeightLabel")
        self.colWidthLabel = QtWidgets.QLabel(CollisionEditor)
        self.colWidthLabel.setGeometry(QtCore.QRect(30, 132, 47, 31))
        self.colWidthLabel.setObjectName("colWidthLabel")
        self.btnColSaveCell = QtWidgets.QPushButton(CollisionEditor)
        self.btnColSaveCell.setGeometry(QtCore.QRect(90, 60, 75, 23))
        self.btnColSaveCell.setObjectName("btnColSaveCell")
        self.uiColValue = QtWidgets.QLineEdit(CollisionEditor)
        self.uiColValue.setGeometry(QtCore.QRect(90, 30, 71, 20))
        self.uiColValue.setObjectName("uiColValue")
        self.uiColWidthSB = QtWidgets.QSpinBox(CollisionEditor)
        self.uiColWidthSB.setGeometry(QtCore.QRect(70, 140, 42, 22))
        self.uiColWidthSB.setObjectName("uiColWidthSB")
        self.btnColSaveMatrix = QtWidgets.QPushButton(CollisionEditor)
        self.btnColSaveMatrix.setGeometry(QtCore.QRect(90, 90, 75, 23))
        self.btnColSaveMatrix.setObjectName("btnColSaveMatrix")
        self.scrollArea = QtWidgets.QScrollArea(CollisionEditor)
        self.scrollArea.setGeometry(QtCore.QRect(180, 20, 911, 911))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 909, 909))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.scrollAreaWidgetContents)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.uiColMap = ClickLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiColMap.sizePolicy().hasHeightForWidth())
        self.uiColMap.setSizePolicy(sizePolicy)
        self.uiColMap.setMinimumSize(QtCore.QSize(0, 0))
        self.uiColMap.setFrameShape(QtWidgets.QFrame.Box)
        self.uiColMap.setFrameShadow(QtWidgets.QFrame.Raised)
        self.uiColMap.setText("")
        self.uiColMap.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.uiColMap.setObjectName("uiColMap")
        self.verticalLayout_2.addWidget(self.uiColMap)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.uiColExMap = ClickLabel(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiColExMap.sizePolicy().hasHeightForWidth())
        self.uiColExMap.setSizePolicy(sizePolicy)
        self.uiColExMap.setMinimumSize(QtCore.QSize(0, 0))
        self.uiColExMap.setFrameShape(QtWidgets.QFrame.Box)
        self.uiColExMap.setFrameShadow(QtWidgets.QFrame.Raised)
        self.uiColExMap.setText("")
        self.uiColExMap.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.uiColExMap.setObjectName("uiColExMap")
        self.verticalLayout_3.addWidget(self.uiColExMap)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(CollisionEditor)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(CollisionEditor)

    def retranslateUi(self, CollisionEditor):
        _translate = QtCore.QCoreApplication.translate
        CollisionEditor.setWindowTitle(_translate("CollisionEditor", "Form"))
        self.colValueLabel.setText(_translate("CollisionEditor", "Collision Value"))
        self.colHeightLabel.setText(_translate("CollisionEditor", "Height"))
        self.colWidthLabel.setText(_translate("CollisionEditor", "Width"))
        self.btnColSaveCell.setText(_translate("CollisionEditor", "Save Cell"))
        self.btnColSaveMatrix.setText(_translate("CollisionEditor", "Save Matrix"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("CollisionEditor", "Collision"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("CollisionEditor", "Ex Attributes"))
from clicklabel import ClickLabel
