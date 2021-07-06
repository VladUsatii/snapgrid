#!/usr/bin/env python3
import sys, os
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QDesktopWidget
from AppKit import NSScreen

class About(QMainWindow):
	def __init__(self):
		super().__init__()
		# silence terminal
		self.screenSize = [int(NSScreen.mainScreen().frame().size.width), int(NSScreen.mainScreen().frame().size.height)]
		# <MainWindow>
		self.setFixedSize(self.screenSize[0]//2, self.screenSize[1]//2)
		self.setStyleSheet("QMainWindow{background-color: white;border: 1px solid black}")
		self.setWindowFlags(Qt.FramelessWindowHint)
		self.center()
		# </MainWindow>

		# TITLE

		# <Label>
		self.lbl = QLabel(self)
		self.lbl.setText("Snapgrid")
		self.lbl.setStyleSheet("QLabel{color:black;font: bold 22pt 'Helvetica Neue';}")
		self.lbl.setGeometry(20, 5, 100, 50)
		# </Label>

		# ABOUT

		# <Label>
		self.lbl2 = QLabel(self)
		self.lbl2.setText("About Us")
		self.lbl2.setStyleSheet("QLabel{color:black;font: bold 18pt 'Helvetica Neue';}")
		self.lbl2.setGeometry(20, 50, 400, 50)
		# </Label>

		# <Label>
		self.lbl3 = QLabel(self)
		self.lbl3.setText("Snapgrid is an open-source initiative to improve workflow of programmers\nall around the world. We hope to help speed up mouse events through snapping\napplications with Terminal. In the future, we may assist in speeding up\nsearch, penetration, or with utility tasks (regulating startup apps, etc.).")
		self.lbl3.setStyleSheet("QLabel{color:black;font: 15pt 'Helvetica Neue';}")
		self.lbl3.setGeometry(20, 60, self.screenSize[0]//2.5, 150)
		# </Label>

		# CONTRIBUTORS

		# <Label>
		self.lbl4 = QLabel(self)
		self.lbl4.setText("Contributors")
		self.lbl4.setStyleSheet("QLabel{color:black;font: bold 18pt 'Helvetica Neue';}")
		self.lbl4.setGeometry(20, 200, 200, 50)
		# </Label>

		# <Label>
		self.lbl5 = QLabel(self)
		self.lbl5.setText("Vlad Usatii, <i>founder of <a href='youshould.readproduct.com/'>youshould.readproduct.com</a></i>")
		self.lbl5.setStyleSheet("QLabel{color:black;font: 16pt 'Helvetica Neue';}")
		self.lbl5.setGeometry(20, 190, self.screenSize[0]//2.5, 150)

		self.lbl6 = QLabel(self)
		self.lbl6.setText("<b>Submit a pull request and successfully get accepted code in order to be featured here.</b>")
		self.lbl6.setStyleSheet("QLabel{color:black;font: 16pt 'Helvetica Neue';}")
		self.lbl6.setGeometry(20, 240, self.screenSize[0]//2.5, 150)
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
