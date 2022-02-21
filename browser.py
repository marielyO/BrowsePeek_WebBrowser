import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar

class MainWindow(QMainWindow):
  def __init__(thewindow):
    super().__init__()
    thewindow.setWindowTitle('WebBrowser')
    thewindow.resize(2000,1000)
    
    thewindow.nav_bar = QToolBar('Navigation Toolbar')
    thewindow.addToolBar(thewindow.nav_bar)
    
    
app=QApplication(sys.argv)
window=MainWindow()
window.show()

sys.exit(app.exec_())
