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
        CollisionEditor.resize(1099, 941)
        self.uiColHeightSB = QtWidgets.QSpinBox(CollisionEditor)
        self.uiColHeightSB.setGeometry(QtCore.QRect(80, 160, 42, 22))
        self.uiColHeightSB.setObjectName("uiColHeightSB")
        self.colValueLabel = QtWidgets.QLabel(CollisionEditor)
        self.colValueLabel.setGeometry(QtCore.QRect(10, 70, 71, 20))
        self.colValueLabel.setObjectName("colValueLabel")
        self.colHeightLabel = QtWidgets.QLabel(CollisionEditor)
        self.colHeightLabel.setGeometry(QtCore.QRect(40, 150, 47, 31))
        self.colHeightLabel.setObjectName("colHeightLabel")
        self.colWidthLabel = QtWidgets.QLabel(CollisionEditor)
        self.colWidthLabel.setGeometry(QtCore.QRect(40, 122, 47, 31))
        self.colWidthLabel.setObjectName("colWidthLabel")
        self.uiColValue = QtWidgets.QLineEdit(CollisionEditor)
        self.uiColValue.setGeometry(QtCore.QRect(60, 70, 111, 20))
        self.uiColValue.setObjectName("uiColValue")
        self.uiColWidthSB = QtWidgets.QSpinBox(CollisionEditor)
        self.uiColWidthSB.setGeometry(QtCore.QRect(80, 130, 42, 22))
        self.uiColWidthSB.setObjectName("uiColWidthSB")
        self.btnColSaveMatrix = QtWidgets.QPushButton(CollisionEditor)
        self.btnColSaveMatrix.setGeometry(QtCore.QRect(40, 220, 75, 23))
        self.btnColSaveMatrix.setObjectName("btnColSaveMatrix")
        self.tabWidget = QtWidgets.QTabWidget(CollisionEditor)
        self.tabWidget.setGeometry(QtCore.QRect(190, 10, 901, 921))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.scrollArea = QtWidgets.QScrollArea(self.tab)
        self.scrollArea.setGeometry(QtCore.QRect(9, 9, 881, 881))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 879, 879))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setContentsMargins(5, 5, 15, 15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.uiColMap = ClickLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiColMap.sizePolicy().hasHeightForWidth())
        self.uiColMap.setSizePolicy(sizePolicy)
        self.uiColMap.setMinimumSize(QtCore.QSize(0, 0))
        self.uiColMap.setFrameShape(QtWidgets.QFrame.Box)
        self.uiColMap.setFrameShadow(QtWidgets.QFrame.Raised)
        self.uiColMap.setText("")
        self.uiColMap.setScaledContents(False)
        self.uiColMap.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.uiColMap.setObjectName("uiColMap")
        self.verticalLayout_2.addWidget(self.uiColMap)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.tab_2)
        self.scrollArea_2.setGeometry(QtCore.QRect(9, 9, 881, 881))
        self.scrollArea_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 879, 879))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout.setContentsMargins(5, 5, 15, 15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.uiColExMap = ClickLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiColExMap.sizePolicy().hasHeightForWidth())
        self.uiColExMap.setSizePolicy(sizePolicy)
        self.uiColExMap.setMinimumSize(QtCore.QSize(0, 0))
        self.uiColExMap.setFrameShape(QtWidgets.QFrame.Box)
        self.uiColExMap.setFrameShadow(QtWidgets.QFrame.Raised)
        self.uiColExMap.setText("")
        self.uiColExMap.setScaledContents(False)
        self.uiColExMap.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.uiColExMap.setObjectName("uiColExMap")
        self.horizontalLayout.addWidget(self.uiColExMap)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.tabWidget.addTab(self.tab_2, "")
        self.label = QtWidgets.QLabel(CollisionEditor)
        self.label.setGeometry(QtCore.QRect(10, 40, 51, 20))
        self.label.setObjectName("label")
        self.uiColExValue = QtWidgets.QLineEdit(CollisionEditor)
        self.uiColExValue.setGeometry(QtCore.QRect(60, 40, 111, 20))
        self.uiColExValue.setObjectName("uiColExValue")
        self.comboBoxCollisionTile = QtWidgets.QComboBox(CollisionEditor)
        self.comboBoxCollisionTile.setGeometry(QtCore.QRect(70, 100, 111, 22))
        self.comboBoxCollisionTile.setObjectName("comboBoxCollisionTile")
        self.comboBoxCollisionTile.addItem("")
        self.comboBoxCollisionTile.addItem("")
        self.comboBoxCollisionTile.addItem("")
        self.comboBoxCollisionTile.addItem("")
        self.comboBoxCollisionTile.addItem("")
        self.comboBoxCollisionTile.addItem("")
        self.comboBoxCollisionTile.addItem("")
        self.comboBoxCollisionTile.addItem("")
        self.comboBoxCollisionTile.addItem("")
        self.comboBoxCollisionTile.addItem("")
        self.comboBoxCollisionTile.addItem("")
        self.comboBoxCollisionTile.addItem("")
        self.comboBoxCollisionTile.addItem("")
        self.comboBoxCollisionTile.addItem("")
        self.comboBoxCollisionTile.addItem("")
        self.comboBoxCollisionTile.addItem("")
        self.comboBoxCollisionTile.addItem("")
        self.comboBoxCollisionTile.addItem("")
        self.comboBoxCollisionTile.addItem("")
        self.comboBoxCollisionTile.addItem("")
        self.label_2 = QtWidgets.QLabel(CollisionEditor)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 61, 20))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(CollisionEditor)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(CollisionEditor)

    def retranslateUi(self, CollisionEditor):
        _translate = QtCore.QCoreApplication.translate
        CollisionEditor.setWindowTitle(_translate("CollisionEditor", "Form"))
        self.colValueLabel.setText(_translate("CollisionEditor", "Attribute"))
        self.colHeightLabel.setText(_translate("CollisionEditor", "Height"))
        self.colWidthLabel.setText(_translate("CollisionEditor", "Width"))
        self.btnColSaveMatrix.setText(_translate("CollisionEditor", "Save Matrix"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("CollisionEditor", "Collision"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("CollisionEditor", "Ex Attributes"))
        self.label.setText(_translate("CollisionEditor", "Ex Attr"))
        self.comboBoxCollisionTile.setItemText(0, _translate("CollisionEditor", "NONE"))
        self.comboBoxCollisionTile.setItemText(1, _translate("CollisionEditor", "WALKABLE"))
        self.comboBoxCollisionTile.setItemText(2, _translate("CollisionEditor", "WALL"))
        self.comboBoxCollisionTile.setItemText(3, _translate("CollisionEditor", "GRASS"))
        self.comboBoxCollisionTile.setItemText(4, _translate("CollisionEditor", "TALLGRASS"))
        self.comboBoxCollisionTile.setItemText(5, _translate("CollisionEditor", "GRASS2"))
        self.comboBoxCollisionTile.setItemText(6, _translate("CollisionEditor", "GRASS3"))
        self.comboBoxCollisionTile.setItemText(7, _translate("CollisionEditor", "PONDWATER"))
        self.comboBoxCollisionTile.setItemText(8, _translate("CollisionEditor", "OCEANWATER"))
        self.comboBoxCollisionTile.setItemText(9, _translate("CollisionEditor", "PUDDLE"))
        self.comboBoxCollisionTile.setItemText(10, _translate("CollisionEditor", "PUDDLE2"))
        self.comboBoxCollisionTile.setItemText(11, _translate("CollisionEditor", "LEDGELEFT"))
        self.comboBoxCollisionTile.setItemText(12, _translate("CollisionEditor", "LEDGEDOWN"))
        self.comboBoxCollisionTile.setItemText(13, _translate("CollisionEditor", "LEDGEDOWNLEFT"))
        self.comboBoxCollisionTile.setItemText(14, _translate("CollisionEditor", "DOOR?"))
        self.comboBoxCollisionTile.setItemText(15, _translate("CollisionEditor", "BIKELEDGESTART"))
        self.comboBoxCollisionTile.setItemText(16, _translate("CollisionEditor", "BIKELEDGERIDE"))
        self.comboBoxCollisionTile.setItemText(17, _translate("CollisionEditor", "SINKSNOW"))
        self.comboBoxCollisionTile.setItemText(18, _translate("CollisionEditor", "MUD"))
        self.comboBoxCollisionTile.setItemText(19, _translate("CollisionEditor", "SNOW"))
        self.label_2.setText(_translate("CollisionEditor", "Collision Tile"))
from clicklabel import ClickLabel
