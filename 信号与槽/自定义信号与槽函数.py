from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
import sys

class WinForm(QWidget):
    
    button_clicked_signal=pyqtSignal()
    
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("自定义信号与槽实例")
        self.resize(330,50)
        btn =QPushButton("测试按钮",self)
        btn.clicked.connect(self.btn_clicked)
        
        self.button_clicked_signal.connect(self.btn_closed)

    def btn_clicked(self):
        self.button_clicked_signal.emit()


    def btn_closed(self):
        self.close()
        
if __name__=="__main__":
    app=QApplication(sys.argv)
    win=WinForm()
    win.show()
    sys.exit(app.exec_())
