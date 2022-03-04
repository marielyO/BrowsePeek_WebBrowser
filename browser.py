from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

import sys

class mainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle('WebBrowser')
    
    self.browser = QWebEngineView()
    self.browser.setUrl(QUrl("http://google.com"))
    self.setCentralWidget(self.browser)
    
    self.navigation = QToolBar('Navigation Toolbar')
    self.addToolBar(self.navigation)
    
    back_button = QAction('back',self)
    back_button.triggered.connect(self.browser.back)
    self.navigation.addAction(back_button)
    
    forward_button = QAction('forward',self)
    forward_button.triggered.connect(self.browser.forward)
    self.navigation.addAction(forward_button)
    
    self.showMaximized()
    
app=QApplication(sys.argv)
window=mainWindow()

app.exec_()
