from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

import sys

class mainWindow(QMainWindow):
  def __init__(thewindow):
    super().__init__()
    thewindow.setWindowTitle('WebBrowser')
    
    thewindow.browser = QWebEngineView()
    thewindow.browser.setUrl(QUrl("http://google.com"))
    thewindow.setCentralWidget(thewindow.browser)
    
    thewindow.navigation = QToolBar('Navigation Toolbar')
    thewindow.addToolBar(thewindow.navigation)
    
    back_button = QAction('back',thewindow)
    back_button.triggered.connect(thewindow.browser.back)
    thewindow.navigation.addAction(back_button)
    
    forward_button = QAction('forward',thewindow)
    forward_button.triggered.connect(thewindow.browser.forward)
    thewindow.navigation.addAction(forward_button)
    
    thewindow.showMaximized()
    
app=QApplication(sys.argv)
window=mainWindow()

app.exec_()
