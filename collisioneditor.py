from tqdm import tqdm
from map import *
from math import floor
from tkinter import filedialog
from tkinter import *
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor
from PyQt5.QtCore import Qt, QRectF
import clicklabel
import collision


class CollisionEditor(QWidget):
    
    CellHeight = 0
    CollisionData = None
    ExData = None
    GridHeight = 0
    GridWidth = 0
    Loading = True
    SelectedCell = None
    CellSize = None

    def __init__(self, collisionData, exData, parent=None):
        super().__init__()
        self.ui = collision.Ui_CollisionEditor()
        self.ui.setupUi(self)
        self.ui.uiColMap.clicked.connect(self.mousePressed)
        self.ui.uiColHeightSB.valueChanged.connect(self.heightChanged)
        self.ui.uiColWidthSB.valueChanged.connect(self.widthChanged)

        self.CollisionData = collisionData
        self.ExData = exData

        #Since the map and map_*_ex files are intended to go together, we will assume they
        #should have the same dimensions.

        self.GridWidth = self.CollisionData['Width']
        self.GridHeight = int(len(self.CollisionData['Attributes']) / self.GridWidth)

        self.ui.uiColHeightSB.setValue(self.GridHeight)
        self.ui.uiColWidthSB.setValue(self.GridWidth)
        self.drawCollisions()
        self.Loading = False


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

    def drawCollision(self, map):
        if self.CellSize is None:
            self.CellSize = {}
            self.CellSize['width'] = int(map.width() / self.GridWidth)
            self.CellSize['height'] = self.CellSize['width']

        canvas = QtGui.QPixmap(self.CellSize['width'] * self.GridWidth, self.CellSize['height'] * self.GridHeight)
        map.setPixmap(canvas)
        map.pixmap().fill(QtGui.QColor("white"))
        qp = QPainter(map.pixmap())

        qp.setBrush(QBrush(QColor("black"), Qt.SolidPattern))
        pen = QPen(QtGui.QColor("white"))
        qp.setPen(pen)
        
        print(f"uiColMapWidth({map.width()}")
        cellWidth = floor(int(map.width() / self.GridWidth))
        cellHeight = cellWidth

        zJson = self.CollisionData['Attributes']

        #Before we begin drawing the grid, if width x height exceeds the count of ZoneIDs
        #then we need to add new entries to the arrays of each file.
        print(f"len(zJson)({len(zJson)}\ncellWidth({cellWidth})")

        if self.GridHeight * self.GridWidth > len(zJson):
            for n in range(self.GridHeight*self.GridWidth - len(zJson)):
                zJson.append(-1)
        elif self.GridHeight * self.GridWidth < len(zJson):
            zJson = zJson[:-(len(zJson) - (self.GridHeight * self.GridWidth))]

        self.CollisionData['Attributes'] = zJson

        for r in range(self.GridHeight):
            for c in range(self.GridWidth):
                tCell = self.GridWidth*r + c
                z = zJson[tCell]
                rect = QRectF(c*cellWidth, r*cellHeight, cellWidth, cellHeight)
                
                if z == 128:
                    qp.setBrush(QBrush(QColor("black"), Qt.SolidPattern))
                elif z == 0:
                    qp.setBrush(QBrush(QColor("white"), Qt.SolidPattern))
                elif z == 105128:
                    qp.setBrush(QBrush(QColor("orange"), Qt.SolidPattern))
                elif z == 16000:
                    qp.setBrush(QBrush(QColor("blue"), Qt.SolidPattern))
                elif z == -1:
                    qp.setBrush(QBrush(QColor("red"), Qt.SolidPattern))

                qp.drawRect(rect)
            
        self.CellWidth = cellWidth
        self.CellHeight = cellHeight


        map.repaint()
    
    def mousePressed(self, event, map):
            self.SelectedCell = None

            if self.CellHeight == 0:
                return

            x = floor(event.x() / self.ui.uiColMap.width())
            y = floor(event.y() / self.ui.uiColMap.height())

            row = int((event.y() / self.CellHeight))
            col = int((event.x() / self.CellWidth))
            cell = row * self.GridWidth + col

            self.CellMatrix = {'col':'{:0>2}'.format(col), 'row':'{:0>2}'.format(row)}
            self.SelectedCell = cell

            if self.SelectedCell > (self.GridHeight * self.GridWidth):
                self.SelectedCell = None
                self.drawCollisions()
                return

            self.ui.uiColValue.setText(str(self.CollisionData['Attributes'][self.SelectedCell]))
            self.drawCollisions()
