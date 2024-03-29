import copy
import sys
import UnityPy
import os
from os import path
import re
import json
from tqdm import tqdm
from map import *
from math import floor
from subprocess import run
from tkinter import filedialog
from tkinter import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QWidget
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor, QTextDocument, QFont
from PyQt5.QtCore import Qt, QSize, QRectF
import clicklabel
from collisioneditor import CollisionEditor
import collisionHeader
import zones
    

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
    Masterdatas = {}
    PlaceDatas = {}
    Sinnoh = None
    SinnohAttribute = None
    SinnohAttribute_sp = None
    SinnohAttribute_Ex = None
    SinnohAttribute_Ex_sp = None

    #FILEPATHS

    ROMFS_PATH = ""
    UNPK_ROMFS_PATH = ""
    DPR_PATH = "StreamingAssets/AssetAssistant/Dpr"

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
        self.ui.uiMap.overworld = True
        self.ui.uiMap.clicked.connect(self.cellClicked)
        self.ui.uiMap.doubleclicked.connect(self.cellDoubleClicked)
        self.resized.connect(self.repaintUI)
        # self.ui.actionLoad.triggered.connect(self.loadGameSettings)
        self.ui.actionLoad.triggered.connect(self.loadRomFS)
        self.uiMapRatios = {
            'w': self.ui.uiMap.width() / self.width(),
            'h': self.ui.uiMap.height() / self.height()
        }
        self.ui.uiWidthSB.valueChanged.connect(self.widthChanged)
        self.ui.uiHeightSB.valueChanged.connect(self.heightChanged)
        self.ui.btnSaveCell.clicked.connect(self.saveCell)
        self.ui.btnSaveMatrix.clicked.connect(self.saveMatrix)
        self.ui.btnEditCollision.clicked.connect(self.openCollisionEditor)

    def initializeOverworldMatrix(self):
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


    def loadRomFS(self):
        root = Tk()
        root.withdraw()
        romfs = filedialog.askdirectory()
        unpackGameSettings = False
        unpackMasterData = False
        unpackEvScript = False
        mdPath = f"{self.DPR_PATH}/masterdatas"
        gsPath = f"{self.DPR_PATH}/scriptableobjects/gamesettings"
        evPath = f"{self.DPR_PATH}/ev_script"

        self.ROMFS_PATH = romfs
        self.UNPK_ROMFS_PATH = f"{romfs}_unpacked"
        
        #Look for unpacked masterdatas

        if path.exists(f"{romfs}_unpacked"):
            ret = QMessageBox.question(self, '', "Unpacked data has been found. Do you want to load it instead?", QMessageBox.Yes, QMessageBox.No)

            if ret == QMessageBox.Yes:
                #Load masterdata already unpacked to disc

                if path.exists(f"{romfs}_unpacked/{mdPath}"):
                    for filename in os.listdir(f"{romfs}_unpacked/{mdPath}"):
                        if re.search(r"PlaceData_", filename):
                            filePath = os.path.join(f"{romfs}_unpacked/{mdPath}/{filename}")

                            f = json.load(open(filePath))
                            pdIndex = 0

                            for pd in f['Data']:
                                if self.PlaceDatas.get(pd['zoneID']) is None:
                                    self.PlaceDatas[pd['zoneID']] = { "filename": filename }
                                
                                self.PlaceDatas[pd['zoneID']][pd['ID']] = {
                                    "index": pdIndex,
                                    "data": pd,
                                    "completeFile": f
                                }

                                pdIndex += 1
                else:
                    unpackMasterData = True
                
                if path.exists(f"{romfs}_unpacked/{gsPath}"):
                    for filename in os.listdir(f"{romfs}_unpacked/{gsPath}"):
                        thePath = os.path.join(f"{romfs}_unpacked/{gsPath}/{filename}")

                        if re.search(r'map[0-9]*_[0-9]*.*', filename):
                            #tree['Attributes'] has what we need, but save the whole tree file
                            input = open(thePath)
                            self.CollisionTrees[filename] = json.load(input)
                        elif filename.lower() == "sinnoh":
                            input = open(thePath)
                            self.Sinnoh = json.load(input)
                        elif filename.lower() == "sinnohattribute":
                            input = open(thePath)
                            self.SinnohAttribute = json.load(input)
                        elif filename.lower() == "sinnohattribute_ex":
                            input = open(thePath)
                            self.SinnohAttribute_Ex = json.load(input)
                        elif filename.lower() == "sinnohattribute_sp":
                            input = open(thePath)
                            self.SinnohAttribute_sp = json.load(input)
                        elif filename.lower() == "sinnohattribute_ex_sp":
                            input = open(thePath)
                            self.SinnohAttribute_Ex_sp = json.load(input)
                else:
                    unpackGameSettings = True

                if path.exists(f"{romfs}_unpacked/{evPath}"):
                    for filename in os.listdir(f"{romfs}_unpacked/{evPath}"):
                        thePath = os.path.join(f"{romfs}_unpacked/{evPath}/{filename}")
                else:
                    unpackEvScript = True
            else:
                unpackMasterData = True
                unpackGameSettings = True
                unpackEvScript = True
        else:
            unpackMasterData = True
            unpackGameSettings = True
            unpackEvScript = True
                
        #Look for masterdatas and gamesettings

        if unpackMasterData and path.exists(f"{romfs}/{mdPath}"):
            masterdatas = UnityPy.load(f"{romfs}/{mdPath}")
            
            if path.exists(f"{romfs}_unpacked/{mdPath}") is False:
                os.makedirs(f"{romfs}_unpacked/{mdPath}")

            for i in tqdm(range(len(masterdatas.objects))):
                obj = masterdatas.objects[i]
                if obj.type.name == "MonoBehaviour":
                    tree = masterdatas.objects[i].read_typetree()

                    with open(f"{romfs}_unpacked/{mdPath}/{tree['m_Name']}", 'w+') as out:
                        json.dump(tree, out)

                    if re.search(r"PlaceData_", tree['m_Name']):
                        #This is a placedata. Search through it's Data array and mark every unique
                        #zoneID found. Use the zoneID to mark its place in the PlaceDatas list.
                        
                        pdIndex = 0

                        for pd in tree['Data']:
                            if self.PlaceDatas.get(pd['zoneID']) is None:
                                self.PlaceDatas[pd['zoneID']] = {"filename": tree['m_Name']}

                            self.PlaceDatas[pd['zoneID']][pd['ID']] = {
                                "index": pdIndex,
                                "data": pd,
                                "completeFile": tree
                            }
                            pdIndex += 1


        if unpackGameSettings and path.exists(f"{romfs}/{gsPath}"):
            gamesettings = UnityPy.load(f"{romfs}/{gsPath}")

            if path.exists(f"{romfs}_unpacked/{gsPath}") is False:
                        os.makedirs(f"{romfs}_unpacked/{gsPath}")

            for i in tqdm(range(len(gamesettings.objects))):
                obj = gamesettings.objects[i]
                if obj.type.name == "MonoBehaviour":
                    tree = gamesettings.objects[i].read_typetree()

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
                    
                    with open(f"{romfs}_unpacked/{gsPath}/{tree['m_Name']}", 'w+') as out:
                        json.dump(tree, out)

        if unpackEvScript and path.exists(f"{romfs}/{evPath}"):
            QMessageBox.information(self, '', "Please choose the location of ev-as.")
            root = Tk()
            root.withdraw()
            evas = filedialog.askdirectory()

            run(f"\"{evas}/ev_parse.exe\" -i \"{romfs}/{evPath}\" -o \"{romfs}_unpacked/{evPath}\"")

            QMessageBox.information(self, '', f"Parsed scripts to {romfs}/{evPath}")

        self.initializeOverworldMatrix()
        self.Loading = False
        self.drawOverworld()

    def openCollisionEditor(self, zoneID):
        if self.SelectedCell is None:
            return
            
        if zoneID is False:
            zoneID = self.Sinnoh['ZoneIDs'][self.SelectedCell]

        colFileName = f"map{self.CellMatrix['col']}_{self.CellMatrix['row']}"
        exFileName = f"{colFileName}_Ex"

        if colFileName not in self.CollisionTrees:
            newCol = copy.deepcopy(collisionHeader.colHeader)
            newCol['m_Name'] = colFileName
            self.CollisionTrees[colFileName] = newCol

        if exFileName not in self.CollisionTrees:
            newEx = copy.deepcopy(collisionHeader.exHeader)
            newEx['m_Name'] = exFileName
            self.CollisionTrees[exFileName] = newEx

        collisionData = self.CollisionTrees[colFileName]
        exAttributeData = self.CollisionTrees[exFileName]
        placeData = self.PlaceDatas.get(self.Sinnoh['ZoneIDs'][self.SelectedCell])

        #grab the full file out of the set of placedatas we're working with so we can easily add new things to it later

        pdFile = ''
        for p in placeData:
            if p != 'filename':
                pdFile = placeData[p]['completeFile']

        filePaths = { 'romfs': self.ROMFS_PATH, 'romfs_unpacked': self.UNPK_ROMFS_PATH, 'dpr': self.DPR_PATH, 'pdFile': pdFile }
        self.CollisionEditor = CollisionEditor(collisionData, exAttributeData, placeData, self.CellMatrix, zoneID, filePaths)
        self.CollisionEditor.show()
        print('done showing')


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

        if os.path.exists("output") is False:
            os.makedirs("output")

    def cellClicked(self, event, map):
        if self.setSelectedCell(event) is False:
            return

        if self.SelectedCell is None:
            return

        # print(f"Searching {self.SelectedCell}")
        if self.IsArrayed is True and self.SelectedCell < len(self.Sinnoh['ZoneIDs']['Array']):
            self.ui.uiZoneID.setText(str(self.Sinnoh['ZoneIDs']['Array'][self.SelectedCell]))
            self.ui.uiAttributeFID.setText(str(self.SinnohAttribute['AttributeBlocks']['Array'][self.SelectedCell]['m_FileID']))
            self.ui.uiAttributePID.setText(str(self.SinnohAttribute['AttributeBlocks']['Array'][self.SelectedCell]['m_PathID']))
            self.ui.uiAttributeEXFID.setText(str(self.SinnohAttribute_Ex['AttributeBlocks']['Array'][self.SelectedCell]['m_FileID']))
            self.ui.uiAttributeEXPID.setText(str(self.SinnohAttribute_Ex['AttributeBlocks']['Array'][self.SelectedCell]['m_PathID']))
            self.ui.uiAttributeSPFID.setText(str(self.SinnohAttribute_sp['AttributeBlocks']['Array'][self.SelectedCell]['m_FileID']))
            self.ui.uiAttributeSPPID.setText(str(self.SinnohAttribute_sp['AttributeBlocks']['Array'][self.SelectedCell]['m_PathID']))
            self.ui.uiAttributeEXSPFID.setText(str(self.SinnohAttribute_Ex_sp['AttributeBlocks']['Array'][self.SelectedCell]['m_FileID']))
            self.ui.uiAttributeEXSPPID.setText(str(self.SinnohAttribute_Ex_sp['AttributeBlocks']['Array'][self.SelectedCell]['m_PathID']))
        elif self.SelectedCell < len(self.Sinnoh['ZoneIDs']):
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

    def cellDoubleClicked(self, event, map):
        if self.setSelectedCell(event) is False:
            return

        self.openCollisionEditor(self.Sinnoh['ZoneIDs'][self.SelectedCell])
    
    def setSelectedCell(self, event):
        self.SelectedCell = None

        if self.CellHeight == 0:
            return False

        row = int((event.y() / self.CellHeight))
        col = int((event.x() / self.CellWidth))
        cell = row * self.GridWidth + col

        self.CellMatrix = {'col':'{:0>2}'.format(col), 'row':'{:0>2}'.format(row)}

        self.SelectedCell = cell
        self.ui.uiMapMatrixSelection.setText(f"map{self.CellMatrix['col']}_{self.CellMatrix['row']}")
        if self.SelectedCell > (self.GridHeight * self.GridWidth):
            self.SelectedCell = None
            self.drawOverworld()

        return True


    def widthChanged(self):
        if self.Loading is True:
            return
        
        self.GridWidth = self.ui.uiWidthSB.value()
        self.drawOverworld()

    def heightChanged(self):
        if self.Loading is True:
            return
            
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