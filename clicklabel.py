
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QLabel
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor
from PyQt5 import QtCore
class ClickLabel(QLabel):
    clicked = QtCore.pyqtSignal(QtCore.QPoint, QLabel)
    released = QtCore.pyqtSignal(QtCore.QPoint)
    doubleclicked = QtCore.pyqtSignal(QtCore.QPoint, QLabel)
    keypressed = QtCore.pyqtSignal(int)
    mapData = None
    overworld = False

    def keyPressEvent(self, event):
        print('keypressevent')
        self.keypressed.emit(event.key())

    def resizeEvent(self, event):
        return

    def mousePressEvent(self, event):
        self.clicked.emit(event.pos(), self)

    def mouseDoubleClickEvent(self, event):
        self.doubleclicked.emit(event.pos(), self)