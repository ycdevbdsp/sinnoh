import sys
import os
from os import path
import json
from map import *
from tkinter import filedialog
from tkinter import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor, QTextDocument, QFont
from PyQt5.QtCore import Qt, QSize, QRectF
import clicklabel

class Overworld(QMainWindow):


    resized = QtCore.pyqtSignal()

    gridWidth = 0
    gridHeight = 0
    sinnoh = None
    sinnohAttribute = None
    sinnohAttribute_sp = None
    sinnohAttribute_Ex = None
    sinnohAttribute_Ex_sp = None

    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.resized.connect(self.repaintUI)
        self.ui.actionLoad.triggered.connect(self.loadData)
        self.uiMapRatios = {
            'w': self.ui.uiMap.width() / self.width(),
            'h': self.ui.uiMap.height() / self.height()
        }


    def loadData(self):
        root = Tk()
        root.withdraw()
        selectedFolder = filedialog.askdirectory()
        foundData = False
        missing = ""

        #check for all 5 map attribute files:
        #sinnoh.json
        if path.exists(f"{selectedFolder}/sinnoh.json"):
            input = open(f"{selectedFolder}/sinnoh.json")
            self.sinnoh = json.load(input)
        else:
            missing = f"sinnoh.json\n"

        
        #sinnohAttribute.json
        if path.exists(f"{selectedFolder}/sinnohAttribute.json"):
            input = open(f"{selectedFolder}/sinnohAttribute.json")
            self.sinnohAttribute = json.load(input)
        else:
            missing = f"{missing}sinnohAttribute.json\n"

        #sinnohAttribute_sp.json
        if path.exists(f"{selectedFolder}/sinnohAttribute_sp.json"):
            input = open(f"{selectedFolder}/sinnohAttribute_sp.json")
            self.sinnohAttribute_sp = json.load(input)
        else:
            missing = f"{missing}sinnohAttribute_sp.json\n"
        
        #sinnohAttribute_Ex.json
        if path.exists(f"{selectedFolder}/sinnohAttribute_Ex.json"):
            input = open(f"{selectedFolder}/sinnohAttribute_Ex.json")
            self.sinnohAttribute_Ex = json.load(input)
        else:
            missing = f"{missing}sinnohAttribute_Ex.json\n"
        
        #sinnohAttribute_Ex_sp.json
        if path.exists(f"{selectedFolder}/sinnohAttribute_Ex_sp.json"):
            input = open(f"{selectedFolder}/sinnohAttribute_Ex_sp.json")
            self.sinnohAttribute_Ex_sp = json.load(input)
        else:
            missing = f"{missing}sinnohAttribute_Ex_sp.json\n"


        #Any files missing?
        if len(missing) > 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.setText(f"Missing files:\n{missing}")
            msg.setWindowTitle("Missing Data")
            msg.exec_()
            return

        self.gridWidth = self.sinnoh['Width']
        print(len(self.sinnoh['ZoneIDs']))
        zoneIDCount = len(self.sinnoh['ZoneIDs'])
        self.gridHeight = int(zoneIDCount / self.gridWidth)

        if zoneIDCount % self.gridWidth > 0:
            self.gridHeight += 1

        self.drawOverworld()


    def resizeEvent(self, event):
        self.resized.emit()
        return super(Overworld, self).resizeEvent(event)

    def repaintUI(self):
        self.ui.uiMap.resize(QSize(int(self.uiMapRatios['w']*self.width()), int(self.uiMapRatios['h']*self.height())))
        canvas = QtGui.QPixmap(self.ui.uiMap.width(), self.ui.uiMap.height())
        self.ui.uiMap.setPixmap(canvas)
        self.ui.uiMap.pixmap().fill(QtGui.QColor("red"))
        self.ui.uiMap.repaint()

    def drawOverworld(self):
        canvas = QtGui.QPixmap(self.ui.uiMap.width(), self.ui.uiMap.height())
        self.ui.uiMap.setPixmap(canvas)
        self.ui.uiMap.pixmap().fill(QtGui.QColor("white"))
        qp = QPainter(self.ui.uiMap.pixmap())

        qp.setBrush(QBrush(QColor("black"), Qt.SolidPattern))
        pen = QPen(QtGui.QColor("white"))
        qp.setPen(pen)
        
        cellWidth = int(self.ui.uiMap.width() / self.gridWidth)
        cellHeight = int(cellWidth / 2)

        for r in range(self.gridHeight):
            for c in range(self.gridWidth):
                z = self.sinnoh['ZoneIDs'][self.sinnoh['Width']*r + c]
                rect = QRectF(c*cellWidth, r*cellHeight, cellWidth, cellHeight)
                
                if z != -1:
                    zid = '{:0>4}'.format(z)
                    qp.setBrush(QBrush(QColor("white"), Qt.SolidPattern))
                    pen = QPen(QtGui.QColor("black"))
                    qp.setPen(pen)
                else:
                    zid = '{:0>4}'.format(0)
                    qp.setBrush(QBrush(QColor("black"), Qt.SolidPattern))
                    pen = QPen(QtGui.QColor("white"))
                    qp.setPen(pen)
                
                qp.drawRect(rect)
                qp.drawText(rect, Qt.AlignCenter, zid)

        for z in self.sinnoh['ZoneIDs']:
            zid = '{:0>4}'.format(0)
            if z != -1:
                zid = '{:0>4}'.format(z)
            



        self.ui.uiMap.repaint()

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = Overworld()
    w.show()
    sys.exit(app.exec_())