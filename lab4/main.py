import sys  # sys нужен для передачи argv в QApplication
import os  # Отсюда нам понадобятся методы для отображения содержимого директорий
from PyQt5 import QtWidgets
import design  # Это наш конвертированный файл дизайна

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.ifconfig_button.clicked.connect(self.ifconfig_click)
        self.getmac_button.clicked.connect(self.getmac_click)
        self.route_button.clicked.connect(self.route_click)
        self.nmblookup_button.clicked.connect(self.nmblookup_click)
        self.traceroute_button.clicked.connect(self.traceroute_click)
        self.ping_button.clicked.connect(self.ping_click)
	
    def ifconfig_click(self):
        self.cmdRead("ifconfig")
        
    def getmac_click(self):
        self.cmdRead("ip a | grep ether | gawk '{print $2}'")
        
    def route_click(self):
        self.cmdRead("route")
    
    def nmblookup_click(self):
        self.cmdReadParam("nmblookup", self.nmblookup_text.toPlainText())
        
    def traceroute_click(self):
        self.cmdReadParam("traceroute -I", self.traceroute_text.toPlainText())
    
    def ping_click(self):
        self.cmdReadParam("ping -c 5", self.ping_text.toPlainText())
        
    def cmdRead(self, cmdText):
        myCmd = os.popen(cmdText)
        res = myCmd.read()
        myCmd.close()
        self.result.setPlainText(res)
        
    def cmdReadParam(self, cmdText, addText):
        myCmd = os.popen(cmdText + " " + addText)
        res = myCmd.read()
        myCmd.close()
        self.result.setPlainText(res)
	
def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
