from PyQt5.QtCore import pyqtSignal, QObject



class people(QObject):
    sendSignal = pyqtSignal()

    def __init__(self):
        QObject.__init__(self)



    def send(self):
        self.sendSignal.emit()


    def tosql(self):
        print("jkjj")


people = people()
# подключение сигнала cracked к слоту crackit
#people.sendSignal.connect(people.tosql)
#people.send()