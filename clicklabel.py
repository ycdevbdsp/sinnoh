
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QLabel
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor
from PyQt5 import QtCore
class ClickLabel(QLabel):
    clicked = QtCore.pyqtSignal(QtCore.QPoint, QLabel)
    released = QtCore.pyqtSignal(QtCore.QPoint)

    mapData = None

    def resizeEvent(self, event):
        print(f'Map Resized: {self.objectName()}\nwidth: {self.width()}\nheight: {self.height()}')

    def mousePressEvent(self, event):
        self.clicked.emit(event.pos(), self)