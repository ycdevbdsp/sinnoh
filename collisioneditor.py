import json
import os
from os import path
from tqdm import tqdm
from map import *
from math import floor
from tkinter import filedialog
from tkinter import *
from PyQt5.QtWidgets import QWidget, QMessageBox, QShortcut
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor, QKeySequence
from PyQt5.QtCore import Qt, QRectF
import clicklabel
import collision
import zones
from constants import *



class CollisionEditor(QWidget):
    
    CellSize = None
    CellHeight = 0
    CollisionData = None
    EventsMapSelected = None
    ExData = None
    GridHeight = 0
    GridWidth = 0
    Loading = True
    PlaceData = None
    PlaceDataCells = {}
    SelectedCell = None
    SelectedPlaceData = None
    UpdateTile = True
    ZoneID = 0

    #FILEPATHS
    ROMFS_PATH = ""
    UNPK_ROMFS_PATH = ""
    DPR_PATH = ""
    SCRIPT_PATH = None
    TRAINER_SCRIPT_PATH = None
    EV_SCRIPT = {}

    #PLACEDATA MOVEMENT
    PD_MOVE_KEYS = [QtCore.Qt.Key.Key_Left, QtCore.Qt.Key.Key_Right, QtCore.Qt.Key.Key_Up, QtCore.Qt.Key.Key_Down]
    SELECTED_PLACEDATA_POS = {}

    def __init__(self, collisionData, exData, placeData, mapOffsets, zoneID, filepaths, parent=None):
        super().__init__()
        self.ui = collision.Ui_CollisionEditor()
        self.ui.setupUi(self)
        self.ui.uiColMap.clicked.connect(self.mousePressed)
        self.ui.uiColExMap.clicked.connect(self.mousePressed)
        self.ui.uiEventsMap.clicked.connect(self.eventsMousePressed)
        self.ui.uiEventsMap.keypressed.connect(self.keyPressed)
        self.ui.uiColHeightSB.valueChanged.connect(self.heightChanged)
        self.ui.uiColWidthSB.valueChanged.connect(self.widthChanged)
        self.ui.btnColSaveMatrix.clicked.connect(self.saveMatrix)
        self.ui.btnSaveEvent.clicked.connect(self.saveEvent)
        self.ui.comboBoxCollisionTile.currentTextChanged.connect(self.collisionTileChanged)
        self.CollisionData = collisionData
        self.ExData = exData
        self.PlaceData = placeData
        self.MapOffsets = mapOffsets
        self.ZoneID = str(zoneID)
        self.ROMFS_PATH = filepaths['romfs']
        self.UNPK_ROMFS_PATH = filepaths['romfs_unpacked']
        self.DPR_PATH = filepaths['dpr']

        QShortcut(QKeySequence(Qt.Key.Key_Left), self, activated=self.movePDLeft)
        QShortcut(QKeySequence(Qt.Key.Key_Up), self, activated=self.movePDUp)
        QShortcut(QKeySequence(Qt.Key.Key_Right), self, activated=self.movePDRight)
        QShortcut(QKeySequence(Qt.Key.Key_Down), self, activated=self.movePDDown)
        #Since the map and map_*_ex files are intended to go together, we will assume they
        #should have the same dimensions.

        self.GridWidth = self.CollisionData['Width']
        self.GridHeight = int(len(self.CollisionData['Attributes']) / self.GridWidth)

        #Mark the location of the associated ev_script file
        self.SCRIPT_PATH = open(f"{self.UNPK_ROMFS_PATH}/{self.DPR_PATH}/ev_script/{str(zones.zones[self.ZoneID]['WarpName'].lower())}.ev")
        self.TRAINER_SCRIPT_PATH = open(f"{self.UNPK_ROMFS_PATH}/{self.DPR_PATH}/ev_script/trainer.ev")

        if self.SCRIPT_PATH is not None:
            lines = self.SCRIPT_PATH.readlines()
            scriptHeader = ""

            for line in lines:
                if len(line) > 0 and line[0] != '\t':
                    scriptHeader = line.replace(':', '').strip()
                    print(scriptHeader)
                    self.EV_SCRIPT[scriptHeader] = []
                else:
                    self.EV_SCRIPT[scriptHeader].append(line.strip())
        
        if self.TRAINER_SCRIPT_PATH is not None:
            lines = self.TRAINER_SCRIPT_PATH.readlines()
            scriptHeader = ""

            for line in lines:
                if len(line) > 0 and line[0] != '\t':
                    scriptHeader = line.replace(':', '').strip()
                    print(scriptHeader)
                    self.EV_SCRIPT[scriptHeader] = []
                else:
                    self.EV_SCRIPT[scriptHeader].append(line.strip())

        self.ui.uiColHeightSB.setValue(self.GridHeight)
        self.ui.uiColWidthSB.setValue(self.GridWidth)
        self.drawCollisions()
        self.Loading = False

    def collisionTileChanged(self):
        if self.SelectedCell == None or (not self.UpdateTile):
            return
        
        cell = self.SelectedCell['cell']
        tile = self.ui.comboBoxCollisionTile.currentText()

        if self.SelectedCell['map'] == self.ui.uiColMap:
            self.CollisionData['Attributes'][cell] = COLLISIONS[tile]
            self.ui.uiColValue.setText(str(COLLISIONS[tile]))
        elif self.SelectedCell['map'] == self.ui.uiColExMap:
            self.ExData['Attributes'][cell] = COLLISIONS[tile]

    def heightChanged(self):
        if self.Loading is True:
            return
            
        self.GridHeight = self.ui.uiColHeightSB.value()
        self.drawCollisions()

    def widthChanged(self):
        if self.Loading is True:
            return

        self.GridWidth = self.ui.uiColWidthSB.value()
        self.drawCollisions()
        
    def drawCollisions(self):
        self.drawCollision(self.ui.uiColMap)
        self.drawCollision(self.ui.uiColExMap)
        self.drawOverworldEventMap(self.ui.uiEventsMap)

    def drawCollision(self, map):
        if os.path.exists(f"maps/{self.CollisionData['m_Name']}c.png"):
            canvas = QtGui.QPixmap(f"maps/{self.CollisionData['m_Name']}c.png")
            map.setPixmap(canvas)
        else:
            if self.CellSize is None:
                    self.CellSize = {}
                    self.CellSize['width'] = int(map.width() / self.GridWidth)
                    self.CellSize['height'] = self.CellSize['width']

            canvas = QtGui.QPixmap(self.CellSize['width'] * self.GridWidth, self.CellSize['height'] * self.GridHeight)
            map.setPixmap(canvas)
            map.pixmap().fill(QtGui.QColor("white"))

        qp = QPainter(map.pixmap())

        if self.CellSize is None:
                    self.CellSize = {}
                    self.CellSize['width'] = int(map.pixmap().width() / self.GridWidth)
                    self.CellSize['height'] = self.CellSize['width']

        qp.setBrush(QBrush(QColor("black"), Qt.SolidPattern))
        pen = QPen(QtGui.QColor("white"))
        qp.setPen(pen)
        
        cellWidth = floor(int(map.pixmap().width() / self.GridWidth))
        cellHeight = cellWidth

        if map == self.ui.uiColMap:
            zJson = self.CollisionData['Attributes']
        elif map == self.ui.uiColExMap:
            zJson = self.ExData['Attributes']

        #Before we begin drawing the grid, if width x height exceeds the count of ZoneIDs
        #then we need to add new entries to the arrays of each file.
        #print(f"len(zJson)({len(zJson)}\ncellWidth({cellWidth})")

        if self.GridHeight * self.GridWidth > len(zJson):
            for n in range(self.GridHeight*self.GridWidth - len(zJson)):
                zJson.append(-1)
        elif self.GridHeight * self.GridWidth < len(zJson):
            zJson = zJson[:-(len(zJson) - (self.GridHeight * self.GridWidth))]

        if map == self.ui.uiColMap:
            self.CollisionData['Attributes'] = zJson
        elif map == self.ui.uiColExMap:
            self.ExData['Attributes'] = zJson

        for r in range(self.GridHeight):
            for c in range(self.GridWidth):
                tCell = self.GridWidth*r + c
                z = zJson[tCell]
                rect = QRectF(c*cellWidth, r*cellHeight, cellWidth, cellHeight)
                
                if self.SelectedCell is not None and tCell == self.SelectedCell['cell']:
                    qp.setBrush(QBrush(SELECTED, Qt.SolidPattern))
                else:
                    if z == 128:
                        qp.setBrush(QBrush(BLACK, Qt.SolidPattern))
                    elif z == 0:
                        qp.setBrush(QBrush(WHITE, Qt.SolidPattern))
                    elif z == 105128:
                        qp.setBrush(QBrush(ORANGE, Qt.SolidPattern))
                    elif z == 16000:
                        qp.setBrush(QBrush(GREEN, Qt.SolidPattern))
                    elif z == -1:
                        qp.setBrush(QBrush(RED, Qt.SolidPattern))
                    else:
                        qp.setBrush(QBrush(YELLOW, Qt.SolidPattern))

                qp.drawRect(rect)
            
        self.CellWidth = cellWidth
        self.CellHeight = cellHeight


        map.repaint()
    
    def drawOverworldEventMap(self, map):
        if os.path.exists(f"maps/{self.CollisionData['m_Name']}c.png"):
            canvas = QtGui.QPixmap(f"maps/{self.CollisionData['m_Name']}c.png")
            map.setPixmap(canvas)
        else:
            if self.CellSize is None:
                    self.CellSize = {}
                    self.CellSize['width'] = int(map.width() / self.GridWidth)
                    self.CellSize['height'] = self.CellSize['width']

            canvas = QtGui.QPixmap(self.CellSize['width'] * self.GridWidth, self.CellSize['height'] * self.GridHeight)
            map.setPixmap(canvas)
            map.pixmap().fill(QtGui.QColor("white"))

        x = int(self.MapOffsets['col'])
        y = int(self.MapOffsets['row'])

        qp = QPainter(map.pixmap())

        #set up brush for drawing lines
        qp.setBrush(QBrush(GRIDLINE, Qt.SolidPattern))
        pen = QPen(QtGui.QColor("black"))

        for i in range(floor(map.width() / self.CellSize['width'])):
            qp.drawLine(i * self.CellSize['width'], 0, i * self.CellSize['width'], map.height())    
        for j in range(floor(map.height() / self.CellSize['height'])):
            qp.drawLine(0, j * self.CellSize['height'], map.width(), j * self.CellSize['height'])

        
        for key in self.PlaceData:
            pd = self.PlaceData.get(key)
            
            #Just set the filename onto the title of the events window
            if key == 'filename':
                self.setWindowTitle(f"Events ({pd})")            
                continue

            if self.CellSize is None:
                        self.CellSize = {}
                        self.CellSize['width'] = int(map.pixmap().width() / self.GridWidth)
                        self.CellSize['height'] = self.CellSize['width']

            cellWidth = floor(int(map.pixmap().width() / self.GridWidth))
            cellHeight = cellWidth

            pdx = int(pd['data']['Position']['x'] - (x * MAP_WIDTH)) * self.CellSize['width']
            pdy = int(pd['data']['Position']['y'] - (y * MAP_HEIGHT)) * self.CellSize['height']
            pdIndex = f"{floor(pdx/self.CellSize['width'])}{floor(pdy/self.CellSize['height'])}"
            self.PlaceDataCells[pdIndex] = pd

            if self.SelectedPlaceData == pdIndex:
                qp.setBrush(QBrush(SELECTED, Qt.SolidPattern))
            else:
                qp.setBrush(QBrush(RED, Qt.SolidPattern))

            pen = QPen(QtGui.QColor("white"))
            qp.setPen(pen)

            qp.drawRect(pdx, pdy, cellWidth, cellHeight)
        
        if self.EventsMapSelected is not None:
            qp.setBrush(QBrush(SELECTED, Qt.SolidPattern))
            qp.drawRect(self.EventsMapSelected['x'] * self.CellSize['width'],
                self.EventsMapSelected['y'] * self.CellSize['height'],
                cellWidth, cellHeight)

    def movePDLeft(self):
        self.keyPressed(Qt.Key.Key_Left)

    def movePDRight(self):
        self.keyPressed(Qt.Key.Key_Right)

    def movePDUp(self):
        self.keyPressed(Qt.Key.Key_Up)

    def movePDDown(self):
        self.keyPressed(Qt.Key.Key_Down)

    def keyPressed(self, key):
        #EventsMapSelected holds current X and Y position of the grid. e.g. X: 12, Y: 22,
        #and also contains the index into PlaceDataCells

        #SELECTED_PLACEDATA_POS holds the true map position. e.g. X: 112, Y: 878

        #PlaceDataCells holds all valid placedatas on the loaded map

        #MapOffsets holds the "origin" point of the map, i.e. the top left position of the map.
        #MapOffsets X and Y plus 32 are the extents of the map!

        newCol = -1
        newRow = -1
        print('keypressed')
        if key in self.PD_MOVE_KEYS:
            print('move key pressed')
            if self.SelectedPlaceData is None:
                return

            if key == QtCore.Qt.Key.Key_Left:
                if int(self.SELECTED_PLACEDATA_POS['x']) - 1 < int(self.MapOffsets['col'])*MAP_WIDTH:
                    return
                self.SELECTED_PLACEDATA_POS['x'] -= 1
                self.EventsMapSelected['x'] -= 1
                newCol = self.EventsMapSelected['x']
                newRow = self.EventsMapSelected['y']
            elif key == QtCore.Qt.Key.Key_Right:
                if int(self.SELECTED_PLACEDATA_POS['x']) + 1 > int(self.MapOffsets['col'])*MAP_WIDTH + int(MAP_WIDTH):
                    return
                self.SELECTED_PLACEDATA_POS['x'] += 1
                self.EventsMapSelected['x'] += 1
                newCol = self.EventsMapSelected['x']
                newRow = self.EventsMapSelected['y']
            elif key == QtCore.Qt.Key.Key_Up:
                if int(self.SELECTED_PLACEDATA_POS['y']) - 1 < int(self.MapOffsets['row'])*MAP_HEIGHT:
                    return
                self.SELECTED_PLACEDATA_POS['y'] -= 1
                self.EventsMapSelected['y'] -= 1
                newCol = self.EventsMapSelected['x']
                newRow = self.EventsMapSelected['y']
            elif key == QtCore.Qt.Key.Key_Down:
                if int(self.SELECTED_PLACEDATA_POS['y']) + 1 > int(self.MapOffsets['row'])*MAP_HEIGHT + int(MAP_HEIGHT):
                    return
                self.SELECTED_PLACEDATA_POS['y'] += 1
                self.EventsMapSelected['y'] += 1
                newCol = self.EventsMapSelected['x']
                newRow = self.EventsMapSelected['y']
            
            if self.PlaceDataCells.get(f"{newCol}{newRow}") is not None:
                self.fillPlaceDataDetails(newCol, newRow, self.PlaceDataCells[f"{newCol}{newRow}"])
            else:
                newPD = PLACEDATA_NEW
                newPD['data']['Position']['x'] = self.SELECTED_PLACEDATA_POS['x']
                newPD['data']['Position']['y'] = self.SELECTED_PLACEDATA_POS['y']
                newPD['filename'] = self.PlaceData['filename']
                self.fillPlaceDataDetails(newCol, newRow, newPD)

            self.drawOverworldEventMap(self.ui.uiEventsMap)


    def mousePressed(self, event, map):
            self.SelectedCell = None

            if self.CellHeight == 0:
                return
                
            row = int((event.y() / self.CellHeight))
            col = int((event.x() / self.CellWidth))
            cell = row * self.GridWidth + col

            self.CellMatrix = {'col':'{:0>2}'.format(col), 'row':'{:0>2}'.format(row)}
            self.SelectedCell = {
                'cell': cell,
                'map': map
            }

            if self.SelectedCell['cell'] > (self.GridHeight * self.GridWidth):
                self.SelectedCell = None
                self.drawCollision(map)
                return

            self.ui.uiColValue.setText(str(self.CollisionData['Attributes'][self.SelectedCell['cell']]))
            self.ui.uiColExValue.setText(str(self.ExData['Attributes'][self.SelectedCell['cell']]))

            if not (COLLISIONS.get(self.CollisionData['Attributes'][self.SelectedCell['cell']])) is None:
                self.ui.comboBoxCollisionTile.setCurrentText(COLLISIONS[self.CollisionData['Attributes'][self.SelectedCell['cell']]])
            else:
                self.UpdateTile = False
                self.ui.comboBoxCollisionTile.setCurrentText("UNKNOWN")
                self.UpdateTile = True

            self.drawCollision(map)

    def eventsMousePressed(self, event, map):
        self.SelectedPlaceData = None
        self.EventsMapSelected = None

        if self.CellHeight == 0:
            return
            
        row = floor((event.y() / self.CellHeight))
        col = floor((event.x() / self.CellWidth))

        self.EventsMapSelected = {'x': col, 'y': row}

        if self.PlaceDataCells.get(f"{col}{row}"):
            # print (self.PlaceDataCells[f"{col}{row}"])
            print(f"Setting selected PlaceData to: {col}{row}")
            self.SelectedPlaceData = f"{col}{row}"
            self.fillPlaceDataDetails(col, row, self.PlaceDataCells[self.SelectedPlaceData])
        else:
            self.ui.uiEventsScript.setPlainText('')
            newPD = PLACEDATA_NEW
            newPD['data']['Position']['x'] = (int(self.MapOffsets['col'])*MAP_WIDTH + int(col))
            newPD['data']['Position']['y'] = (int(self.MapOffsets['row'])*MAP_HEIGHT + int(row))
            newPD['filename'] = self.PlaceData['filename']
            self.fillPlaceDataDetails(col, row, newPD)

        self.drawOverworldEventMap(map)

    def fillPlaceDataDetails(self, col, row, pd):
        script = ""
        contactScript = ""

        if self.EV_SCRIPT.get(pd['data']['TalkLabel']) is not None:
            script = f"{self.EV_SCRIPT[pd['data']['TalkLabel']][0]}"

            for i in range(1, len(self.EV_SCRIPT[pd['data']['TalkLabel']])):
                script = f"{script}\n{self.EV_SCRIPT[pd['data']['TalkLabel']][i]}"
        
        if self.EV_SCRIPT.get(pd['data']['ContactLabel']) is not None:
            contactScript = f"{self.EV_SCRIPT[pd['data']['Contactlabel']][0]}"
            for j in range(1, len(self.EV_SCRIPT[pd['data']['ContactLabel']])):
                contactScript = f"{contactScript}\n{self.EV_SCRIPT[pd['data']['ContactLabel']][i]}"
                
        self.ui.uiEventsScript.setPlainText(script)
        self.ui.uiEventsScriptContact.setPlainText(contactScript)

        self.ui.pdID.setText(pd['data']['ID'])
        self.ui.pdTrainerID.setText(str(pd['data']['TrainerID']))
        self.ui.pdOGI.setText(str(pd['data']['ObjectGraphicIndex']))
        self.ui.pdPositionX.setValue(int(pd['data']['Position']['x']))
        self.ui.pdPositionY.setValue(int(pd['data']['Position']['y']))
        self.ui.pdHeightLayer.setText(str(pd['data']['HeightLayer']))
        self.ui.pdRotation.setCurrentText(ROTATION[pd['data']['Rotation']])
        self.ui.pdMoveLimitX.setValue(int(pd['data']['MoveLimit']['x']))
        self.ui.pdMoveLimitY.setValue(int(pd['data']['MoveLimit']['y']))
        self.ui.pdMoveCode.setText (str(pd['data']['MoveCode']))
        self.ui.pdMoveParam0.setText(str(pd['data']['MoveParam0']))
        self.ui.pdMoveParam1.setText(str(pd['data']['MoveParam1']))
        self.ui.pdMoveParam2.setText(str(pd['data']['MoveParam2']))
        self.ui.pdTalkLabel.setText(str(pd['data']['TalkLabel']))
        self.ui.pdContactLabel.setText(str(pd['data']['ContactLabel']))
        self.ui.pdWork.setText(str(pd['data']['Work']))
        self.ui.pdDowsing.setText(str(pd['data']['Dowsing']))
        self.ui.pdLoadFirst.setChecked(pd['data']['LoadFirst'] != 0)
        self.ui.pdDoNotLoad.setText(str(pd['data']['DoNotLoad']))
        self.ui.pdTalkToRange.setText(str(pd['data']['TalkToRange']))
        self.ui.pdTalkToSizeX.setText(str(pd['data']['TalkToSize']['x']))
        self.ui.pdTalkToSizeY.setText(str(pd['data']['TalkToSize']['y']))
        self.ui.pdTalkBit.setText(str(pd['data']['TalkBit']))

        #Set the true BDSP map position for later use.
        self.SELECTED_PLACEDATA_POS = { 
            'x': int(pd['data']['Position']['x']),
            'y': int(pd['data']['Position']['y'])
        }

    def printTest(self, msg):
        QMessageBox.information(self, '', msg)


    def saveEvent(self):
        #Get the SelectedPlaceData and overwrite the corresponding entry in the loaded placedata.


        return

    def saveMatrix(self):
        if os.path.exists("output") is False:
            os.makedirs("output")
            
        with open(f"output/{self.CollisionData['m_Name']}.json", 'w+') as out:
            json.dump(self.CollisionData, out)
        with open(f"output/{self.ExData['m_Name']}.json", 'w+') as out:
            json.dump(self.ExData, out)
