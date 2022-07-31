import sys
import UnityPy
import os
from os import path
import re
import json
from tqdm import tqdm
from map import *
from math import floor
from tkinter import filedialog
from tkinter import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QWidget
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor, QTextDocument, QFont
from PyQt5.QtCore import Qt, QSize, QRectF
import clicklabel
from collisioneditor import CollisionEditor
import collisionHeader

    

class Overworld(QMainWindow):


    resized = QtCore.pyqtSignal()
    IsArrayed = False
    CellWidth = 0
    CellHeight = 0
    CollisionEditor = None
    CollisionTrees = {}
    GridWidth = 0
    GridHeight = 0
    Loading = False
    SelectedCell = None
    CellMatrix = {}
    Sinnoh = None
    SinnohAttribute = None
    SinnohAttribute_sp = None
    SinnohAttribute_Ex = None
    SinnohAttribute_Ex_sp = None

    MapMatrixGroup = [
        "Sinnoh",
        "SinnohAttribute",
        "SinnohAttribute_Ex",
        "SinnohAttribute_Ex_sp",
        "SinnohAttribute_sp"
    ]

    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.uiMap.clicked.connect(self.mousePressed)
        self.resized.connect(self.repaintUI)
        self.ui.actionLoad.triggered.connect(self.loadGameSettings)
        self.uiMapRatios = {
            'w': self.ui.uiMap.width() / self.width(),
            'h': self.ui.uiMap.height() / self.height()
        }
        self.ui.uiWidthSB.valueChanged.connect(self.widthChanged)
        self.ui.uiHeightSB.valueChanged.connect(self.heightChanged)
        self.ui.btnSaveCell.clicked.connect(self.saveCell)
        self.ui.btnSaveMatrix.clicked.connect(self.saveMatrix)
        self.ui.btnEditCollision.clicked.connect(self.openCollisionEditor)

    def loadGameSettings(self):
        root = Tk()
        root.withdraw()
        gamesettings = filedialog.askopenfilename()
        attributesList = []
        attributesExList = []

        if path.exists("gamesettings_unpackedmaps"):
            print("ready")
        else:
            env = UnityPy.load(gamesettings)

            for i in tqdm(range(len(env.objects))):
                obj = env.objects[i]
                if obj.type.name == "MonoBehaviour":
                    tree = env.objects[i].read_typetree()

                    if re.search(r'map[0-9]*_[0-9]*.*', tree['m_Name']):
                        #tree['Attributes'] has what we need, but save the whole tree file
                        self.CollisionTrees[tree['m_Name']] = tree
                        
                        #Commented out but retained for debugging purposes.    
                        # if 0:
                        # for at in tree['Attributes']:
                        #     if '_Ex' not in tree['m_Name'] and at not in attributesList:
                        #         attributesList.append(at)
                        #     elif '_Ex' in tree['m_Name'] and at not in attributesExList:
                        #         attributesExList.append(at)
                        
                    elif tree['m_Name'] in self.MapMatrixGroup:
                        if tree['m_Name'] == "Sinnoh":
                            self.Sinnoh = tree
                        elif tree['m_Name'] == "SinnohAttribute":
                            self.SinnohAttribute = tree
                        elif tree['m_Name'] == "SinnohAttribute_Ex":
                            self.SinnohAttribute_Ex = tree
                        elif tree['m_Name'] == "SinnohAttribute_Ex_sp":
                            self.SinnohAttribute_Ex_sp = tree
                        elif tree['m_Name'] == "SinnohAttribute_sp":
                            self.SinnohAttribute_sp = tree
                    
            #Save the collision trees and sinnoh matrix files to disk for faster loading later.    


        #Commented out but retained for debugging purposes.    
        # if 0:
        #     with open('attributesList.json', 'w+') as af:
        #         json.dump({'attributes': attributesList}, af)

        #     with open('attributesExList.json', 'w+') as afex:
        #         json.dump({'attributes':attributesExList}, afex)
        
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

    def openCollisionEditor(self):
        colFileName = f"map{self.CellMatrix['col']}_{self.CellMatrix['row']}"
        exFileName = f"{colFileName}_Ex"

        if colFileName not in self.CollisionTrees:
            newCol = collisionHeader.colHeader
            newCol['m_Name'] = colFileName
            self.CollisionTrees[colFileName] = newCol

        if exFileName not in self.CollisionTrees:
            newEx = collisionHeader.exHeader
            newEx['m_Name'] = exFileName
            self.CollisionTrees[exFileName] = newEx

        collisionData = self.CollisionTrees[colFileName]
        exAttributeData = self.CollisionTrees[exFileName]
        self.CollisionEditor = CollisionEditor(collisionData, exAttributeData)
        self.CollisionEditor.show()


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

        if self.IsArrayed is True:
            for n in range(len(self.Sinnoh['ZoneIDs']['Array'])):
                if self.Sinnoh['ZoneIDs']['Array'][n] == -1000:
                    self.Sinnoh['ZoneIDs']['Array'][n] = -1
        else:
            for n in range(len(self.Sinnoh['ZoneIDs'])):
                if self.Sinnoh['ZoneIDs'][n] == -1000:
                    self.Sinnoh['ZoneIDs'][n] = -1

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

    def mousePressed(self, event, map):
        self.SelectedCell = None

        if self.CellHeight == 0:
            return

        x = floor(event.x() / map.width())
        y = floor(event.y() / map.height())

        row = int((event.y() / self.CellHeight))
        col = int((event.x() / self.CellWidth))
        cell = row * self.GridWidth + col

        self.CellMatrix = {'col':'{:0>2}'.format(col), 'row':'{:0>2}'.format(row)}

        # if 1:
        #     print(f"event.x({event.x()}), event.y({event.y()}); CellWidth({self.CellWidth}); CellHeight({self.CellHeight}); x({x})")
        #     print(cell)

        self.SelectedCell = cell

        if self.SelectedCell > (self.GridHeight * self.GridWidth):
            self.SelectedCell = None
            self.drawOverworld()
            return

        # print(f"Searching {self.SelectedCell}")
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
        # print("width changed")
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
        
        # print(f"GridHeight({self.GridHeight}), GridWidth({self.GridWidth}) [{self.GridHeight*self.GridWidth}], len(zJson)({len(zJson)}")
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

        # print(f"zJson({len(zJson)}, zAttr({len(zAttr)}), zAttrSP({len(zAttrSP)}, zAttrEX({len(zAttrEX)}, zAttrEXSP({len(zAttrEXSP)})")
        
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