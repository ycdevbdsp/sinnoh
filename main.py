import sys
import os
from os import path
import json
from map import *
from math import floor
from tkinter import filedialog
from tkinter import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor, QTextDocument, QFont
from PyQt5.QtCore import Qt, QSize, QRectF
import clicklabel

class Overworld(QMainWindow):


    resized = QtCore.pyqtSignal()
    IsArrayed = False
    CellWidth = 0
    CellHeight = 0
    GridWidth = 0
    GridHeight = 0
    Loading = False
    SelectedCell = None
    Sinnoh = None
    SinnohAttribute = None
    SinnohAttribute_sp = None
    SinnohAttribute_Ex = None
    SinnohAttribute_Ex_sp = None

    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.uiMap.clicked.connect(self.mousePressed)
        self.resized.connect(self.repaintUI)
        self.ui.actionLoad.triggered.connect(self.loadData)
        self.uiMapRatios = {
            'w': self.ui.uiMap.width() / self.width(),
            'h': self.ui.uiMap.height() / self.height()
        }
        self.ui.uiWidthSB.valueChanged.connect(self.widthChanged)
        self.ui.uiHeightSB.valueChanged.connect(self.heightChanged)
        self.ui.btnSaveCell.clicked.connect(self.saveCell)
        self.ui.btnSaveMatrix.clicked.connect(self.saveMatrix)


    def loadData(self):
        root = Tk()
        root.withdraw()
        selectedFolder = filedialog.askdirectory()
        foundData = False
        missing = ""

        self.Loading = True

        #check for all 5 map attribute files:
        #sinnoh.json
        if path.exists(f"{selectedFolder}/sinnoh.json"):
            input = open(f"{selectedFolder}/sinnoh.json")
            self.Sinnoh = json.load(input)
        else:
            missing = f"sinnoh.json\n"

        
        #sinnohAttribute.json
        if path.exists(f"{selectedFolder}/sinnohAttribute.json"):
            input = open(f"{selectedFolder}/sinnohAttribute.json")
            self.SinnohAttribute = json.load(input)
        else:
            missing = f"{missing}sinnohAttribute.json\n"

        #sinnohAttribute_sp.json
        if path.exists(f"{selectedFolder}/sinnohAttribute_sp.json"):
            input = open(f"{selectedFolder}/sinnohAttribute_sp.json")
            self.SinnohAttribute_sp = json.load(input)
        else:
            missing = f"{missing}sinnohAttribute_sp.json\n"
        
        #sinnohAttribute_Ex.json
        if path.exists(f"{selectedFolder}/sinnohAttribute_Ex.json"):
            input = open(f"{selectedFolder}/sinnohAttribute_Ex.json")
            self.SinnohAttribute_Ex = json.load(input)
        else:
            missing = f"{missing}sinnohAttribute_Ex.json\n"
        
        #sinnohAttribute_Ex_sp.json
        if path.exists(f"{selectedFolder}/sinnohAttribute_Ex_sp.json"):
            input = open(f"{selectedFolder}/sinnohAttribute_Ex_sp.json")
            self.SinnohAttribute_Ex_sp = json.load(input)
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

        self.GridWidth = self.Sinnoh['Width']

        if 'Array' in self.Sinnoh['ZoneIDs']:
            zoneIDCount = len(self.Sinnoh['ZoneIDs']['Array'])
            self.IsArrayed = True
        else:
            zoneIDCount = len(self.Sinnoh['ZoneIDs'])
            self.IsArrayed = False

        self.GridHeight = int(zoneIDCount / self.GridWidth)

        #Set the width and height in the spinboxes

        self.ui.uiWidthSB.setValue(self.GridWidth)

        if zoneIDCount % self.GridWidth > 0:
            self.GridHeight += 1

        self.ui.uiHeightSB.setValue(self.GridHeight)

        self.Loading = False
        self.drawOverworld()

    def saveCell(self):
        if self.SelectedCell is None:
            return
        
        if self.IsArrayed is True:
            self.Sinnoh['ZoneIDs']['Array'][self.SelectedCell] = int(self.ui.uiZoneID.text())
            self.SinnohAttribute['AttributeBlocks']['Array'][self.SelectedCell]['m_FileID'] = int(self.ui.uiAttributeFID.text())
            self.SinnohAttribute['AttributeBlocks']['Array'][self.SelectedCell]['m_PathID'] = int(self.ui.uiAttributePID.text())
            self.SinnohAttribute_Ex['AttributeBlocks']['Array'][self.SelectedCell]['m_FileID'] = int(self.ui.uiAttributeEXFID.text())
            self.SinnohAttribute_Ex['AttributeBlocks']['Array'][self.SelectedCell]['m_PathID'] = int(self.ui.uiAttributeEXPID.text())
            self.SinnohAttribute_sp['AttributeBlocks']['Array'][self.SelectedCell]['m_FileID'] = int(self.ui.uiAttributeSPFID.text())
            self.SinnohAttribute_sp['AttributeBlocks']['Array'][self.SelectedCell]['m_PathID'] = int(self.ui.uiAttributeSPPID.text())
            self.SinnohAttribute_Ex_sp['AttributeBlocks']['Array'][self.SelectedCell]['m_FileID'] = int(self.ui.uiAttributeEXSPFID.text())
            self.SinnohAttribute_Ex_sp['AttributeBlocks']['Array'][self.SelectedCell]['m_PathID'] = int(self.ui.uiAttributeEXPID.text())
        else:
            self.Sinnoh['ZoneIDs'][self.SelectedCell] = int(self.ui.uiZoneID.text())
            self.SinnohAttribute['AttributeBlocks'][self.SelectedCell]['m_FileID'] = int(self.ui.uiAttributeFID.text())
            self.SinnohAttribute['AttributeBlocks'][self.SelectedCell]['m_PathID'] = int(self.ui.uiAttributePID.text())
            self.SinnohAttribute_Ex['AttributeBlocks'][self.SelectedCell]['m_FileID'] = int(self.ui.uiAttributeEXFID.text())
            self.SinnohAttribute_Ex['AttributeBlocks'][self.SelectedCell]['m_PathID'] = int(self.ui.uiAttributeEXPID.text())
            self.SinnohAttribute_sp['AttributeBlocks'][self.SelectedCell]['m_FileID'] = int(self.ui.uiAttributeSPFID.text())
            self.SinnohAttribute_sp['AttributeBlocks'][self.SelectedCell]['m_PathID'] = int(self.ui.uiAttributeSPPID.text())
            self.SinnohAttribute_Ex_sp['AttributeBlocks'][self.SelectedCell]['m_FileID'] = int(self.ui.uiAttributeEXSPFID.text())
            self.SinnohAttribute_Ex_sp['AttributeBlocks'][self.SelectedCell]['m_PathID'] = int(self.ui.uiAttributeEXPID.text())

        self.drawOverworld()

    def saveMatrix(self):
        outDir = "output"

        self.Sinnoh['Width'] = self.GridWidth
        self.SinnohAttribute['Width'] = self.GridWidth
        self.SinnohAttribute_Ex['Width'] = self.GridWidth
        self.SinnohAttribute_sp['Width'] = self.GridWidth
        self.SinnohAttribute_Ex_sp['Width'] = self.GridWidth

        if os.path.exists(outDir) == False:
            os.makedirs(outDir)

        with open(f"{outDir}\Sinnoh.json", 'w+') as of:
            json.dump(self.Sinnoh, of)

        with open(f"{outDir}\SinnohAttribute.json", 'w+') as of:
            json.dump(self.SinnohAttribute, of)

        with open(f"{outDir}\SinnohAttribute_sp.json", 'w+') as of:
            json.dump(self.SinnohAttribute_sp, of)

        with open(f"{outDir}\SinnohAttribute_Ex.json", 'w+') as of:
            json.dump(self.SinnohAttribute_Ex, of)

        with open(f"{outDir}\SinnohAttribute_Ex_sp.json", 'w+') as of:
            json.dump(self.SinnohAttribute_Ex_sp, of)

    def mousePressed(self, event):
        self.SelectedCell = None

        x = floor(event.x() / self.ui.uiMap.width())
        y = floor(event.y() / self.ui.uiMap.height())

        cell = (int((event.y() / self.CellHeight)) * self.GridWidth) + int((event.x() / self.CellWidth))

        if 1:
            print(f"event.x({event.x()}), event.y({event.y()}); CellWidth({self.CellWidth}); CellHeight({self.CellHeight}); x({x})")
            print(cell)

        self.SelectedCell = cell

        if self.SelectedCell > (self.GridHeight * self.GridWidth):
            self.SelectedCell = None
            self.drawOverworld()
            return

        print(f"Searching {self.SelectedCell}")
        if self.IsArrayed is True:
            self.ui.uiZoneID.setText(str(self.Sinnoh['ZoneIDs']['Array'][self.SelectedCell]))
            self.ui.uiAttributeFID.setText(str(self.SinnohAttribute['AttributeBlocks']['Array'][self.SelectedCell]['m_FileID']))
            self.ui.uiAttributePID.setText(str(self.SinnohAttribute['AttributeBlocks']['Array'][self.SelectedCell]['m_PathID']))
            self.ui.uiAttributeEXFID.setText(str(self.SinnohAttribute_Ex['AttributeBlocks']['Array'][self.SelectedCell]['m_FileID']))
            self.ui.uiAttributeEXPID.setText(str(self.SinnohAttribute_Ex['AttributeBlocks']['Array'][self.SelectedCell]['m_PathID']))
            self.ui.uiAttributeSPFID.setText(str(self.SinnohAttribute_sp['AttributeBlocks']['Array'][self.SelectedCell]['m_FileID']))
            self.ui.uiAttributeSPPID.setText(str(self.SinnohAttribute_sp['AttributeBlocks']['Array'][self.SelectedCell]['m_PathID']))
            self.ui.uiAttributeEXSPFID.setText(str(self.SinnohAttribute_Ex_sp['AttributeBlocks']['Array'][self.SelectedCell]['m_FileID']))
            self.ui.uiAttributeEXSPPID.setText(str(self.SinnohAttribute_Ex_sp['AttributeBlocks']['Array'][self.SelectedCell]['m_PathID']))
        else:
            self.ui.uiZoneID.setText(str(self.Sinnoh['ZoneIDs'][self.SelectedCell]))
            self.ui.uiAttributeFID.setText(str(self.SinnohAttribute['AttributeBlocks'][self.SelectedCell]['m_FileID']))
            self.ui.uiAttributePID.setText(str(self.SinnohAttribute['AttributeBlocks'][self.SelectedCell]['m_PathID']))
            self.ui.uiAttributeEXFID.setText(str(self.SinnohAttribute_Ex['AttributeBlocks'][self.SelectedCell]['m_FileID']))
            self.ui.uiAttributeEXPID.setText(str(self.SinnohAttribute_Ex['AttributeBlocks'][self.SelectedCell]['m_PathID']))
            self.ui.uiAttributeSPFID.setText(str(self.SinnohAttribute_sp['AttributeBlocks'][self.SelectedCell]['m_FileID']))
            self.ui.uiAttributeSPPID.setText(str(self.SinnohAttribute_sp['AttributeBlocks'][self.SelectedCell]['m_PathID']))
            self.ui.uiAttributeEXSPFID.setText(str(self.SinnohAttribute_Ex_sp['AttributeBlocks'][self.SelectedCell]['m_FileID']))
            self.ui.uiAttributeEXSPPID.setText(str(self.SinnohAttribute_Ex_sp['AttributeBlocks'][self.SelectedCell]['m_PathID']))
    
        self.drawOverworld()

    def widthChanged(self):
        if self.Loading is True:
            return
        
        self.GridWidth = self.ui.uiWidthSB.value()
        print("width changed")
        self.drawOverworld()

    def heightChanged(self):
        if self.Loading is True:
            return
        print(self.ui.uiHeightSB.value())
        self.GridHeight = self.ui.uiHeightSB.value()
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
        
        cellWidth = floor(int(self.ui.uiMap.width() / self.GridWidth))
        cellHeight = int(cellWidth / 2)

        #Depending on if it was exported from AssetStudio or UABEA, the structure
        #will be slightly different. Consider UABEA first:
        
        if self.IsArrayed is True:
            zJson = self.Sinnoh['ZoneIDs']['Array']
            zAttr = self.SinnohAttribute['AttributeBlocks']['Array']
            zAttrSP = self.SinnohAttribute_sp['AttributeBlocks']['Array']
            zAttrEX = self.SinnohAttribute_Ex['AttributeBlocks']['Array']
            zAttrEXSP = self.SinnohAttribute_Ex_sp['AttributeBlocks']['Array']
        else:
            zJson = self.Sinnoh['ZoneIDs']
            zAttr = self.SinnohAttribute['AttributeBlocks']
            zAttrSP = self.SinnohAttribute_sp['AttributeBlocks']
            zAttrEX = self.SinnohAttribute_Ex['AttributeBlocks']
            zAttrEXSP = self.SinnohAttribute_Ex_sp['AttributeBlocks']

        #Before we begin drawing the grid, if width x height exceeds the count of ZoneIDs
        #then we need to add new entries to the arrays of each file.
        
        print(f"GridHeight({self.GridHeight}), GridWidth({self.GridWidth}) [{self.GridHeight*self.GridWidth}], len(zJson)({len(zJson)}")
        if self.GridHeight * self.GridWidth > len(zJson):
            for n in range(self.GridHeight*self.GridWidth - len(zJson)):
                zJson.append(-1000)
                zAttr.append({"m_FileID": 0, "m_PathID": 0})
                zAttrSP.append({"m_FileID": 0, "m_PathID": 0})
                zAttrEX.append({"m_FileID": 0, "m_PathID": 0})
                zAttrEXSP.append({"m_FileID": 0, "m_PathID": 0})
        elif self.GridHeight * self.GridWidth < len(zJson):
            print (len(zJson) - (self.GridHeight * self.GridWidth))
            zJson = zJson[:-(len(zJson) - (self.GridHeight * self.GridWidth))]
            zAttr = zAttr[:-(len(zAttr) - (self.GridHeight * self.GridWidth))]
            zAttrSP = zAttrSP[:-(len(zAttrSP) - (self.GridHeight * self.GridWidth))]
            zAttrEX = zAttrEX[:-(len(zAttrEX) - (self.GridHeight * self.GridWidth))]
            zAttrEXSP = zAttrEXSP[:-(len(zAttrEXSP) - (self.GridHeight * self.GridWidth))]

        print(f"zJson({len(zJson)}, zAttr({len(zAttr)}), zAttrSP({len(zAttrSP)}, zAttrEX({len(zAttrEX)}, zAttrEXSP({len(zAttrEXSP)})")
        
        if self.IsArrayed is True:
            self.Sinnoh['ZoneIDs']['Array'] = zJson
            self.SinnohAttribute['AttributeBlocks']['Array'] = zAttr
            self.SinnohAttribute_sp['AttributeBlocks']['Array'] = zAttrSP
            self.SinnohAttribute_Ex['AttributeBlocks']['Array'] = zAttrEX
            self.SinnohAttribute_Ex_sp['AttributeBlocks']['Array'] = zAttrEXSP
        else:
            self.Sinnoh['ZoneIDs'] = zJson
            self.SinnohAttribute['AttributeBlocks'] = zAttr
            self.SinnohAttribute_sp['AttributeBlocks'] = zAttrSP
            self.SinnohAttribute_Ex['AttributeBlocks'] = zAttrEX
            self.SinnohAttribute_Ex_sp['AttributeBlocks'] = zAttrEXSP


        for r in range(self.GridHeight):
            for c in range(self.GridWidth):
                tCell = self.GridWidth*r + c
                z = zJson[tCell]
                rect = QRectF(c*cellWidth, r*cellHeight, cellWidth, cellHeight)
                
                if z == -1000:
                    zid = '{:0>4}'.format(0)

                    if tCell == self.SelectedCell:
                        qp.setBrush(QBrush(QColor("orange"), Qt.SolidPattern))
                        pen = QPen(QtGui.QColor("black"))
                    else:                        
                        qp.setBrush(QBrush(QColor("red"), Qt.SolidPattern))
                        pen = QPen(QtGui.QColor("black"))

                    qp.setPen(pen)
                elif z != -1:
                    zid = '{:0>4}'.format(z)

                    if tCell == self.SelectedCell:
                        qp.setBrush(QBrush(QColor("blue"), Qt.SolidPattern))
                        pen = QPen(QtGui.QColor("white"))
                    else:
                        qp.setBrush(QBrush(QColor("white"), Qt.SolidPattern))
                        pen = QPen(QtGui.QColor("black"))

                    qp.setPen(pen)
                else:
                    zid = '{:0>4}'.format(0)

                    if tCell == self.SelectedCell:
                        qp.setBrush(QBrush(QColor("blue"), Qt.SolidPattern))
                        pen = QPen(QtGui.QColor("white"))
                    else:
                        qp.setBrush(QBrush(QColor("black"), Qt.SolidPattern))
                        pen = QPen(QtGui.QColor("white"))

                    qp.setPen(pen)
                
                qp.drawRect(rect)
                qp.drawText(rect, Qt.AlignCenter, zid)

        for z in zJson:
            zid = '{:0>4}'.format(0)
            if z != -1:
                zid = '{:0>4}'.format(z)
            
        self.CellWidth = cellWidth
        self.CellHeight = cellHeight


        self.ui.uiMap.repaint()

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = Overworld()
    w.show()
    sys.exit(app.exec_())