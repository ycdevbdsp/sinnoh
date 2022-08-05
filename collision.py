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
        self.tabWidget = QtWidgets.QTabWidget(CollisionEditor)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 901, 921))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.tabEvents = QtWidgets.QWidget()
        self.tabEvents.setObjectName("tabEvents")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.tabEvents)
        self.scrollArea_3.setGeometry(QtCore.QRect(9, 9, 524, 524))
        self.scrollArea_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_3.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 522, 522))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.uiEventsMap = ClickLabel(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiEventsMap.sizePolicy().hasHeightForWidth())
        self.uiEventsMap.setSizePolicy(sizePolicy)
        self.uiEventsMap.setMinimumSize(QtCore.QSize(0, 0))
        self.uiEventsMap.setFrameShape(QtWidgets.QFrame.Box)
        self.uiEventsMap.setFrameShadow(QtWidgets.QFrame.Raised)
        self.uiEventsMap.setText("")
        self.uiEventsMap.setScaledContents(False)
        self.uiEventsMap.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.uiEventsMap.setObjectName("uiEventsMap")
        self.verticalLayout_3.addWidget(self.uiEventsMap)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.formLayoutWidget = QtWidgets.QWidget(self.tabEvents)
        self.formLayoutWidget.setGeometry(QtCore.QRect(550, 10, 213, 595))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setContentsMargins(5, 5, 5, 5)
        self.formLayout.setObjectName("formLayout")
        self.iDLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.iDLabel.setObjectName("iDLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.iDLabel)
        self.pdID = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.pdID.setObjectName("pdID")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.pdID)
        self.trainerIDLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.trainerIDLabel.setObjectName("trainerIDLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.trainerIDLabel)
        self.pdTrainerID = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.pdTrainerID.setObjectName("pdTrainerID")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pdTrainerID)
        self.oGILabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.oGILabel.setObjectName("oGILabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.oGILabel)
        self.pdOGI = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.pdOGI.setObjectName("pdOGI")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pdOGI)
        self.positionXLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.positionXLabel.setObjectName("positionXLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.positionXLabel)
        self.pdPositionX = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.pdPositionX.setAlignment(QtCore.Qt.AlignCenter)
        self.pdPositionX.setObjectName("pdPositionX")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.pdPositionX)
        self.positionYLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.positionYLabel.setObjectName("positionYLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.positionYLabel)
        self.pdPositionY = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.pdPositionY.setAlignment(QtCore.Qt.AlignCenter)
        self.pdPositionY.setObjectName("pdPositionY")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.pdPositionY)
        self.heightLayerLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.heightLayerLabel.setObjectName("heightLayerLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.heightLayerLabel)
        self.pdHeightLayer = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.pdHeightLayer.setObjectName("pdHeightLayer")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.pdHeightLayer)
        self.rotationLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.rotationLabel.setObjectName("rotationLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.rotationLabel)
        self.pdRotation = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.pdRotation.setObjectName("pdRotation")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.pdRotation)
        self.moveLimitXLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.moveLimitXLabel.setObjectName("moveLimitXLabel")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.moveLimitXLabel)
        self.pdMoveLimitX = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.pdMoveLimitX.setAlignment(QtCore.Qt.AlignCenter)
        self.pdMoveLimitX.setObjectName("pdMoveLimitX")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.pdMoveLimitX)
        self.moveLimitYLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.moveLimitYLabel.setObjectName("moveLimitYLabel")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.moveLimitYLabel)
        self.pdMoveLimitY = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.pdMoveLimitY.setAlignment(QtCore.Qt.AlignCenter)
        self.pdMoveLimitY.setObjectName("pdMoveLimitY")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.pdMoveLimitY)
        self.moveCodeLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.moveCodeLabel.setObjectName("moveCodeLabel")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.moveCodeLabel)
        self.pdMoveCode = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.pdMoveCode.setObjectName("pdMoveCode")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.pdMoveCode)
        self.moveParam0Label = QtWidgets.QLabel(self.formLayoutWidget)
        self.moveParam0Label.setObjectName("moveParam0Label")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.moveParam0Label)
        self.pdMoveParam0 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.pdMoveParam0.setObjectName("pdMoveParam0")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.pdMoveParam0)
        self.moveParam1Label = QtWidgets.QLabel(self.formLayoutWidget)
        self.moveParam1Label.setObjectName("moveParam1Label")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.moveParam1Label)
        self.pdMoveParam1 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.pdMoveParam1.setObjectName("pdMoveParam1")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.pdMoveParam1)
        self.moveParam2Label = QtWidgets.QLabel(self.formLayoutWidget)
        self.moveParam2Label.setObjectName("moveParam2Label")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.moveParam2Label)
        self.pdMoveParam2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.pdMoveParam2.setObjectName("pdMoveParam2")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.pdMoveParam2)
        self.talkLabelLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.talkLabelLabel.setObjectName("talkLabelLabel")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.talkLabelLabel)
        self.pdTalkLabel = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.pdTalkLabel.setObjectName("pdTalkLabel")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.pdTalkLabel)
        self.contactLabelLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.contactLabelLabel.setObjectName("contactLabelLabel")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.contactLabelLabel)
        self.pdContactLabel = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.pdContactLabel.setObjectName("pdContactLabel")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.pdContactLabel)
        self.workLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.workLabel.setObjectName("workLabel")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.LabelRole, self.workLabel)
        self.pdWork = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.pdWork.setObjectName("pdWork")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.FieldRole, self.pdWork)
        self.dowsingLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.dowsingLabel.setObjectName("dowsingLabel")
        self.formLayout.setWidget(16, QtWidgets.QFormLayout.LabelRole, self.dowsingLabel)
        self.pdDowsing = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.pdDowsing.setObjectName("pdDowsing")
        self.formLayout.setWidget(16, QtWidgets.QFormLayout.FieldRole, self.pdDowsing)
        self.loadFirstLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.loadFirstLabel.setObjectName("loadFirstLabel")
        self.formLayout.setWidget(17, QtWidgets.QFormLayout.LabelRole, self.loadFirstLabel)
        self.pdLoadFirst = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.pdLoadFirst.setObjectName("pdLoadFirst")
        self.formLayout.setWidget(17, QtWidgets.QFormLayout.FieldRole, self.pdLoadFirst)
        self.doNotLoadLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.doNotLoadLabel.setObjectName("doNotLoadLabel")
        self.formLayout.setWidget(18, QtWidgets.QFormLayout.LabelRole, self.doNotLoadLabel)
        self.pdDoNotLoad = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.pdDoNotLoad.setObjectName("pdDoNotLoad")
        self.formLayout.setWidget(18, QtWidgets.QFormLayout.FieldRole, self.pdDoNotLoad)
        self.talkToRangeLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.talkToRangeLabel.setObjectName("talkToRangeLabel")
        self.formLayout.setWidget(19, QtWidgets.QFormLayout.LabelRole, self.talkToRangeLabel)
        self.pdTalkToRange = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.pdTalkToRange.setObjectName("pdTalkToRange")
        self.formLayout.setWidget(19, QtWidgets.QFormLayout.FieldRole, self.pdTalkToRange)
        self.talkToSizeXLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.talkToSizeXLabel.setObjectName("talkToSizeXLabel")
        self.formLayout.setWidget(20, QtWidgets.QFormLayout.LabelRole, self.talkToSizeXLabel)
        self.pdTalkToSizeX = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.pdTalkToSizeX.setObjectName("pdTalkToSizeX")
        self.formLayout.setWidget(20, QtWidgets.QFormLayout.FieldRole, self.pdTalkToSizeX)
        self.talkToSizeYLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.talkToSizeYLabel.setObjectName("talkToSizeYLabel")
        self.formLayout.setWidget(21, QtWidgets.QFormLayout.LabelRole, self.talkToSizeYLabel)
        self.pdTalkToSizeY = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.pdTalkToSizeY.setObjectName("pdTalkToSizeY")
        self.formLayout.setWidget(21, QtWidgets.QFormLayout.FieldRole, self.pdTalkToSizeY)
        self.talkBitLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.talkBitLabel.setObjectName("talkBitLabel")
        self.formLayout.setWidget(22, QtWidgets.QFormLayout.LabelRole, self.talkBitLabel)
        self.pdTalkBit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.pdTalkBit.setObjectName("pdTalkBit")
        self.formLayout.setWidget(22, QtWidgets.QFormLayout.FieldRole, self.pdTalkBit)
        self.tabWidget.addTab(self.tabEvents, "")
        self.tabCollision = QtWidgets.QWidget()
        self.tabCollision.setObjectName("tabCollision")
        self.scrollArea = QtWidgets.QScrollArea(self.tabCollision)
        self.scrollArea.setGeometry(QtCore.QRect(9, 9, 524, 524))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 522, 522))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
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
        self.uiColValue = QtWidgets.QLineEdit(self.tabCollision)
        self.uiColValue.setGeometry(QtCore.QRect(620, 50, 111, 20))
        self.uiColValue.setObjectName("uiColValue")
        self.colHeightLabel = QtWidgets.QLabel(self.tabCollision)
        self.colHeightLabel.setGeometry(QtCore.QRect(790, 50, 47, 31))
        self.colHeightLabel.setObjectName("colHeightLabel")
        self.colValueLabel = QtWidgets.QLabel(self.tabCollision)
        self.colValueLabel.setGeometry(QtCore.QRect(570, 50, 43, 13))
        self.colValueLabel.setObjectName("colValueLabel")
        self.uiColHeightSB = QtWidgets.QSpinBox(self.tabCollision)
        self.uiColHeightSB.setGeometry(QtCore.QRect(830, 60, 42, 22))
        self.uiColHeightSB.setObjectName("uiColHeightSB")
        self.colWidthLabel = QtWidgets.QLabel(self.tabCollision)
        self.colWidthLabel.setGeometry(QtCore.QRect(790, 22, 47, 31))
        self.colWidthLabel.setObjectName("colWidthLabel")
        self.uiColWidthSB = QtWidgets.QSpinBox(self.tabCollision)
        self.uiColWidthSB.setGeometry(QtCore.QRect(830, 30, 42, 22))
        self.uiColWidthSB.setObjectName("uiColWidthSB")
        self.label_2 = QtWidgets.QLabel(self.tabCollision)
        self.label_2.setGeometry(QtCore.QRect(560, 80, 61, 20))
        self.label_2.setObjectName("label_2")
        self.comboBoxCollisionTile = QtWidgets.QComboBox(self.tabCollision)
        self.comboBoxCollisionTile.setGeometry(QtCore.QRect(620, 80, 111, 22))
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
        self.tabWidget.addTab(self.tabCollision, "")
        self.tabExAttributes = QtWidgets.QWidget()
        self.tabExAttributes.setObjectName("tabExAttributes")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.tabExAttributes)
        self.scrollArea_2.setGeometry(QtCore.QRect(9, 9, 524, 524))
        self.scrollArea_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 522, 522))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
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
        self.uiColExValue = QtWidgets.QLineEdit(self.tabExAttributes)
        self.uiColExValue.setGeometry(QtCore.QRect(600, 20, 111, 20))
        self.uiColExValue.setObjectName("uiColExValue")
        self.label = QtWidgets.QLabel(self.tabExAttributes)
        self.label.setGeometry(QtCore.QRect(550, 20, 51, 20))
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.tabExAttributes, "")
        self.btnColSaveMatrix = QtWidgets.QPushButton(CollisionEditor)
        self.btnColSaveMatrix.setGeometry(QtCore.QRect(920, 30, 75, 23))
        self.btnColSaveMatrix.setObjectName("btnColSaveMatrix")

        self.retranslateUi(CollisionEditor)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(CollisionEditor)

    def retranslateUi(self, CollisionEditor):
        _translate = QtCore.QCoreApplication.translate
        CollisionEditor.setWindowTitle(_translate("CollisionEditor", "Form"))
        self.iDLabel.setText(_translate("CollisionEditor", "ID:"))
        self.trainerIDLabel.setText(_translate("CollisionEditor", "TrainerID:"))
        self.oGILabel.setText(_translate("CollisionEditor", "OGI:"))
        self.positionXLabel.setText(_translate("CollisionEditor", "PositionX:"))
        self.positionYLabel.setText(_translate("CollisionEditor", "PositionY:"))
        self.heightLayerLabel.setText(_translate("CollisionEditor", "Height Layer:"))
        self.rotationLabel.setText(_translate("CollisionEditor", "Rotation:"))
        self.moveLimitXLabel.setText(_translate("CollisionEditor", "Move Limit X:"))
        self.moveLimitYLabel.setText(_translate("CollisionEditor", "Move Limit Y:"))
        self.moveCodeLabel.setText(_translate("CollisionEditor", "Move Code:"))
        self.moveParam0Label.setText(_translate("CollisionEditor", "Move Param 0:"))
        self.moveParam1Label.setText(_translate("CollisionEditor", "Move Param 1:"))
        self.moveParam2Label.setText(_translate("CollisionEditor", "Move Param 2:"))
        self.talkLabelLabel.setText(_translate("CollisionEditor", "Talk Label:"))
        self.contactLabelLabel.setText(_translate("CollisionEditor", "Contact Label:"))
        self.workLabel.setText(_translate("CollisionEditor", "Work:"))
        self.dowsingLabel.setText(_translate("CollisionEditor", "Dowsing:"))
        self.loadFirstLabel.setText(_translate("CollisionEditor", "Load First:"))
        self.doNotLoadLabel.setText(_translate("CollisionEditor", "DoNotLoad:"))
        self.talkToRangeLabel.setText(_translate("CollisionEditor", "Talk To Range:"))
        self.talkToSizeXLabel.setText(_translate("CollisionEditor", "Talk To SizeX:"))
        self.talkToSizeYLabel.setText(_translate("CollisionEditor", "Talk To SizeY:"))
        self.talkBitLabel.setText(_translate("CollisionEditor", "Talk Bit:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabEvents), _translate("CollisionEditor", "Events"))
        self.colHeightLabel.setText(_translate("CollisionEditor", "Height"))
        self.colValueLabel.setText(_translate("CollisionEditor", "Attribute"))
        self.colWidthLabel.setText(_translate("CollisionEditor", "Width"))
        self.label_2.setText(_translate("CollisionEditor", "Collision Tile"))
        self.comboBoxCollisionTile.setItemText(0, _translate("CollisionEditor", "UNKNOWN"))
        self.comboBoxCollisionTile.setItemText(1, _translate("CollisionEditor", "WALKABLE"))
        self.comboBoxCollisionTile.setItemText(2, _translate("CollisionEditor", "WALL"))
        self.comboBoxCollisionTile.setItemText(3, _translate("CollisionEditor", "GRASS"))
        self.comboBoxCollisionTile.setItemText(4, _translate("CollisionEditor", "TALLGRASS"))
        self.comboBoxCollisionTile.setItemText(5, _translate("CollisionEditor", "GRASS2"))
        self.comboBoxCollisionTile.setItemText(6, _translate("CollisionEditor", "GRASS3"))
        self.comboBoxCollisionTile.setItemText(7, _translate("CollisionEditor", "PONDWATER"))
        self.comboBoxCollisionTile.setItemText(8, _translate("CollisionEditor", "OCEANWATER"))
        self.comboBoxCollisionTile.setItemText(9, _translate("CollisionEditor", "PUDDLE"))
        self.comboBoxCollisionTile.setItemText(10, _translate("CollisionEditor", "WALKABLEWATER"))
        self.comboBoxCollisionTile.setItemText(11, _translate("CollisionEditor", "PUDDLE2"))
        self.comboBoxCollisionTile.setItemText(12, _translate("CollisionEditor", "SAND"))
        self.comboBoxCollisionTile.setItemText(13, _translate("CollisionEditor", "LEDGERIGHT"))
        self.comboBoxCollisionTile.setItemText(14, _translate("CollisionEditor", "LEDGELEFT"))
        self.comboBoxCollisionTile.setItemText(15, _translate("CollisionEditor", "LEDGEDOWN"))
        self.comboBoxCollisionTile.setItemText(16, _translate("CollisionEditor", "LEDGEDOWNLEFT"))
        self.comboBoxCollisionTile.setItemText(17, _translate("CollisionEditor", "ROCKCLIMBVERT"))
        self.comboBoxCollisionTile.setItemText(18, _translate("CollisionEditor", "ROCKCLIMBHORI"))
        self.comboBoxCollisionTile.setItemText(19, _translate("CollisionEditor", "???"))
        self.comboBoxCollisionTile.setItemText(20, _translate("CollisionEditor", "DOOR?"))
        self.comboBoxCollisionTile.setItemText(21, _translate("CollisionEditor", "PASSAGELEFT"))
        self.comboBoxCollisionTile.setItemText(22, _translate("CollisionEditor", "PASSAGERIGHT"))
        self.comboBoxCollisionTile.setItemText(23, _translate("CollisionEditor", "PASSAGEDOWN"))
        self.comboBoxCollisionTile.setItemText(24, _translate("CollisionEditor", "TREEENTER"))
        self.comboBoxCollisionTile.setItemText(25, _translate("CollisionEditor", "BRIDGESTART?"))
        self.comboBoxCollisionTile.setItemText(26, _translate("CollisionEditor", "BRDGOVRGRND"))
        self.comboBoxCollisionTile.setItemText(27, _translate("CollisionEditor", "BRDGOVRWATER"))
        self.comboBoxCollisionTile.setItemText(28, _translate("CollisionEditor", "BIKELEDGERIDE"))
        self.comboBoxCollisionTile.setItemText(29, _translate("CollisionEditor", "BIKELEDGEHORI"))
        self.comboBoxCollisionTile.setItemText(30, _translate("CollisionEditor", "BERRYSOIL"))
        self.comboBoxCollisionTile.setItemText(31, _translate("CollisionEditor", "SINKSNOW"))
        self.comboBoxCollisionTile.setItemText(32, _translate("CollisionEditor", "SINKSNOWPRMTR"))
        self.comboBoxCollisionTile.setItemText(33, _translate("CollisionEditor", "MUD"))
        self.comboBoxCollisionTile.setItemText(34, _translate("CollisionEditor", "SNOW"))
        self.comboBoxCollisionTile.setItemText(35, _translate("CollisionEditor", "GRASSINSNOW"))
        self.comboBoxCollisionTile.setItemText(36, _translate("CollisionEditor", "BIKERACK"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCollision), _translate("CollisionEditor", "Collision"))
        self.label.setText(_translate("CollisionEditor", "Ex Attr"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabExAttributes), _translate("CollisionEditor", "Ex Attributes"))
        self.btnColSaveMatrix.setText(_translate("CollisionEditor", "Save Matrix"))
from clicklabel import ClickLabel
