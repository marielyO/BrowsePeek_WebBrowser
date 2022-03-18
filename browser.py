from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction, QStatusBar
from PyQt5.QtGui import QIcon 
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

import sys

class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('BrowsePeek')
    
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://google.com"))
        self.setCentralWidget(self.browser)
    
        self.navigation = QToolBar('Navigation Toolbar')
        self.addToolBar(self.navigation)
        
        self.status = QStatusBar()
        self.setStatusBar(self.status)
    
        back_button = QAction('back', self)
        back_button.setStatusTip('Go back to previous page')
        back_button.triggered.connect(self.browser.back)
        self.navigation.addAction(back_button)
    
        reload_button = QAction('reload', self)
        reload_button.setStatusTip('Reload page')
        reload_button.triggered.connect(self.browser.reload)
        self.navigation.addAction(reload_button)
        
        forward_button = QAction('forward', self)
        forward_button.setStatusTip('Go to next page')
        forward_button.triggered.connect(self.browser.forward)
        self.navigation.addAction(forward_button)
    
        home_button = QAction('home', self)
        home_button.setStatusTip('Go to home page')
        home_button.triggered.connect(self.home)
        self.navigation.addAction(home_button)
        
        self.showMaximized()
    
    
    def home(self):
        self.browser.setUrl(QUrl("http://google.com"))
       
    
app = QApplication(sys.argv)
window = mainWindow()

app.exec_()
