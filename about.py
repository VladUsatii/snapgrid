#!/usr/bin/env python3
import sys, os
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from AppKit import NSScreen

class About(QMainWindow):
	def __init__(self):
		super().__init__()
		self.screenSize = [int(NSScreen.mainScreen().frame().size.width), int(NSScreen.mainScreen().frame().size.height)]
		# <MainWindow>
		self.setFixedSize(screenSize[0]//2, screenSize[1]//2)
		self.setStyleSheet("QMainWindow{background-color: white;border: 1px solid black}")
		self.setWindowFlags(Qt.FramelessWindowHint)
		self.center()
		# </MainWindow>

		# <Label>
		self.lbl = QLabel(self)
		self.lbl.setText("About Snapgrid")
		self.lbl.setStyleSheet("QLabel{color:black;font: bold 22pt 'Helvetica Neue';}")
		self.lbl.setGeometry(5, 5, screenSize[0]//6, screenSize[1]//10)
		# </Label>

		self.oldPos = self.pos()
		self.show()

		def center(self):
			qr = self.frameGeometry()
			cp = QDesktopWidget().availableGeometry().center()
			qr.moveCenter(cp)
			self.move(qr.topLeft())

		def mousePressEvent(self, event):
			self.oldPos = event.globalPos()

		def mouseMoveEvent(self, event):
			delta = QPoint(event.globalPos() - self.oldPos)
			self.move(self.x() + delta.x(), self.y() + delta.y())
			self.oldPos = event.globalPos()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	ex = About()
	sys.exit(app.exec_())
